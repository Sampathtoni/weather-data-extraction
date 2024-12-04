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
cd weather_data_extractor

Step 2: Create Required Files
Inside the project directory, create the following files and populate them with the corresponding code/content:

fetch_weather.py: This script fetches weather data from the OpenWeatherMap API.
parse_weather.py: This script parses the fetched JSON data and converts it into a CSV file.
settings.json: This metadata-driven configuration file contains API settings, locations, and output configurations.
README.md: This documentation file (the file you are currently reading).
Step 3: Install Dependencies
Install the required Python libraries:

bash
Copy code
pip install requests pandas  
Configuration
Edit the settings.json file to customize locations, units, and file output preferences. Below is an example configuration:

json
Copy code
{  
  "api_key": "your_openweathermap_api_key",  
  "locations": ["London", "New York", "Tokyo"],  
  "units": "metric",  
  "output_files": {  
    "json": "weather_output.json",  
    "csv": "weather_data.csv"  
  }  
}  
Usage
Step 1: Fetch Weather Data
Run the fetch_weather.py script to retrieve current weather data from OpenWeatherMap:

bash
Copy code
python fetch_weather.py  
The fetched data will be saved as weather_output.json.

Step 2: Parse JSON to CSV
Run the parse_weather.py script to process the JSON file and convert it to CSV format:

bash
Copy code
python parse_weather.py  
The parsed data will be saved as weather_data.csv.

Step 3: Verify Outputs
Check your project directory to ensure that weather_output.json and weather_data.csv are correctly created.

Example Outputs
Raw JSON File:
Example content from weather_output.json:

json
Copy code
{  
  "city": "London",  
  "temperature": 15,  
  "humidity": 80,  
  "conditions": "Cloudy"  
}  
Parsed CSV File:
Example content from weather_data.csv:

City	Temperature	Humidity	Conditions
London	15°C	80%	Cloudy
New York	20°C	65%	Sunny
Contributing
Contributions to improve the functionality or documentation are welcome! To contribute:

Fork this repository.
Create a new branch for your feature or bug fix.
Submit a pull request with a detailed explanation of your changes.

