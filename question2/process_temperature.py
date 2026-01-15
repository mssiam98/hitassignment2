# process_temperature.py
import os
import pandas as pd
import numpy as np

SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))

# Seasons mapping
SEASONS = {
    "Summer": ["December", "January", "February"],
    "Autumn": ["March", "April", "May"],
    "Winter": ["June", "July", "August"],
    "Spring": ["September", "October", "November"]
}

def calculate_seasonal_average(seasonal_dfs):
    seasonal_avg = {}
    for season, months in SEASONS.items():
        temps = []
        for df in seasonal_dfs:
            for month in months:
                if month in df.columns:
                    temps.extend(df[month].dropna().tolist())
        seasonal_avg[season] = round(np.mean(temps), 2)
    
    output_file = os.path.join(SCRIPT_FOLDER, "average_temp.txt")
    with open(output_file, "w") as f:
        for season, avg in seasonal_avg.items():
            f.write(f"{season}: {avg}°C\n")
    print(f"[✓] Seasonal averages saved to {output_file}")

def calculate_largest_temp_range(station_dfs):
    station_ranges = []
    for df in station_dfs:
        for _, row in df.iterrows():
            temps = row[5:].dropna().tolist()  # Months start at column 5
            if temps:
                max_temp = max(temps)
                min_temp = min(temps)
                station_ranges.append((row["STATION_NAME"], max_temp, min_temp, max_temp - min_temp))
    
    if not station_ranges:
        return

    max_range = max(station_ranges, key=lambda x: x[3])[3]
    largest_stations = [s for s in station_ranges if round(s[3], 2) == round(max_range, 2)]
    
    output_file = os.path.join(SCRIPT_FOLDER, "largest_temp_range_station.txt")
    with open(output_file, "w") as f:
        for s in largest_stations:
            f.write(f"Station {s[0]}: Range {round(s[3], 2)}°C (Max: {round(s[1], 2)}°C, Min: {round(s[2], 2)}°C)\n")
    print(f"[✓] Largest temperature range saved to {output_file}")

def calculate_temperature_stability(station_dfs):
    station_std = []
    for df in station_dfs:
        for _, row in df.iterrows():
            temps = row[5:].dropna().tolist()
            if temps:
                station_std.append((row["STATION_NAME"], np.std(temps)))
    
    if not station_std:
        return

    min_std = min(station_std, key=lambda x: x[1])[1]
    max_std = max(station_std, key=lambda x: x[1])[1]

    most_stable = [s for s in station_std if round(s[1], 2) == round(min_std, 2)]
    most_variable = [s for s in station_std if round(s[1], 2) == round(max_std, 2)]

    output_file = os.path.join(SCRIPT_FOLDER, "temperature_stability_stations.txt")
    with open(output_file, "w") as f:
        for s in most_stable:
            f.write(f"Most Stable: Station {s[0]}: StdDev {round(s[1], 2)}°C\n")
        for s in most_variable:
            f.write(f"Most Variable: Station {s[0]}: StdDev {round(s[1], 2)}°C\n")
    print(f"[✓] Temperature stability saved to {output_file}")
