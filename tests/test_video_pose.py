"""Smoke tests for WP2 pose extraction.

Uses a synthetic short video (no human silhouette → all landmarks NaN) to verify
the extraction pipeline handles missing detections cleanly and writes a valid
parquet with the canonical schema.
"""

from __future__ import annotations

from pathlib import Path

import cv2
import numpy as np
import pyarrow.parquet as pq
import pytest

from choir_entanglement.video.pose import extract_pose_to_parquet
from choir_entanglement.video.schema import (
    LIP_LANDMARK_INDICES,
    POSE_LANDMARK_NAMES,
    SCHEMA_VERSION,
    build_pose_schema,
)


@pytest.fixture
def synthetic_video(tmp_path: Path) -> Path:
    """Write a 1-second 30-fps grey video (no human → no landmarks)."""
    out = tmp_path / "synthetic.mp4"
    width, height, fps = 320, 240, 30
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # type: ignore[attr-defined]
    writer = cv2.VideoWriter(str(out), fourcc, fps, (width, height))
    frame = np.full((height, width, 3), 128, dtype=np.uint8)
    for _ in range(fps):
        writer.write(frame)
    writer.release()
    assert out.exists() and out.stat().st_size > 0
    return out


def test_schema_has_metadata_pose_lip_derived_columns() -> None:
    schema = build_pose_schema()
    names = set(schema.names)
    assert {"frame_idx", "time_sec", "singer_id"} <= names
    for landmark in POSE_LANDMARK_NAMES:
        for axis in ("x", "y", "z", "vis"):
            assert f"pose_{landmark}_{axis}" in names
    for idx in LIP_LANDMARK_INDICES:
        assert f"lip_{idx}_x" in names
        assert f"lip_{idx}_y" in names
    assert {"shoulder_rise", "head_sway", "trunk_lean"} <= names


def test_extract_pose_writes_parquet_with_correct_schema(
    synthetic_video: Path, tmp_path: Path
) -> None:
    out = tmp_path / "pose.parquet"
    df = extract_pose_to_parquet(synthetic_video, out, singer_id="S1")

    assert out.exists()
    assert len(df) == 30
    assert (df["singer_id"] == "S1").all()
    assert df["frame_idx"].tolist() == list(range(30))
    assert np.allclose(df["time_sec"].iloc[1] - df["time_sec"].iloc[0], 1 / 30, atol=1e-3)


def test_parquet_metadata_records_schema_version(synthetic_video: Path, tmp_path: Path) -> None:
    out = tmp_path / "pose.parquet"
    extract_pose_to_parquet(synthetic_video, out, singer_id="A1")
    table = pq.read_table(out)
    metadata = table.schema.metadata or {}
    assert metadata.get(b"schema_version") == SCHEMA_VERSION.encode()
    assert metadata.get(b"singer_id") == b"A1"


def test_landmarks_are_nan_when_no_human_in_frame(synthetic_video: Path, tmp_path: Path) -> None:
    out = tmp_path / "pose.parquet"
    df = extract_pose_to_parquet(synthetic_video, out, singer_id="T1")
    assert df["pose_nose_x"].isna().all()
    assert df["shoulder_rise"].isna().all()
