# Banknote Authentication Prediction API

A Machine Learning-powered REST API built using FastAPI to predict whether a banknote is authentic or forged based on its physical characteristics.

---

## Project Overview

This project demonstrates the complete Machine Learning workflow from data preprocessing to model deployment.

The API accepts banknote features as input, validates the request using Pydantic, loads a trained Random Forest model, and returns the prediction through a FastAPI endpoint.

---

## Features

- Data preprocessing
- Train/Test Split
- Random Forest Classification
- Model Evaluation
- Model Serialization using Pickle
- REST API using FastAPI
- Request Validation using Pydantic
- Dependency Management using uv

---

## Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Framework | FastAPI |
| ML Library | Scikit-learn |
| Validation | Pydantic |
| Model Serialization | Pickle |
| Dependency Manager | uv |
| Testing | Postman |

---

## Machine Learning Workflow

1. Load Dataset
2. Data Exploration
3. Train-Test Split
4. Train Random Forest Classifier
5. Evaluate Accuracy
6. Save Model using Pickle
7. Build FastAPI Backend
8. Validate Input using Pydantic
9. Predict using Trained Model
10. Test API using Postman

---

## API Endpoint

POST /predict

### Sample Request

```json
{
    "variance": 3.62,
    "skewness": 8.66,
    "curtosis": -2.80,
    "entropy": -0.44
}
```

### Sample Response

```json
{
    "prediction": "Authentic note"
}
```

|Version	|Date	|Changes
|-----------|-------|----------------------------------------------
|v1.0.0	|25-Jun-2026	|1. Initial ML model training using Random Forest. 2.Saved trained model using Pickle. 3.Managed project dependencies using uv                 
|v1.1.0	|26-Jun-2026	|1. Built FastAPI prediction endpoint,2. Added Pydantic request validation,3. Tested API using Postman
---


## Run Locally

Clone the repository

```bash
git clone <repository-url>
```

Create environment

```bash
uv venv
```

Install dependencies

```bash
uv sync
```

Run the application

```bash
uv run uvicorn app:app --reload
```


## Future Improvements

- Docker Support
- Model Versioning
- CI/CD Pipeline
- Cloud Deployment
- Logging
- Unit Testing
- Authentication
- Database Integration

---

## Author

Anubama T




