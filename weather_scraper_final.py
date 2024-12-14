import requests
from datetime import datetime

# Your API key
api_key = "2e704e3beff98d5cc71adf8561190d2e"

# Base URL for OpenWeatherMap
base_url = "http://api.openweathermap.org/data/2.5/weather"

# Input: Ask the user for the city name
city_name = input("Enter the city name: ")

# Construct the complete API URL with country code
url = f"{base_url}?q={city_name},US&appid={api_key}&units=metric"

# Fetch data from the API
response = requests.get(url)

# Parse the response (JSON)
weather_data = response.json()

# Display and Save the weather information
if weather_data["cod"] == 200:  # Status code 200 means "OK"
    city = weather_data["name"]
    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    weather_description = weather_data["weather"][0]["description"]

    # Print the results to the console
    print(f"Weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {weather_description.capitalize()}")

    # Get current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save the results to a file with date and time
    with open("weather_data.txt", "a") as file:
        file.write(f"Weather in {city} - {current_time}:\n")
        file.write(f"Temperature: {temp}°C\n")
        file.write(f"Humidity: {humidity}%\n")
        file.write(f"Description: {weather_description.capitalize()}\n")
        file.write("-" * 30 + "\n")  # Adds a separator between entries

    print("Weather data saved to 'weather_data.txt'.")

else:
    print("City not found. Please check the name and try again.")