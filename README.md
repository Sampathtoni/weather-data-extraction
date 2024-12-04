# Weather Data Extraction Tool

## Overview
This project provides a Python-based tool to extract weather data from OpenWeatherMap. It saves the raw JSON response and parses it into a CSV file, excluding unnecessary data for simplicity.

## Features
- Metadata-driven to easily configure locations, units, and output files.
- Fetches current weather data from OpenWeatherMap's API.
- Saves raw responses in JSON and processes them into CSV format.

## Prerequisites
- Python 3.7 or higher.
- An OpenWeatherMap API key (sign up at [OpenWeatherMap](https://openweathermap.org/)).

## Setup and Installation
Step 1: Create Project Directory
Open a terminal or file explorer.
Create a new directory for your project:
mkdir weather_data_extractor
cd weather_data_extractor
Step 2: Create the Files
Inside the directory, create the following files:
1. fetch_weather.py
This script fetches the weather data from the OpenWeatherMap API.
Save the code provided in the Step 1: Fetch Weather Data section into this file.
2. parse_weather.py
This script parses the JSON file and converts it to CSV format.
Save the code provided in the Step 2: Parse JSON Data section into this file.
3. settings.json
This is the metadata-driven configuration file.
Save the JSON example from Step 3: Configuration File into this file.
4. README.md
This file provides documentation for your project.
Copy the content from Step 4: Instructions in README into this file.
Step 3: Install Dependencies
If you haven’t already installed the required Python libraries (requests and pandas), do so by running:
pip install requests pandas
Step 4: Test Your Code
Fetch Weather Data Run the fetch_weather.py script to fetch data and save it to weather_output.json:
python fetch_weather.py
Parse JSON to CSV Run the parse_weather.py script to parse the JSON data and save it to weather_data.csv:
python parse_weather.py
Verify that the output files (weather_output.json and weather_data.csv) are correctly created in your directory.
