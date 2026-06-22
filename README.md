Here is your updated, professional `README.md`. It now perfectly reflects the complete MLOps architecture you built, including the new Streamlit frontend UI and your automated GitHub Actions pipelines.

You can copy this entire block and paste it right over the old text in your `README.md` file.

```markdown
# 📈 TotalEnergies Stock Prediction API & Dashboard

A full-stack, production-ready Machine Learning ecosystem designed to predict the stock market closing prices for TotalEnergies on the Nigerian Exchange (NGX). 

This project bridges Data Science and MLOps by automating the data pipeline, containerizing the backend model, serving it via a REST API, and providing an interactive web dashboard for real-time predictions. The entire training lifecycle is fully automated using GitHub Actions.

## 🚀 Key Features
* **Interactive UI:** A sleek, user-friendly frontend built with Streamlit for instant stock predictions.
* **High-Performance Backend:** A fast, asynchronous REST API built with FastAPI and Uvicorn to serve the Machine Learning model.
* **Automated Data Pipeline:** Fetches, cleans, and engineers financial features (SMA_7, SMA_21, Lagging Close Prices) from raw historical market data.
* **MLOps / Continuous Training (CT):** A GitHub Actions pipeline configured to automatically wake up every Friday at midnight, fetch the latest NGX market data, retrain the Scikit-Learn Random Forest model, and commit the updated weights back to the repository.
* **Continuous Integration (CI):** Automated Docker build testing on every push to the `main` branch.
* **Containerized Infrastructure:** The backend API and model are fully containerized using Docker, ensuring exact environment replication.

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **Data Processing & ML:** Pandas, Scikit-Learn
* **Backend Framework:** FastAPI, Uvicorn
* **Frontend UI:** Streamlit
* **DevOps & CI/CD:** Docker, GitHub Actions

## 📂 Project Structure
```text
stock_prediction_api/
├── .github/workflows/
│   ├── ci.yml               # Automated Docker build testing
│   └── retrain.yml          # Weekly automated model retraining pipeline
├── app/
│   ├── main.py              # FastAPI backend application
│   └── stock_model.pkl      # Trained Scikit-Learn Random Forest model
├── data/                    # Raw and cleaned dataset storage
├── frontend.py              # Streamlit interactive web dashboard
├── clean_data.py            # Data cleaning script
├── engineer_features.py     # Feature engineering script
├── fetch_data.py            # Financial data extraction script
├── train_model.py           # Model training script
├── Dockerfile               # Docker image configuration for the backend
└── requirements.txt         # Python package dependencies

```

## 💻 How to Run the Application

This ecosystem is split into two parts: the containerized backend (FastAPI) and the local frontend dashboard (Streamlit).

### 1. Start the Backend API (Docker)

Ensure the Docker engine is installed and running on your system.

**Build the Docker Image:**

```bash
docker build -t stock-predictor-api .

```

**Run the Backend Container:**

```bash
docker run -d -p 8000:8000 --name my-stock-api stock-predictor-api

```

*(The backend API is now actively listening for requests on `http://localhost:8000/docs`)*

### 2. Launch the Frontend Dashboard (Streamlit)

With the backend running, open a new terminal window to start the user interface.

**Install UI Dependencies (if not already installed):**

```bash
pip install streamlit requests

```

**Run the Streamlit App:**

```bash
streamlit run frontend.py

```

*(Your default web browser will automatically open the interactive dashboard)*

## 📡 API Endpoints

If you prefer to bypass the Streamlit UI, you can send requests directly to the backend API.

### `POST /predict`

Accepts a JSON payload containing the engineered financial features and returns the predicted closing price.

**Example Request Payload:**

```json
{
  "SMA_7": 62.50,
  "SMA_21": 61.10,
  "Daily_Return": 0.015,
  "Close_Lag_1": 63.00,
  "Close_Lag_2": 62.00,
  "Close_Lag_3": 62.10
}

```

**Example Response:**

```json
{
  "status": "success",
  "prediction_next_close_price": 63.13
}

```

```

```