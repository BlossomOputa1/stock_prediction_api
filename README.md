# 📈 TotalEnergies Stock Prediction API & Quantitative Dashboard

A full-stack, production-ready MLOps ecosystem designed to predict the stock market closing prices for TotalEnergies (TTE) on the VanEck Africa Index ETF. 

This project bridges Data Science and DevOps by automating the data pipeline, containerizing the backend model, serving it via a REST API, and providing an interactive Streamlit web dashboard. Recently upgraded to a multi-variate quantitative model, the system now factors in broader macroeconomic trends using the MSCI Nigeria ETF (`NGE`) as a market proxy to improve prediction accuracy. The entire training lifecycle is fully automated using GitHub Actions.

# 📈 Automated Stock Prediction API

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF.svg)

An end-to-end, automated machine learning REST API that serves stock price predictions. This project bridges the gap between data science and robust backend infrastructure by wrapping a predictive machine learning model in a production-ready, containerized environment with continuous training pipelines.

## 🚀 Features

*   **Lightning-Fast Serving:** Built with FastAPI for high-performance, asynchronous endpoint handling.
*   **Isolated Environment:** Fully containerized using Docker, ensuring consistent behavior across local development and production.
*   **Continuous Training (CT):** Integrated GitHub Actions workflows that automatically retrain the model with the latest market data without manual intervention.
*   **Scalable Architecture:** Designed with DevOps best practices, making it easy to deploy to any cloud provider.

## 🛠️ Tech Stack

*   **Backend:** Python, FastAPI, Uvicorn
*   **Machine Learning:** scikit-learn 
*   **Infrastructure & DevOps:** Docker, GitHub Actions
*   **Data Processing:** Pandas, NumPy

## ⚙️ Local Setup & Installation

### Prerequisites
*   [Docker](https://docs.docker.com/get-docker/) installed on your machine.
*   Git installed.

### Run via Docker

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/blossomoputa/stock-prediction-api.git](https://github.com/blossomoputa/stock-prediction-api.git)
   cd stock-prediction-api
   ```

2. **Build the Docker image:**
   ```bash
   docker build -t stock-prediction-api .
   ```

3. **Run the container:**
   ```bash
   docker run -d -p 8000:8000 stock-prediction-api
   ```

4. **Access the API:**
   *   Open your browser and navigate to `http://localhost:8000`
   *   Interactive API documentation (Swagger UI) is available at `http://localhost:8000/docs`

## 📡 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Health check and API status. |
| `POST` | `/predict` | Submit a ticker symbol and receive the forecasted stock price. |
| `GET` | `/model-info` | Returns the current model version and last training timestamp. |

## 🔄 CI/CD & Continuous Training

This repository utilizes **GitHub Actions** to automate the machine learning lifecycle:
1. **Integration:** On every push to the `main` branch, the workflow runs automated unit tests and lints the Python code.
2. **Continuous Training:** A scheduled cron job triggers a pipeline to fetch new historical stock data, retrain the **Scikit-Learn** model, and save the updated weights.
3. **Delivery:** The updated model and application are rebuilt into a fresh Docker image, ready for deployment.

## 👤 Author

**Blossom Oputa**
*   LinkedIn: https://linkedin.com/in/chidera-oputa
*   GitHub: [@BlossomOputa1](https://github.com/BlossomOputa1)
*   Personal website : https://blossoms-portfolio.netlify.app
