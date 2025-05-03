# Grid Monitoring and Anomaly Detection with Machine Learning

## Overview

This project focuses on monitoring power grid telemetry data, detecting anomalies in the grid's behavior using machine learning, and visualizing the results. The data includes voltage, current, and frequency, and the system is designed to identify abnormal behaviors that could indicate faults, overloading, or potential system failures.

The project uses:
- **Python** for data generation and anomaly detection
- **PostgreSQL** for data storage
- **Power BI** for data visualization
- **Docker** for containerization

---

## Table of Contents

- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Running the ML Model](#running-the-ml-model)
- [Docker Setup](#docker-setup)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Project Description

This project involves:

1. **Data Generation**: Creating mock telemetry data (voltage, current, frequency) for simulation.
2. **Data Processing**: Loading the data into a PostgreSQL database for efficient querying and analysis.
3. **Anomaly Detection**: Using machine learning models (e.g., Isolation Forest or Autoencoders) to identify anomalies.
4. **Visualization**: Analyzing and visualizing the data in Power BI.
5. **Dockerization**: Containerizing the application to ensure consistent deployment across environments.

---

## Technologies Used

- Python
- pandas
- scikit-learn
- PostgreSQL
- Power BI
- Docker
- Matplotlib (optional)
- Jupyter Notebooks

---

## Installation

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) (optional but recommended)
- Python 3.x

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/grid-monitoring-anomaly-detection.git
    cd grid-monitoring-anomaly-detection
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. If not using Docker, ensure PostgreSQL is installed and a database is set up manually.

---

## Usage

1. **Generate mock telemetry data**:

    ```bash
    python scripts/generate_data.py
    ```

    This will generate a `mock_telemetry.csv` file in the `data/raw` directory.

2. **Load data into PostgreSQL**:

    ```bash
    python scripts/load_data_to_db.py
    ```

3. **Run anomaly detection**:

    ```bash
    python scripts/run_anomaly_detection.py
    ```

    This trains a model and stores anomaly results in `data/results/anomalies.csv` and/or in the PostgreSQL database.

4. **Visualize the data**:

    - Use **Power BI** to connect to the PostgreSQL database and explore time-series anomalies.
    - Alternatively, view example plots in the `notebooks/` directory using **Matplotlib**.

---

## Running the ML Model

Example usage with Isolation Forest:

```python
from sklearn.ensemble import IsolationForest
import pandas as pd

# Load telemetry data
df = pd.read_csv('data/raw/mock_telemetry.csv')

# Select features
features = df[['voltage_kV', 'current_A', 'frequency_Hz']]

# Train model
model = IsolationForest(n_estimators=100, contamination=0.05)
df['anomaly'] = model.fit_predict(features)

# Save results
df.to_csv('data/results/anomalies.csv', index=False)
