import requests
import json
from APIconfig import OPENWEATHER_API_KEY, AIRVISUAL_API_KEY, EVENTBRITE_API_KEY, NEWS_API_KEY, API_ENDPOINTS

class APIClient:
    def __init__(self):
        self.api_keys = {
            "weather": OPENWEATHER_API_KEY,
            "air_quality": AIRVISUAL_API_KEY,
            "events": EVENTBRITE_API_KEY,
            "news": NEWS_API_KEY
        }
        self.endpoints = API_ENDPOINTS

    def get_weather_data(self, location):
        """Fetch current weather data for a location"""
        params = {
            'lat': location['lat'],
            'lon': location['lon'],
            'appid': self.api_keys['weather'],
            'units': 'metric'
        }
        try:
            response = requests.get(self.endpoints['weather'], params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Weather API error: {e}")
            return None

    def get_air_quality_data(self, location):
        """Fetch air quality data for a location"""
        params = {
            'lat': location['lat'],
            'lon': location['lon'],
            'key': self.api_keys['air_quality']
        }
        try:
            response = requests.get(self.endpoints['air_quality'], params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Air Quality API error: {e}")
            return None

    def get_local_events(self, location, category=None):
        """Fetch local events for a location"""
        headers = {
            "Authorization": f"Bearer {self.api_keys['events']}"
        }
        params = {
            "location.address": location['city'],
            "location.within": "50km",
            "sort_by": "date"
        }
        if category:
            params["categories"] = category
            
        try:
            response = requests.get(self.endpoints['events'], headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Events API error: {e}")
            return None

    def get_news(self, location, category="general"):
        """Fetch news for a location"""
        params = {
            "apiKey": self.api_keys['news'],
            "country": location['country'].lower(),
            "category": category
        }
        try:
            response = requests.get(self.endpoints['news'], params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"News API error: {e}")
            return None