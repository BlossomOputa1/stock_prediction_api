# 📈 Stock Market Prediction API

A production-ready, containerized Machine Learning API designed to predict stock market closing prices. Built with Python and FastAPI, this backend serves a Random Forest predictive model trained on historical market data. 

This project bridges the gap between Data Science and DevOps by automating the data pipeline, engineering financial features, and packaging the entire ecosystem into an isolated Docker container for seamless, reproducible deployment.

## 🚀 Features
* **Automated Data Pipeline:** Fetches, cleans, and processes raw historical financial data.
* **Feature Engineering:** Calculates key market indicators including Simple Moving Averages (SMA_7, SMA_21) and Lagging Close Prices.
* **Machine Learning:** Utilizes a Scikit-Learn Random Forest model to predict next-day closing prices based on engineered time-series features.
* **High-Performance API:** Serves predictions via a fast, asynchronous REST endpoint using FastAPI and Uvicorn.
* **Containerized Infrastructure:** Fully containerized using Docker, ensuring exact environment replication and eliminating dependency mismatches.

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **Data Processing & ML:** Pandas, Scikit-Learn
* **Backend Framework:** FastAPI, Uvicorn
* **DevOps / Deployment:** Docker

## 📂 Project Structure
```text
stock_prediction_api/
├── app/
│   ├── main.py              # FastAPI application and routing
│   └── stock_model.pkl      # Trained Scikit-Learn Random Forest model
├── data/                    # Raw and cleaned dataset storage
├── notebooks/               # Jupyter notebooks for EDA and prototyping
├── clean_data.py            # Data cleaning script
├── engineer_features.py     # Feature engineering script
├── fetch_data.py            # Financial data extraction script
├── train_model.py           # Model training and export script
├── Dockerfile               # Docker image configuration
└── requirements.txt         # Python package dependencies 


```

## 🐳 Running with Docker (Recommended)

The easiest way to run this application is via Docker. Ensure the Docker engine is installed and running on your system.

**1. Build the Docker Image**

```bash
docker build -t stock-predictor-api .

```

**2. Run the Container**

```bash
docker run -d -p 8000:8000 --name my-stock-api stock-predictor-api

```

**3. Access the API**
Navigate to `http://localhost:8000/docs` in your web browser to access the interactive Swagger UI and test the `/predict` endpoint.

## 💻 Running Locally (Without Docker)

If you prefer to run the application directly on your local Ubuntu environment:

**1. Create and activate a virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate

```

**2. Install dependencies:**

```bash
pip install -r requirements.txt

```

**3. Start the Uvicorn server:**

```bash
uvicorn app.main:app --reload

```

## 📡 API Endpoints

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