"""Parquet schema for per-singer pose + face landmark features.

Wide format with named MediaPipe landmarks. Each row is one frame, one singer.

Reference:
- MediaPipe Pose: 33 landmarks (BlazePose), see POSE_LANDMARK_NAMES below
- FaceMesh lip subset: 40 indices (outer + inner lip contours) — UPPER_LIP + LOWER_LIP
"""

from __future__ import annotations

from typing import Final

import pyarrow as pa

POSE_LANDMARK_NAMES: Final[tuple[str, ...]] = (
    "nose",
    "left_eye_inner", "left_eye", "left_eye_outer",
    "right_eye_inner", "right_eye", "right_eye_outer",
    "left_ear", "right_ear",
    "mouth_left", "mouth_right",
    "left_shoulder", "right_shoulder",
    "left_elbow", "right_elbow",
    "left_wrist", "right_wrist",
    "left_pinky", "right_pinky",
    "left_index", "right_index",
    "left_thumb", "right_thumb",
    "left_hip", "right_hip",
    "left_knee", "right_knee",
    "left_ankle", "right_ankle",
    "left_heel", "right_heel",
    "left_foot_index", "right_foot_index",
)

LIP_LANDMARK_INDICES: Final[tuple[int, ...]] = (
    61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291, 308,
    324, 318, 402, 317, 14, 87, 178, 88, 95,
    78, 191, 80, 81, 82, 13, 312, 311, 310, 415,
    185, 40, 39, 37, 0, 267, 269, 270, 409,
)

METADATA_COLUMNS: Final[tuple[tuple[str, pa.DataType], ...]] = (
    ("frame_idx", pa.int64()),
    ("time_sec", pa.float64()),
    ("singer_id", pa.string()),
)

DERIVED_COLUMNS: Final[tuple[tuple[str, pa.DataType], ...]] = (
    ("shoulder_rise", pa.float32()),
    ("head_sway", pa.float32()),
    ("trunk_lean", pa.float32()),
)


def build_pose_schema() -> pa.Schema:
    """Build the canonical pose+face parquet schema."""
    fields: list[pa.Field] = []
    for name, dtype in METADATA_COLUMNS:
        fields.append(pa.field(name, dtype))
    for landmark in POSE_LANDMARK_NAMES:
        for axis in ("x", "y", "z", "vis"):
            fields.append(pa.field(f"pose_{landmark}_{axis}", pa.float32()))
    for idx in LIP_LANDMARK_INDICES:
        for axis in ("x", "y"):
            fields.append(pa.field(f"lip_{idx}_{axis}", pa.float32()))
    for name, dtype in DERIVED_COLUMNS:
        fields.append(pa.field(name, dtype))
    return pa.schema(fields)


SCHEMA_VERSION: Final[str] = "wp2-pose-v1"
POSE_COLUMNS: Final[list[str]] = [f.name for f in build_pose_schema()]
