import os
import pandas as pd

def engineer_features(input_path, asi_path, output_path):
    print(f"Loading the clean data from {input_path}...")
    df = pd.read_csv(input_path)
    
    print(f"Loading the macroeconomic data from {asi_path}...")
    asi_df = pd.read_csv(asi_path)

    # 1. CRITICAL FIX: Strip timezones and normalize exactly to YYYY-MM-DD
    df["Date"] = pd.to_datetime(df["Date"], utc=True).dt.tz_localize(None).dt.normalize()
    asi_df["Date"] = pd.to_datetime(asi_df["Date"], utc=True).dt.tz_localize(None).dt.normalize()

    df = df.sort_values('Date').reset_index(drop=True)
    asi_df = asi_df.sort_values('Date').reset_index(drop=True)
    
    # Calculate the Macro Daily Return for the entire market
    asi_df['ASI_Daily_Return'] = asi_df['Close'].pct_change()
    
    # Merge the macro data into the main dataframe
    print("Merging macroeconomic indicators...")
    df = pd.merge(df, asi_df[['Date', 'ASI_Daily_Return']], on='Date', how='left')

    # 2. CRITICAL FIX: Forward-fill macro data to prevent holiday gaps from ruining the dataset
    df['ASI_Daily_Return'] = df['ASI_Daily_Return'].ffill()

    print("Engineering mathematical features...")

    # Trend & Momentum Features
    df['SMA_7'] = df['Close'].rolling(window=7).mean()
    df['SMA_21'] = df['Close'].rolling(window=21).mean()
    df['Daily_Return'] = df['Close'].pct_change()

    # History Features: Lags
    df['Close_Lag_1'] = df['Close'].shift(1)
    df['Close_Lag_2'] = df['Close'].shift(2)
    df['Close_Lag_3'] = df['Close'].shift(3)

    # Target Variable
    df['Target_Next_Close'] = df['Close'].shift(-1)

    # Drop the boundary rows
    df_cleaned = df.dropna().copy()

    # Save our newly enriched dataset
    df_cleaned.to_csv(output_path, index=False)
    print(f"✅ Success! Engineered features saved to {output_path}")
    print(f"Dataset shape went from {df.shape} to {df_cleaned.shape} after dropping boundary rows")
    
    # Show the very last 3 rows to verify the dates are up to date!
    print("\nSample of your new features (last 3 rows):")
    print(df_cleaned[['Date', 'Close', 'SMA_7', 'ASI_Daily_Return', 'Target_Next_Close']].tail(3))

if __name__ == "__main__":
    CLEAN_PATH = os.path.join("data", "total_raw.csv")
    ASI_PATH = os.path.join("data", "asi_raw.csv") 
    FEATURES_PATH = os.path.join("data", "features_tte_stock.csv")

    engineer_features(CLEAN_PATH, ASI_PATH, FEATURES_PATH)
    
