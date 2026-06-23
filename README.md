# 📈 TotalEnergies Stock Prediction API & Quantitative Dashboard

A full-stack, production-ready MLOps ecosystem designed to predict the stock market closing prices for TotalEnergies (TTE) on the Nigerian Exchange (NGX). 

This project bridges Data Science and DevOps by automating the data pipeline, containerizing the backend model, serving it via a REST API, and providing an interactive Streamlit web dashboard. Recently upgraded to a multi-variate quantitative model, the system now factors in broader macroeconomic trends using the MSCI Nigeria ETF (`NGE`) as a market proxy to improve prediction accuracy. The entire training lifecycle is fully automated using GitHub Actions.

## 🚀 Key Features
* **Quantitative Macro-Analysis:** Integrates broader market health (NGX All-Share proxy) alongside localized stock features to anticipate market-wide ripple effects.
* **Interactive UI:** A sleek, user-friendly frontend built with Streamlit for real-time predictions.
* **High-Performance Backend:** A fast, asynchronous REST API built with FastAPI and Uvicorn to serve the Random Forest model.
* **Multi-Container Orchestration:** The backend API and frontend UI are fully containerized and securely linked over an internal network using Docker Compose.
* **Automated Data Pipeline:** Fetches, cleans, and engineers financial features (Moving Averages, Lagging Close Prices, and Market Daily Returns) from raw historical market data.
* **MLOps / Continuous Training (CT):** A GitHub Actions pipeline configured to automatically wake up every Friday at midnight, fetch the latest market data, retrain the model, and commit the updated weights back to the repository.

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **Data Processing & ML:** Pandas, Scikit-Learn, yfinance
* **Backend Framework:** FastAPI, Uvicorn
* **Frontend UI:** Streamlit
* **DevOps & CI/CD:** Docker, Docker Compose, GitHub Actions

## 📂 Project Structure
```text
stock_prediction_api/
├── .github/workflows/
│   ├── ci.yml               # Automated Docker build testing
│   └── retrain.yml          # Weekly automated model retraining pipeline
├── app/
│   ├── main.py              # FastAPI backend application
│   └── stock_model.pkl      # Trained Multi-Variate Random Forest model
├── data/                    # Raw and cleaned dataset storage
├── frontend.py              # Streamlit interactive web dashboard
├── engineer_features.py     # Feature engineering & proxy merging script
├── fetch_data.py            # Financial data extraction script (TTE & NGE)
├── train_model.py           # Model training script
├── Dockerfile               # Blueprint for the FastAPI backend image
├── Dockerfile.frontend      # Blueprint for the Streamlit UI image
├── docker-compose.yml       # Multi-container orchestration configuration
└── requirements.txt         # Python package dependencies
```

## 💻 How to Run the Application Locally

The entire full-stack application is managed via Docker Compose, allowing you to spin up the integrated ecosystem with a single command. Ensure the Docker engine is installed and running on your system.

**1. Build and Launch the Multi-Container Architecture:**

```bash
docker-compose up -d --build

```

*(Docker will automatically build the backend and frontend images, construct the internal network, and start both containers in the background).*

**2. Access the Interactive Dashboard:**
Open your web browser and navigate to:

```text
http://localhost:8501

```

**3. Access the API Documentation:**
To view the raw backend architecture or interact directly with the Swagger UI, navigate to:

```text
http://localhost:8000/docs

```

**4. Shutting Down:**
To stop the application and safely spin down the containers, run:

```bash
docker-compose down

```

## 📡 API Endpoints (Backend)

If you prefer to bypass the Streamlit UI, you can send requests directly to the containerized FastAPI backend.

### `POST /predict`

Accepts a JSON payload containing the engineered financial features (including the new macroeconomic proxy) and returns the predicted closing price.

**Example Request Payload:**

```json
{
  "SMA_7": 62.50,
  "SMA_21": 61.10,
  "Daily_Return": 0.015,
  "Close_Lag_1": 63.00,
  "Close_Lag_2": 62.00,
  "Close_Lag_3": 62.10,
  "ASI_Daily_Return": 0.0097
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