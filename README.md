# Subham Dey | Nexvia Technologies Capstone Projects

This repository contains two capstone projects prepared for evaluation by Nexvia Technologies.

## Projects

### AIML-03: Large-Scale Personalized Recommendation Engine

A personalized movie recommendation system built with TensorFlow/Keras, FAISS, and FastAPI using MovieLens 25M-derived artifacts.

- **Project directory:** `AIML-03/`
- **Setup and run guide:** [AIML-03 README](AIML-03/README.md)

### AIML-04: Autonomous Driving Perception Stack

A computer vision pipeline combining object detection, multi-object tracking, and lane detection.

- **Project directory:** `AIML-04/`
- **Setup and run guide:** [AIML-04 README](AIML-04/README.md)

## Start Here

1. Open the README for the project you want to evaluate.
2. Follow its setup instructions and run commands in order.
3. Check its model-weight section before running inference. Some model files are intentionally downloaded separately because of their size or licensing terms.
4. Follow its test instructions to run the available automated checks.

**Important:** Commands and relative paths in each project-specific README assume that you first change into that project's directory (`AIML-03/` or `AIML-04/`) unless a command explicitly says otherwise.

## Repository Structure

```text
Subham_Dey_Capstone_Projects/
├── README.md
├── AIML-03/
│   ├── README.md
│   ├── requirements.txt
│   ├── src/
│   ├── artifacts/
│   ├── data/
│   └── ...
└── AIML-04/
    ├── README.md
    ├── requirements.txt
    ├── requirements-dev.txt
    ├── src/
    ├── tests/
    └── ...
```

The project-specific READMEs document setup, runtime requirements, model artifacts, usage, and known limitations. Do not commit virtual environments, caches, credentials, or unrelated local files.
