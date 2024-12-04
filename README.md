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

---
## Step 2: Create Required Files
Inside the project directory, create the following files and populate them with the corresponding code/content:

fetch_weather.py: This script fetches weather data from the OpenWeatherMap API.
parse_weather.py: This script parses the fetched JSON data and converts it into a CSV file.
config.json: This metadata-driven configuration file contains API settings, locations, and output configurations.
README.md: This documentation file (the file you are currently reading).
