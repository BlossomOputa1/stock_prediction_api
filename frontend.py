import streamlit as st
import requests

# Set up the page title and description
st.title("📈 TotalEnergies Stock Predictor")
st.write("Enter the latest NGX market indicators below to predict the next closing price.")

# Create a clean layout with columns
col1, col2 = st.columns(2)

with col1:
    sma_7 = st.number_input("7-Day Moving Average (SMA_7)", value=62.50)
    sma_21 = st.number_input("21-Day Moving Average (SMA_21)", value=61.10)
    daily_return = st.number_input("Daily Return", value=0.015, format="%.4f")

with col2:
    lag_1 = st.number_input("Close Price - 1 Day Ago", value=63.00)
    lag_2 = st.number_input("Close Price - 2 Days Ago", value=62.00)
    lag_3 = st.number_input("Close Price - 3 Days Ago", value=62.10)

# The prediction button
if st.button("Predict Next Close Price", type="primary"):

    # 1. Package the inputs into a dictionary
    payload = {
        "SMA_7": sma_7,
        "SMA_21": sma_21,
        "Daily_Return": daily_return,
        "Close_Lag_1": lag_1,
        "Close_Lag_2": lag_2,
        "Close_Lag_3": lag_3
    }

    # 2. Send the data to your running FastAPI Docker container
    api_url = "http://api:8000/predict"

    try:
        response = requests.post(api_url, json=payload)

        # 3. Display the result
        if response.status_code == 200:
            prediction = response.json()["prediction_next_close_price"]
            st.success(f"### Predicted Close Price: ₦{prediction:.2f}")
            st.balloons()  # Adds a fun animation on success!
        else:
            st.error(f"API Error: {response.text}")

    except requests.exceptions.ConnectionError:
        st.error("🚨 Could not connect to the API. Is your Docker container running?")