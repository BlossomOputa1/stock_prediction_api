import joblib
import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


def train_predictive_model(data_path, model_path):
    print(f"Loading engineering features from {data_path}...")
    df = pd.read_csv(data_path)

    #Define Features (X) and Target(Y)
    features = ['SMA_7', 'SMA_21', 'Daily_Return', 'Close_Lag_1', 'Close_Lag_2', 'Close_Lag_3']
    X = df[features]
    y = df['Target_Next_Close']

    # Chronological Split (80% Train, 20% test)
    # We cannot shuffle time-series data, so we slice it sequentially
    split_index = int(len(df) * 0.8)
    X_train, X_test = X[:split_index], X[split_index:]
    y_train, y_test = y[:split_index], y[split_index:]

    print(f"Training model on {len(X_train)} historical days...")
    print(f"Training model on {len(X_test)} future days...")

    # A random forest builds 100 decision trees and averages their predictions
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    #evaluate the model
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)

    print("\n ------- Model Evaluation --------")
    print(f"MAE: {mae:.2f}")
    print("This means on average, our predicted stock price is off by this many units")

    #save the trained model for the backend
    joblib.dump(model, model_path)
    print(f"\n Successful! Model saved to {model_path}. it is now ready for the API ")

if __name__ == "__main__":
    DATA_PATH = os.path.join("data", "features_tte_stock.csv")

    #made sure the 'app' directory exists so that the model can be saved in there for FastAPI
    os.makedirs("app", exist_ok=True)
    MODEL_PATH = os.path.join("app", "stock_model.pkl")

    train_predictive_model(DATA_PATH, MODEL_PATH)