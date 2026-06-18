# Part 4 - FastAPI Churn Scoring Service

## Overview

This API provides churn-risk predictions for customer retention teams.

## Installation

```bash
pip install -r requirements.txt
```

## Run API

```bash
uvicorn app.main:app --reload
```

## Endpoints

### GET /health

Returns API health status.

### POST /predict

Returns churn prediction for one customer.

### POST /batch_predict

Returns predictions for multiple customers.

## Example Response

```json
{
  "churn_probability": 0.72,
  "predicted_class": 1,
  "risk_level": "high"
}
```

## Testing

```bash
pytest
```

## Model Source

The API uses the churn model developed in Part 3.
