import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# Read the CSV
df = pd.read_csv('eia_telemetry_dataset.csv')

# Convert 'period' column to datetime (in case it's read as a string)
df['period'] = pd.to_datetime(df['period'])

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    pasword=os.getenv("POSTGRES_PASSWORD")
)

cur = conn.cursor()

# Read processed telemetry data
csv_path = os.path.join(os.path.dirname(__file__), "processed_data", "telemetry_data.csv")
data_to_insert = pd.read_csv(csv_path)

# Insert each row into the table
for _, row in data_to_insert.iterrows():
    cur.execute("""
        INSERT INTO grid_data (period, region, voltage_kv, current_a, frequency_hz, load_mw)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            row["timestamp"],
            row["region"],
            row["voltage_kv"],
            row["current_a"],
            row["frequency_hz"],
            row["demand_mw"]
        ))

# Commit and close the connection
conn.commit()
cur.close()
conn.close()

print("Telemetry data loaded successfully.")