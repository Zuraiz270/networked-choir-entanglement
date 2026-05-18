"""Generate WP2 visual-feature figure from the Sprint-2 pilot pose parquet."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

POSE_PARQUET = Path("data/processed/tier1/ouFyQKszE_Y/pose.parquet")
FIGURE_OUT = Path("data/figures/wp2_visual_features.png")


def run() -> None:
    df = pd.read_parquet(POSE_PARQUET)
    voiced = df["pose_nose_x"].notna()

    fig, axes = plt.subplots(3, 1, figsize=(11, 7), sharex=True)

    axes[0].plot(df["time_sec"], df["head_sway"], color="#1f77b4", linewidth=0.9)
    axes[0].set_ylabel("Head sway\n(nose vs shoulder midpoint)")
    axes[0].grid(True, alpha=0.3)
    axes[0].set_title(
        "WP2 visual features · Tier-1 SoundJack rehearsal (ouFyQKszE_Y, 12 singers)\n"
        f"MediaPipe Pose detection rate: {voiced.mean()*100:.1f}% of {len(df)} frames"
    )

    axes[1].plot(df["time_sec"], df["shoulder_rise"], color="#2ca02c", linewidth=0.9)
    axes[1].set_ylabel("Shoulder rise\n(breath proxy)")
    axes[1].grid(True, alpha=0.3)

    axes[2].plot(df["time_sec"], df["trunk_lean"], color="#d62728", linewidth=0.9)
    axes[2].set_ylabel("Trunk lean\n(rad)")
    axes[2].set_xlabel("Time (s)")
    axes[2].grid(True, alpha=0.3)

    fig.tight_layout()
    FIGURE_OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURE_OUT, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Figure: {FIGURE_OUT}")


if __name__ == "__main__":
    run()
