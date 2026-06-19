from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

app = FastAPI(
    title="Stock Price Prediction API",
    description="A machine learning API that predicts the next day's closing price" ,
    version="1.0.0",
)

# i am going to use os.path to ensure it finds the file no matter where you run the script from

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "stock_model.pkl")

#load into the memory when the server starts
model =joblib.load(MODEL_PATH)

# Pydantic Schema for the incoming data
class StockFeatures(BaseModel):
    SMA_7: float
    SMA_21: float
    Daily_Return: float
    Close_Lag_1: float
    Close_Lag_2: float
    Close_Lag_3: float

#prediction endpoint
@app.post("/predict")
def predict_stock_price(features: StockFeatures):
    #converted the incoming JSON payload into a pandas DataFrame
    # the model expects a 2D array/dataframe just like it was trained on
    input_data =pd.DataFrame([features.model_dump()])

    #Generate the prediction
    prediction = model.predict(input_data)
    # Return the predicted price rounded to 2 decimal places
    return {
        "status": "success",
        "prediction_next_close_price": round(prediction[0], 2),
    }