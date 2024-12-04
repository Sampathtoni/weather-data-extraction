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

### Additional Notes
1.'Please make sure the working directory is correctly set to the folder containing the project files when running the scripts'.
2.'You can add or remove cities in the settings.json file without modifying the code'.
3.If there are any issues, please look at the error messages in the console for debugging.
