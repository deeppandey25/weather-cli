# Weather CLI Tool

## Overview
This is a command-line interface (CLI) tool that fetches real-time weather data using the OpenWeather API.

## Features
- Get weather by city name
- Get weather using latitude and longitude
- Auto-detect location using IP (Bonus feature)

## Tech Stack
- Python
- Requests library
- OpenWeather API

## Approach
Instead of raw web scraping, I used an API because it provides structured and reliable data in JSON format. This makes parsing easier and avoids issues caused by changes in website HTML.

## How it works
1. User inputs location (city or coordinates)
2. A GET request is sent to the OpenWeather API
3. API returns data in JSON format
4. Required data is parsed and displayed

## Challenges
- Handling API key activation delay
- Managing invalid inputs (wrong city names)
- Understanding JSON parsing

## How to run
1. Install dependencies:
   pip install requests

2. Run the program:
   python main.py

## Bonus
- Implemented auto-location detection using IP-based API