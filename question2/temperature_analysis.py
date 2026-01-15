# temperature_analysis.py
from load_data import load_temperature_data
from process_temperature import calculate_seasonal_average, calculate_largest_temp_range, calculate_temperature_stability

def main():
    seasonal_dfs, station_dfs = load_temperature_data()
    calculate_seasonal_average(seasonal_dfs)
    calculate_largest_temp_range(station_dfs)
    calculate_temperature_stability(station_dfs)
    print("[✓] All analysis complete!")

if __name__ == "__main__":
    main()
