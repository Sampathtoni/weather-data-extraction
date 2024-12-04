import json
import pandas as pd

def convert_to_csv(config_path="config.json"):
    # Load configuration details
    with open(config_path, "r") as config_file:
        settings = json.load(config_file)

    json_input = settings["json_output"]
    csv_output = settings["csv_output"]

    # Load JSON data from the file
    with open(json_input, "r") as input_file:
        weather_records = json.load(input_file)

    processed_data = []

    for record in weather_records:
        # Extract key fields from the API response
        row = {
            "City": record.get("name"),
            "Country": record.get("sys", {}).get("country"),
            "Temperature (°C)": record.get("main", {}).get("temp"),
            "Humidity (%)": record.get("main", {}).get("humidity"),
            "Pressure (hPa)": record.get("main", {}).get("pressure"),
            "Weather Description": record.get("weather", [{}])[0].get("description"),
        }
        processed_data.append(row)

    # Create a DataFrame and save it as a CSV file
    weather_df = pd.DataFrame(processed_data)
    weather_df.to_csv(csv_output, index=False)

    print(f"Data converted and saved to {csv_output}")

if __name__ == "__main__":
    convert_to_csv()
