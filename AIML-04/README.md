# Autonomous Driving Perception Stack

A computer vision project combining vehicle detection, multi-object tracking, and lane detection into a unified video-processing pipeline.

## Features

- **Vehicle detection:** YOLO11n detects objects in traffic videos.
- **Multi-object tracking:** ByteTrack maintains object IDs across frames.
- **Lane detection:** Ultra-Fast Lane Detection v2 identifies road-lane markings.
- **Integrated visualization:** Combines vehicle bounding boxes, tracking IDs, and lane overlays.
- **Performance profiling:** Measures inference, preprocessing, annotation, video-writing time, and effective FPS.

## Tech Stack

- Python
- PyTorch and TorchVision
- OpenCV
- Ultralytics YOLO
- ByteTrack
- Ultra-Fast Lane Detection v2

## Project Structure

```text
AIML-04/
├── artifacts/models/       # Model weights downloaded separately
├── configs/                # Detection and model configuration
├── data/samples/           # Sample road images and videos
├── docs/                   # Project documentation
├── experiments/             # Experimental implementations
├── external_models/        # External lane-detection repository, cloned separately
├── src/
│   ├── detection/           # Object detection
│   ├── lanes/               # Lane detection
│   └── tracking/            # Object tracking
├── tests/                  # Automated tests
├── tools/
│   ├── download_yolo_model.py
│   ├── integrated_perception.py
│   └── evaluate_ufld_video.py
├── pytest.ini
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## Setup

Run the following commands from the repository root:

```powershell
cd AIML-04
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

For development and testing, install the additional dependencies:

```powershell
python -m pip install -r requirements-dev.txt
```

Python 3.11 was used to validate the pinned dependencies. PyTorch installation may require a platform-specific adjustment. Choose a compatible build for your operating system and hardware if the pinned build does not support your setup.

## Obtain Model Weights

Model weights are excluded from Git to keep the repository manageable. Review the applicable license terms before using or redistributing model files.

### YOLO11n: object detection and tracking

From the `AIML-04` directory, run:

```powershell
python tools/download_yolo_model.py
```

The script downloads `yolo11n.pt` into `artifacts/models/` on the first run. It skips the download if the file already exists. An internet connection is required for the initial download.

### CULane ResNet-18: lane detection

The `culane_res18.pth` checkpoint is approximately 787 MB and is excluded from Git. Obtain a compatible checkpoint from a permitted source, review its license, and place it at:

```text
artifacts/models/culane_res18.pth
```

The external lane-detection repository is also required for the pretrained lane-detection pipeline.

## Obtain the External Lane-Detection Repository

From the `AIML-04` directory, clone the official Ultra-Fast Lane Detection v2 repository:

```powershell
git clone https://github.com/cfzd/Ultra-Fast-Lane-Detection-v2 external_models/Ultra-Fast-Lane-Detection-v2
```

Follow the external repository's setup instructions and verify that its model configuration and checkpoint are compatible with this project.

## Run the Integrated Pipeline

From the `AIML-04` directory, activate the virtual environment and run:

```powershell
python tools/integrated_perception.py
```

The script processes its configured input video and saves the annotated output under:

```text
outputs/perception/integrated_traffic.mp4
```

Check the paths in the script if your local video or model locations differ.

## Run Tests

Download the YOLO weights first, then run the automated test suite from the `AIML-04` directory:

```powershell
python -m pytest -v
```

The tests cover lane-processing functions and a ByteTrack tracking smoke test. The pretrained Ultra-Fast Lane Detection v2 pipeline also requires its external code repository and compatible lane checkpoint.

## Performance

The integrated pipeline was benchmarked in a CPU-only environment using a 1,260-frame traffic video at 1280 × 720 resolution.

| Metric | Result |
|---|---:|
| Total frames processed | 1,260 |
| Total processing time | 181.00 seconds |
| Effective processing speed | 6.96 FPS |
| Lane inference frames | 158 |
| Lane inference interval | Every 8 frames |
| YOLO detection and tracking | Every frame |

### Component Timing

| Component | Time |
|---|---:|
| YOLO detection and tracking | 81.15 seconds |
| Lane model inference | 56.47 seconds |
| Lane preprocessing | 5.62 seconds |
| Annotation and drawing | 4.19 seconds |
| Video writing | 16.23 seconds |

The lane inference interval was increased from every 5 frames to every 8 frames, reducing lane inference operations while retaining vehicle detection and tracking on every frame.

In the measured baseline, processing time decreased from 237.19 seconds to 181.00 seconds, and effective processing speed improved from 5.31 FPS to 6.96 FPS, an improvement of approximately 31.1%.

Performance varies with hardware, input video, model configuration, and software versions. The reported FPS represents processing throughput, not the output video's playback frame rate. These results are development benchmarks and do not establish real-time or safety-critical readiness.

## Limitations

- Lane predictions may be imperfect, especially around curves or unclear road markings.
- Lane inference is performed less frequently than vehicle tracking to reduce processing time.
- The current pipeline is a prototype and is not validated for real-world autonomous driving or safety-critical use.

## Future Improvements

- Improve lane continuity and handling of curved roads.
- Optimize inference latency.
- Evaluate detection and tracking accuracy using appropriate metrics.
- Improve automated test coverage.
- Compare experimental lane-smoothing approaches.

## Disclaimer

This project is intended for educational and research purposes. It must not be used as a standalone system for vehicle control or safety-critical navigation.
