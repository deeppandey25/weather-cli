# Weather CLI Tool

## Overview
A command-line tool to fetch real-time weather data using the OpenWeather API.

## Features
- Get weather by city name
- Get weather using latitude and longitude
- Auto-detect location using IP (Bonus feature)

## Tech Stack
- Python
- Requests library
- OpenWeather API

## Approach
Instead of web scraping, I used an API because it provides structured and reliable data in JSON format. This makes parsing easier and avoids issues caused by changes in website HTML.

## How it works
1. User inputs location (city or coordinates)
2. A GET request is sent to the OpenWeather API
3. API returns data in JSON format
4. Required data is parsed and displayed

## Challenges
- Handling API key activation delay
- Managing invalid inputs (wrong city names)
- Understanding JSON parsing

---

## 🔐 API Key Setup

⚠️ API key is not included for security reasons. Please use your own.

1. Get your API key from: https://openweathermap.org/api  
2. Set it as an environment variable:

### Windows
```bash
setx OPENWEATHER_API_KEY "your_api_key"