# load_data.py
import os
import pandas as pd

def load_temperature_data():
    """
    Loads all CSV files in the 'temperatures' folder.
    Returns:
        seasonal_dfs: List of all dataframes for seasonal calculations
        station_dfs: List of all dataframes for station calculations
    """
    SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))
    DATA_FOLDER = os.path.join(SCRIPT_FOLDER, "temperatures")
    
    if not os.path.exists(DATA_FOLDER):
        raise FileNotFoundError(f"Folder not found: {DATA_FOLDER}")

    seasonal_dfs = []
    station_dfs = []

    for filename in os.listdir(DATA_FOLDER):
        if filename.endswith(".csv"):
            filepath = os.path.join(DATA_FOLDER, filename)
            df = pd.read_csv(filepath)
            seasonal_dfs.append(df.copy())
            station_dfs.append(df.copy())
    
    return seasonal_dfs, station_dfs
