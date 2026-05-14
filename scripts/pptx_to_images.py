"""Convert a .pptx file to per-slide PNG images via PowerPoint COM (Windows).

Usage:
    python scripts/pptx_to_images.py <input.pptx> <output_dir>

Falls back gracefully if PowerPoint is not available.
"""

from __future__ import annotations

import os
import sys
import time
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python pptx_to_images.py <input.pptx> <output_dir>")
        return 2

    in_path = Path(sys.argv[1]).resolve()
    out_dir = Path(sys.argv[2]).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    if not in_path.exists():
        print(f"Input not found: {in_path}")
        return 1

    try:
        import pythoncom
        import win32com.client
    except ImportError:
        print("pywin32 not available. Install with: pip install pywin32")
        return 1

    pythoncom.CoInitialize()
    try:
        app = win32com.client.Dispatch("PowerPoint.Application")
        # PowerPoint requires the window to be createable; some installs need Visible=True
        try:
            app.Visible = False
        except Exception:
            pass

        prs = app.Presentations.Open(
            str(in_path),
            ReadOnly=True,
            Untitled=False,
            WithWindow=False,
        )

        # Export each slide as a PNG into the output folder.
        # Slide.Export(filename, filterName, scaleWidth, scaleHeight)
        # filterName "PNG" emits a single PNG.
        n = prs.Slides.Count
        for i in range(1, n + 1):
            slide = prs.Slides(i)
            out_path = out_dir / f"slide-{i:02d}.png"
            slide.Export(str(out_path), "PNG", 1920, 1080)
            print(f"Wrote {out_path}")

        prs.Close()
        app.Quit()
        # Give COM time to release
        time.sleep(0.3)
        return 0
    finally:
        pythoncom.CoUninitialize()


if __name__ == "__main__":
    sys.exit(main())
