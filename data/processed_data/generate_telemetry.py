import pandas as pd
import numpy as np
import os

#Load EIA data
data_path = os.path.join(os.path.dirname(__file__), '..', 'raw', 'eia_data.csv')
df = pd.read_csv(data_path, header=None)

# Manually set column names based on the CSV structure
df.columns = ["period", "respondent", "respondent-name", "type", "type-name", "value", "value-units"]

# Clean column names
df.columns = df.columns.str.strip()

# Filter only actual demand rows
df = df[df["type"] == "D"].copy()

# Rename columns for clarity
df.rename(columns={"period": "timestamp", "value": "demand_mw"}, inplace=True)

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Generate random voltage, current, and frequency
np.random.seed(42)

# Simulate values
df['voltage_kv'] = np.random.normal(loc=120, scale=2, size=len(df)).round(2)
df["current_a"] = (df["demand_mw"] * 8.3).round(2) #scale factor to simulate amps
df["frequency_hz"] = np.random.normal(loc=60, scale=0.05, size=len(df)).round(3)

# Select final telemetry columns
telemetry_df = df[["timestamp", "respondent", "voltage_kv", "current_a", "frequency_hz", "demand_mw"]]
telemetry_df.rename(columns={"respondent": "region"})

# Save telemetry data
output_path = os.path.join(os.path.dirname(__file__), 'telemetry_data.csv')
telemetry_df.to_csv(output_path, index=False)

print(f"Telemetry data generated and saved to {output_path}")