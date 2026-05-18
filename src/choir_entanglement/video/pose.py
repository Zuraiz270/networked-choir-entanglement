"""MediaPipe Pose + FaceMesh extraction to parquet.

Usage:
    from choir_entanglement.video.pose import extract_pose_to_parquet
    extract_pose_to_parquet(Path("video.mp4"), Path("out.parquet"), singer_id="A1")
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path
from typing import Any

import cv2
import mediapipe as mp
import numpy as np
import numpy.typing as npt
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from .schema import (
    LIP_LANDMARK_INDICES,
    POSE_LANDMARK_NAMES,
    SCHEMA_VERSION,
    build_pose_schema,
)

FrameRow = dict[str, Any]
RgbArray = npt.NDArray[np.uint8]
NULL_F32 = np.float32("nan")


def extract_pose_to_parquet(
    video_path: Path,
    output_parquet: Path,
    singer_id: str,
    frame_skip: int = 1,
    max_frames: int | None = None,
) -> pd.DataFrame:
    """Run MediaPipe Pose + FaceMesh on a video, write per-frame parquet, return df.

    Args:
        frame_skip: process every Nth source frame (1=all, 3=every third).
        max_frames: optional cap on processed frames (None=full video).
    """
    rows = _run_extraction(video_path, singer_id, frame_skip, max_frames)
    df = pd.DataFrame(rows, columns=build_pose_schema().names)
    output_parquet.parent.mkdir(parents=True, exist_ok=True)
    table = pa.Table.from_pandas(df, schema=build_pose_schema(), preserve_index=False)
    table = _stamp_metadata(table, video_path, singer_id)
    pq.write_table(table, output_parquet)
    return df


def _run_extraction(
    video_path: Path, singer_id: str, frame_skip: int, max_frames: int | None
) -> list[FrameRow]:
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise FileNotFoundError(f"Cannot open video: {video_path}")
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    pose = mp.solutions.pose.Pose(static_image_mode=False, model_complexity=1)
    face = mp.solutions.face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)
    rows: list[FrameRow] = []
    source_idx = 0
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            if source_idx % frame_skip == 0:
                rgb: RgbArray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).astype(np.uint8)
                rows.append(_frame_to_row(rgb, pose, face, source_idx, fps, singer_id))
                if max_frames is not None and len(rows) >= max_frames:
                    break
            source_idx += 1
    finally:
        cap.release()
        pose.close()
        face.close()
    return rows


def _frame_to_row(
    rgb: RgbArray, pose: Any, face: Any, frame_idx: int, fps: float, singer_id: str
) -> FrameRow:
    row: FrameRow = {
        "frame_idx": frame_idx,
        "time_sec": frame_idx / fps,
        "singer_id": singer_id,
    }
    pose_result = pose.process(rgb)
    landmarks = getattr(pose_result, "pose_landmarks", None)
    for i, name in enumerate(POSE_LANDMARK_NAMES):
        lm = landmarks.landmark[i] if landmarks else None
        row[f"pose_{name}_x"] = np.float32(lm.x) if lm else NULL_F32
        row[f"pose_{name}_y"] = np.float32(lm.y) if lm else NULL_F32
        row[f"pose_{name}_z"] = np.float32(lm.z) if lm else NULL_F32
        row[f"pose_{name}_vis"] = np.float32(lm.visibility) if lm else NULL_F32

    face_result = face.process(rgb)
    face_landmarks = getattr(face_result, "multi_face_landmarks", None)
    face_pts = face_landmarks[0].landmark if face_landmarks else None
    for idx in LIP_LANDMARK_INDICES:
        lm = face_pts[idx] if face_pts else None
        row[f"lip_{idx}_x"] = np.float32(lm.x) if lm else NULL_F32
        row[f"lip_{idx}_y"] = np.float32(lm.y) if lm else NULL_F32

    row["shoulder_rise"] = _shoulder_rise(row)
    row["head_sway"] = _head_sway(row)
    row["trunk_lean"] = _trunk_lean(row)
    return row


def _shoulder_rise(row: FrameRow) -> np.float32:
    """Vertical midpoint of left+right shoulder (proxy for breathing)."""
    ly = row["pose_left_shoulder_y"]
    ry = row["pose_right_shoulder_y"]
    if np.isnan(ly) or np.isnan(ry):
        return NULL_F32
    return np.float32((ly + ry) / 2.0)


def _head_sway(row: FrameRow) -> np.float32:
    """Horizontal nose position relative to shoulder midpoint."""
    nx = row["pose_nose_x"]
    lx = row["pose_left_shoulder_x"]
    rx = row["pose_right_shoulder_x"]
    if any(np.isnan([nx, lx, rx])):
        return NULL_F32
    return np.float32(nx - (lx + rx) / 2.0)


def _trunk_lean(row: FrameRow) -> np.float32:
    """Tilt angle (rad) of shoulder-hip line vs vertical."""
    keys = [
        "pose_left_shoulder_x", "pose_left_shoulder_y",
        "pose_left_hip_x", "pose_left_hip_y",
    ]
    if any(np.isnan(row[k]) for k in keys):
        return NULL_F32
    dx = row["pose_left_hip_x"] - row["pose_left_shoulder_x"]
    dy = row["pose_left_hip_y"] - row["pose_left_shoulder_y"]
    return np.float32(np.arctan2(dx, dy))


def _stamp_metadata(table: pa.Table, video_path: Path, singer_id: str) -> pa.Table:
    metadata = {
        b"schema_version": SCHEMA_VERSION.encode(),
        b"source_video": str(video_path).encode(),
        b"singer_id": singer_id.encode(),
        b"mediapipe_version": getattr(mp, "__version__", "unknown").encode(),
        b"extraction_date": dt.datetime.now(dt.UTC).isoformat().encode(),
    }
    return table.replace_schema_metadata({**(table.schema.metadata or {}), **metadata})
