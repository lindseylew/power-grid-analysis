import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS grid_data (
        id SERIAL PRIMARY KEY,
        period TIMESTAMP NOT NULL,
        voltage_kv NUMERIC NOT NULL,
        current_a NUMERIC NOT NULL,
        frequency_hz NUMERIC NOT NULL,
        load_mw NUMERIC NOT NULL
    );
""")

conn.commit()
cur.close()
conn.close()

print("Table created successfully")