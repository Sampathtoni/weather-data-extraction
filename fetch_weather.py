import requests
import json

def get_weather_data(api_key, config_path="config.json"):
    # Load settings from the configuration file
    with open(config_path, "r") as config_file:
        settings = json.load(config_file)

    cities = settings["cities"]
    unit_system = settings["units"]
    json_output = settings["json_output"]

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    collected_data = []

    for city in cities:
        # Define query parameters
        parameters = {
            "q": city,
            "units": unit_system,
            "appid": api_key
        }
        # API call
        response = requests.get(base_url, params=parameters)
        if response.ok:
            collected_data.append(response.json())
        else:
            print(f"Error retrieving data for {city}: {response.status_code}")

    # Save the API responses to a JSON file
    with open(json_output, "w") as output_file:
        json.dump(collected_data, output_file, indent=4)

    print(f"Weather data successfully saved to {json_output}")

if __name__ == "__main__":
    # Replace this with your actual OpenWeatherMap API key
    API_KEY = "e48a9e8b3869945dc1fa3fe2d897ec28"
    get_weather_data(API_KEY)
