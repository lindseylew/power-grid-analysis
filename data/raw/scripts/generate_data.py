import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Function to generate random data
def generate_mock_data(num_rows):
    # Generate timestamps, starting from current time and spaced by 1 minute
    start_time = datetime.now()
    timestamps = [start_time + timedelta(minutes=i) for i in range(num_rows)]

    # Simulate voltage, current, and frequency with some realistic values
    regions = ['South Florida', 'North Florida', 'Central Florida', 'Panhandle', 'East Coast', 'West Coast']
    voltage = np.random.uniform(110, 130, num_rows) # Voltange between 110V and 130V
    currents = np.random.uniform(50, 200, num_rows) # Current between 50A and 200A
    frequencies = np.random.uniform(59.5, 60.5, num_rows) # Frequency between 59.5Hz and 60.5Hz
    load_mw = np.random.uniform(100, 2000, num_rows) # Load between 100MW and 2000MW

    # Create a DataFrame
    data = {
        'timestamp': timestamps,
        'region': [random.choice(regions) for _ in range(num_rows)],
        'voltage_kV': voltage,
        'current_A': currents,
        'frequency_Hz': frequencies,
        'load_mw': load_mw
    }

    df = pd.DataFrame(data, columns=['timestamp', 'region', 'voltage_kV', 'current_A', 'frequency_Hz', 'load_mw'])

    # Save to CSV
    df.to_csv('mock_telemetry.csv', index=False)

    return df

df_mock_data = generate_mock_data(1000)
print(df_mock_data.head()) # Display the first few rows of the generated data
