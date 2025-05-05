import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv('../data/raw/mock_telemetry.csv')

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

cur = conn.cursor()

for _ , row in df.iterrows():
    cur.execute("""
        INSERT INTO grid_data (period, region, voltage_kv, current_a, frequency_hz, load_mw)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        row['period'],
        row['voltage_kV'],
        row['current_A'],
        row['frequency_Hz'],
        row['load_mw']
    ))

conn.commit()
cur.close()
conn.close()

print("Mock data loaded successfully.")