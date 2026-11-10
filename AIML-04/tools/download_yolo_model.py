"""Download the YOLO11n weights required by AIML-04."""

import os
from pathlib import Path

from ultralytics import YOLO

ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = ROOT / "artifacts" / "models"
MODEL_PATH = MODEL_DIR / "yolo11n.pt"


def main() -> None:
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    if MODEL_PATH.is_file():
        print(f"YOLO weights already exist: {MODEL_PATH}")
        return

    original_directory = Path.cwd()

    try:
        os.chdir(MODEL_DIR)
        print("Downloading YOLO11n weights using Ultralytics...")
        YOLO("yolo11n.pt")

        if not MODEL_PATH.is_file():
            raise RuntimeError(
                "Model download did not create artifacts/models/yolo11n.pt. "
                "Check your internet connection and retry."
            )
    finally:
        os.chdir(original_directory)

    print(f"YOLO weights are ready: {MODEL_PATH}")


if __name__ == "__main__":
    main()
