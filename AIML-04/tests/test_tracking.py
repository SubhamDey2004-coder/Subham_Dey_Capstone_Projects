from pathlib import Path

from ultralytics import YOLO


def test_bytetrack_assigns_stable_ids_on_sample_image():
    root = Path(__file__).resolve().parents[1]

    model_path = root / "artifacts" / "models" / "yolo11n.pt"
    image_path = root / "data" / "samples" / "test_road.png"

    assert model_path.exists(), "YOLO model weights are missing"
    assert image_path.exists(), "Sample road image is missing"

    model = YOLO(str(model_path))
    previous_ids = None

    for _ in range(5):
        result = model.track(
            source=str(image_path),
            persist=True,
            tracker="bytetrack.yaml",
            conf=0.25,
            device="cpu",
            verbose=False,
        )[0]

        boxes = result.boxes
        assert boxes is not None and len(boxes) > 0, (
            "No objects detected in the sample image"
        )
        assert boxes.id is not None, (
            "ByteTrack did not assign tracking IDs"
        )

        current_ids = {int(track_id) for track_id in boxes.id.tolist()}

        if previous_ids is not None:
            assert current_ids == previous_ids, (
                "Tracking IDs changed for the same unchanged image"
            )

        previous_ids = current_ids
