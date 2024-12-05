# Weather Data Extraction Tool  

**Weather Data Extraction Tool** is a Python-based application designed to fetch and process weather data from the [OpenWeatherMap API](https://openweathermap.org/api). This tool saves raw weather data in JSON format and converts it to a streamlined CSV file, making it easy to analyze and integrate into other workflows.  

---

## Features  

- **Metadata-Driven Configuration**: Easily manage locations, units, and output file settings through a `settings.json` file.  
- **Real-Time Weather Data**: Fetch current weather data directly from the OpenWeatherMap API.  
- **Dual Outputs**: Save raw responses in JSON format and process them into clean, human-readable CSV files.  

---

## Prerequisites  

Before using the tool, ensure the following prerequisites are met:  
1. **Python Version**: Python 3.7 or higher.  
2. **OpenWeatherMap API Key**: Get your API key by signing up at [OpenWeatherMap](https://openweathermap.org/api).  

---

## Setup and Installation  

Follow these steps to set up the project:

### Step 1: Create Project Directory  
Open a terminal or file explorer and create a new directory:  
  ```bash
        mkdir weather_data_extractor
   ```

### Step 2: Create the Files 
Inside the directory, create the following files:
1. **fetch_weather.py**:
This script fetches the weather data from the OpenWeatherMap API.
Save the code provided in the Step 1: Fetch Weather Data section into this file.
2. **parse_weather.py**:
This script parses the JSON file and converts it to CSV format.
Save the code provided in the Step 2: Parse JSON Data section into this file.
3.  **config.json**:
This is the metadata-driven configuration file.
Save the JSON example from Step 3: Configuration File into this file.
4. **README.md**:
This file provides documentation for your project.
Copy the content from Step 4: Instructions in README into this file.

### Step 3: Install Dependencies 
 If you haven’t already installed the required Python libraries (requests and pandas), do so by running:
 ```bash
  pip install requests pandas
```

### Step 4: How to Run the Application

## Fetch Weather Data 
Run the `fetch_weather.py` script to retrieve weather data from OpenWeatherMap and save it in JSON format:
```bash
%python
fetch_weather.py
```

## Convert JSON to CSV

Use the parse_weather.py script to parse the JSON file and save the processed data as a CSV file:
```bash
%python
parse_weather.py
```
### File Outputs

- **Raw JSON File:**: Saved as weather_data.json, containing the unprocessed API response.
- **Processed CSV File**: Saved as weather_data.csv, containing structured weather data.
  
---

## Sample Output
# JSON File (weather_output.json)

Below is an example of the raw weather data saved in the JSON file:
```bash
json
[
  {
    "City": "London",
    "Country": "GB",
    "Temperature (°C)": 7.05,
    "Humidity (%)": 87,
    "Pressure (hPa)": 1026,
    "Weather Description": "overcast clouds"
  },
  {
    "City": "New York",
    "Country": "US",
    "Temperature (°C)": -0.65,
    "Humidity (%)": 74,
    "Pressure (hPa)": 1026,
    "Weather Description": "clear sky"
  },
  {
    "City": "Mumbai",
    "Country": "IN",
    "Temperature (°C)": 31.99,
    "Humidity (%)": 51,
    "Pressure (hPa)": 1008,
    "Weather Description": "smoke"
  }
]
```
---
## CSV File (weather_data.csv)
The processed CSV file will look like this:

| City     | Country   |   Temperature (°C) |   Humidity (%) |   Pressure (hPa) | Weather Description   |
|:---------|:----------|-------------------:|---------------:|-----------------:|:----------------------|
| London   | GB        |               7.05 |             87 |             1026 | overcast clouds       |
| New York | US        |              -0.65 |             74 |             1026 | clear sky             |
| Mumbai   | IN        |              31.99 |             51 |             1008 | smoke                 |


---
### Additional Notes

- Ensure the working directory is set correctly to the folder containing the project files when running the scripts.
- The `config.json` file is designed to allow easy configuration of:
  - Cities for weather data retrieval.
  - Units of measurement (`metric`, `imperial`, or `standard`).
  - Output filenames for JSON and CSV files.
- If you encounter issues with the API, verify:
  1. Your API key is correct and active.
  2. You haven't exceeded the API request limit.
  3. The city names in `config.json` match the format supported by OpenWeatherMap.

---

## Extending the Project

This project is modular and can be extended to include:
- **Historical Weather Data**: Modify the API endpoint to fetch historical data.
- **Weather Forecasts**: Add support for 7-day or hourly forecasts.
- **Visualization**: Use Python libraries like Matplotlib or Seaborn to visualize the weather data.

## Contact Information

For any questions or feedback regarding this project, please feel free to reach out:

- **GitHub Profile**: [Sampathtoni](https://github.com/Sampathtoni)
- **Email**: sampathdataengineer25@gmail.com.com


