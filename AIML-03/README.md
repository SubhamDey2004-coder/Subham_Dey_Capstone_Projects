# Large-Scale Personalized Recommendation Engine

A two-stage personalized movie recommendation system built with **TensorFlow, Keras, FAISS, and FastAPI**, using the MovieLens 25M dataset.

The system retrieves candidate movies using learned user and movie embeddings, filters out movies a user has already watched, and reranks the remaining candidates with a neural ranking model.

## Features

- **Large-scale recommendation:** Developed using the MovieLens 25M dataset.
- **User and movie embeddings:** Learns 32-dimensional representations for retrieval.
- **Candidate retrieval:** Uses FAISS for efficient nearest-neighbor search.
- **Neural ranking:** Reranks candidate movies using user embeddings, movie embeddings, and genre features.
- **Seen-item filtering:** Excludes movies already present in a user's recorded viewing history.
- **REST API:** Serves personalized recommendations through FastAPI.
- **Offline evaluation:** Compares retrieval-only recommendations against embedding-based reranking.
- **Input validation:** Enforces valid recommendation limits and handles unknown users.

## System Architecture

```text
MovieLens 25M Dataset
        |
        v
Data Preparation and Time-Based Splitting
        |
        v
User and Movie Embedding Training
        |
        v
FAISS Candidate Retrieval
        |
        v
Seen-Movie Filtering
        |
        v
Neural Embedding-Based Ranking
        |
        v
Top-K Personalized Recommendations
        |
        v
FastAPI REST API
```

## Evaluation Results

The following recommendation metrics were measured on a fixed validation sample of 500 users.

| Metric | Result |
|---|---:|
| Retrieval-only Recall@10 | 0.0169 |
| Retrieval + embedding ranker Recall@10 | 0.0431 |
| Absolute Recall@10 improvement | +0.0262 |
| Relative improvement over retrieval-only | Approximately 155% |
| Recall@10 improvement multiplier | Approximately 2.55× |

The embedding-based ranking stage improved Recall@10 from 0.0169 to 0.0431 on this evaluation sample.

The ranking model also achieved the following results on a separate classification validation split:

| Classification metric | Result |
|---|---:|
| ROC-AUC | 0.7884 |
| Accuracy | 0.7146 |

**Evaluation note:** Recommendation Recall@10 and classification metrics measure different objectives and should not be compared directly. The recommendation results are based on a fixed sample of 500 users and do not establish performance across all users or on the held-out test set. Broader evaluation is still required.

## Technology Stack

- **Language:** Python 3.11
- **Machine learning:** TensorFlow, Keras, TensorFlow Recommenders
- **Candidate retrieval:** FAISS
- **Data processing:** Pandas, NumPy, PyArrow, Parquet
- **API framework:** FastAPI
- **ASGI server:** Uvicorn
- **Model artifacts:** Keras models, NumPy arrays, FAISS index

## Project Structure

```text
AIML-03/
├── src/
│   ├── data/
│   ├── features/
│   ├── retrieval/
│   ├── ranking/
│   ├── evaluation/
│   └── serving/
│       ├── api.py
│       └── recommend_embeddings.py
├── artifacts/
│   └── models/
│       ├── user_embedding.keras
│       ├── movie_embedding.keras
│       ├── ranking_model_embeddings.keras
│       ├── user_ids.npy
│       ├── movie_ids.npy
│       └── movies.faiss
├── data/
│   └── processed/
│       ├── movie_features.parquet
│       └── user_history.parquet
├── requirements.txt
└── README.md
```

This tree highlights the important runtime files. Additional source files and subdirectories may also be present.

## Requirements

- Python 3.11
- Sufficient disk space for the Python environment and model dependencies
- The trained model files and processed data included in this repository

This delivery is intended to run the existing recommendation API. **Downloading the MovieLens dataset and retraining the models are not required for normal API execution.**

Keep the directory structure and filenames unchanged because the serving code loads models and data using paths relative to this project directory.

## Setup

**Run the following commands from the repository root, then continue running the commands in this README from inside `AIML-03/`.**

### 1. Enter the project directory

```powershell
cd AIML-03
```

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, consult the Python documentation for Windows virtual environments or use the environment's Python executable directly.

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Installation time and disk usage depend on the machine and available package wheels.

## Run the API

From inside the `AIML-03/` directory, start the FastAPI server:

```powershell
python -m uvicorn src.serving.api:app --host 127.0.0.1 --port 8000
```

If port `8000` is already occupied, stop the other service using it or select another available port, such as `8001`.

### Verify the service

Health endpoint:

```text
http://127.0.0.1:8000/health
```

Expected response:

```json
{
  "status": "healthy"
}
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

Root endpoint:

```text
http://127.0.0.1:8000/
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns the API status message |
| GET | `/health` | Checks whether the API is responding |
| GET | `/recommend/{user_id}?top_k=10` | Returns personalized movie recommendations |

### Example request

Using PowerShell while the API is running:

```powershell
Invoke-RestMethod "http://127.0.0.1:8000/recommend/1?top_k=10"
```

Example response structure:

```json
{
  "user_id": 1,
  "count": 10,
  "recommendations": [
    {
      "movieId": 26587,
      "title": "Example Movie",
      "score": 0.84
    }
  ]
}
```

The movie title and score above are illustrative. Actual recommendations depend on the trained models and user history.

### Request validation and errors

- `top_k` must be between **1 and 50**, inclusive.
- An unknown user returns HTTP `404`.
- An invalid `top_k` value returns HTTP `422`.
- The response contains the user ID, recommendation count, and a list of movie IDs, titles, and ranking scores.

## Current Project Status

The retrieval, ranking, evaluation, and API-serving components have been implemented. Local validation included API startup, health checks, recommendation generation, unknown-user handling, and invalid-parameter validation. A fresh-clone setup and API smoke test also succeeded with the included model artifacts and processed data.

Further improvements could include broader held-out test evaluation, automated test coverage, reproducibility checks, and additional production-readiness work.

## Limitations and Future Improvements

- **Cold-start users:** Users absent from the trained user vocabulary are not currently supported by the embedding-based recommendation endpoint.
- **Recommendation quality:** Results depend on the trained embeddings, indexed movies, and available user history.
- **Evaluation coverage:** Broader evaluation is required before making general performance or production-scale claims.
- **Production extensions:** Redis caching, scheduled retraining, and cold-start fallbacks are potential future improvements, not currently implemented features.

## Dataset and Licensing

The project uses the MovieLens 25M dataset for recommendation-system development and evaluation.

Before redistributing the dataset or publishing the repository, review the applicable MovieLens dataset terms and the licenses of the software dependencies. Do not assume that distributing the project automatically grants permission to redistribute third-party datasets.
