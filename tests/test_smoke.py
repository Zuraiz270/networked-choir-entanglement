"""Canary smoke tests.

Not feature tests. These prove the stack resolves at runtime so silent data
bugs (FM5 in the scaffold plan) do not slip through to the May 8 milestone.
"""

import numpy as np


def test_package_imports() -> None:
    """Top-level package and WP namespaces all import cleanly."""
    import choir_entanglement
    from choir_entanglement import audio, dashboard, network, video

    assert choir_entanglement.__version__ == "0.0.1"
    assert all(m is not None for m in (audio, video, network, dashboard))


def test_librosa_pyin_on_example() -> None:
    """librosa.pyin extracts a non-all-NaN F0 contour from the trumpet example.

    Guards against the scenario where we pin librosa to a version whose pyin
    silently returns NaN on real inputs.
    """
    import librosa

    y, sr = librosa.load(librosa.ex("trumpet"), duration=2.0)
    f0, voiced, _ = librosa.pyin(
        y,
        fmin=float(librosa.note_to_hz("C2")),
        fmax=float(librosa.note_to_hz("C7")),
        sr=sr,
    )
    assert f0 is not None
    assert not np.all(np.isnan(f0)), "pyin returned all-NaN on trumpet example"
    assert voiced.any(), "no voiced frames detected"


def test_mediapipe_pose_instantiates() -> None:
    """MediaPipe Pose instantiates and returns a result object on a blank frame.

    Guards against the scenario where a MediaPipe wheel installs but the
    TensorFlow Lite delegate fails at runtime.
    """
    import mediapipe as mp

    pose = mp.solutions.pose.Pose(static_image_mode=True)
    assert pose is not None
    blank = np.zeros((480, 640, 3), dtype=np.uint8)
    result = pose.process(blank)
    assert result is not None
