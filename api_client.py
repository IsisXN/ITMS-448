import requests
import json
from config import OPENWEATHER_API_KEY, AIRVISUAL_API_KEY, TICKETMASTER_API_KEY, NEWS_API_KEY, API_ENDPOINTS

class APIClient:
    def __init__(self):
        self.api_keys = {
            "weather": OPENWEATHER_API_KEY,
            "air_quality": AIRVISUAL_API_KEY,
            "events": TICKETMASTER_API_KEY,  # Now using Ticketmaster
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
        """Fetch local events using Ticketmaster API"""
        params = {
            'apikey': self.api_keys['events'],
            'city': location['city'],
            'radius': '50',
            'unit': 'km',
            'sort': 'date,asc',
            'size': '5'  # Limit to 5 results
        }
        
        # Map categories to Ticketmaster classifications
        if category == "outdoors":
            params['classificationName'] = 'outdoor'
        
        try:
            response = requests.get(self.endpoints['events'], params=params)
            response.raise_for_status()
            data = response.json()
            
            # Format the response to match expected structure
            if '_embedded' in data:
                return {
                    'events': [
                        {
                            'name': event['name'],
                            'url': event['url'],
                            'start': {
                                'local': event['dates']['start']['localDate'] + 'T' + 
                                event['dates']['start'].get('localTime', '00:00:00')
                            },
                            'venue': event['_embedded']['venues'][0]['name'] 
                            if '_embedded' in event and 'venues' in event['_embedded'] 
                            else 'Unknown venue'
                        }
                        for event in data['_embedded']['events']
                    ]
                }
            return {'events': []}
        except requests.exceptions.RequestException as e:
            print(f"Ticketmaster API error: {e}")
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