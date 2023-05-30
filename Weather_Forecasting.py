import requests
import json

def get_weather(city):
    api_key = '85309ece37467d16fbc015e72025cf71'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = json.loads(response.text)

        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']

        temperature_celsius = temperature - 273.15

        print(f"Weather forecast for {city}:")
        print(f"Temperature: {temperature_celsius:.2f}°C")
        print(f"Description: {description}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

city_name = input("Enter a city name: ")
get_weather(city_name)


