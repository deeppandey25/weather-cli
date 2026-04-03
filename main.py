import requests

import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")  # <-- paste your API key here


def get_weather_by_city(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if str(data["cod"]) != "200":
            print("❌ City not found!")
            return

        display_weather(data)

    except Exception as e:
        print("Error:", e)


def get_weather_by_coords(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print("❌ Invalid coordinates!")
            return

        display_weather(data)

    except Exception as e:
        print("Error:", e)


def auto_detect_location():
    try:
        res = requests.get("https://ipinfo.io")
        data = res.json()

        loc = data['loc'].split(',')
        lat, lon = loc

        print(f"\n📍 Detected Location: {data['city']}, {data['country']}")
        get_weather_by_coords(lat, lon)

    except:
        print("❌ Could not detect location")


def display_weather(data):
    weather = data['weather'][0]['description']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    humidity = data['main']['humidity']
    timezone = data['timezone']

    print("\n🌤 WEATHER DETAILS")
    print("----------------------")
    print(f"Description : {weather}")
    print(f"Min Temp    : {temp_min}°C")
    print(f"Max Temp    : {temp_max}°C")
    print(f"Humidity    : {humidity}%")
    print(f"Timezone    : {timezone}")
    print("----------------------\n")
    print(API_KEY)


if __name__ == "__main__":
    print("=== Weather CLI ===")
    print("1. Enter City")
    print("2. Enter Latitude/Longitude")
    print("3. Auto Detect Location")

    choice = input("Choose option (1/2/3): ")

    if choice == "1":
        city = input("Enter city: ")
        get_weather_by_city(city)

    elif choice == "2":
        lat = input("Enter latitude: ")
        lon = input("Enter longitude: ")
        get_weather_by_coords(lat, lon)

    elif choice == "3":
        auto_detect_location()

    else:
        print("❌ Invalid choice")