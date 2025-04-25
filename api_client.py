import requests
from datetime import datetime, timedelta
from APIconfig import OPENWEATHER_API_KEY, AIRVISUAL_API_KEY, TICKETMASTER_API_KEY, NEWS_API_KEY, API_ENDPOINTS

class APIClient:
    def __init__(self):
        self.api_keys = {
            "weather": OPENWEATHER_API_KEY,
            "air_quality": AIRVISUAL_API_KEY,
            "events": TICKETMASTER_API_KEY,
            "news": NEWS_API_KEY
        }
        self.endpoints = API_ENDPOINTS

    def _make_api_request(self, endpoint, params=None, headers=None, timeout=5):
        """Generic API request handler with error handling"""
        try:
            response = requests.get(
                self.endpoints[endpoint],
                params=params,
                headers=headers,
                timeout=timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API Error ({endpoint}): {str(e)}")
            return None

    def get_weather_data(self, location):
        """Fetch current weather data"""
        params = {
            'lat': location['lat'],
            'lon': location['lon'],
            'appid': self.api_keys['weather'],
            'units': 'metric'
        }
        return self._make_api_request('weather', params)

    def get_air_quality_data(self, location):
        """Fetch air quality data"""
        params = {
            'lat': location['lat'],
            'lon': location['lon'],
            'key': self.api_keys['air_quality']
        }
        return self._make_api_request('air_quality', params)

    def get_local_events(self, location, category=None):
        # Try Ticketmaster API first
        events = self._get_ticketmaster_events(location, category)
        if events is not None:
            return events
            
        # Fallback to mock data if API fails
        return self._get_mock_events(location, category)

    def _get_ticketmaster_events(self, location, category=None):
        """Internal method to fetch events from Ticketmaster API"""
        params = {
            'apikey': self.api_keys['events'],
            'city': location['city'],
            'countryCode': location['country'],
            'radius': '50',
            'unit': 'km',
            'sort': 'date,asc',
            'size': '3'
        }
        
        # Map categories to Ticketmaster classifications
        category_map = {
            'outdoors': ['outdoor', 'sports'],
            'music': ['music'],
            'arts': ['arts']
        }
        
        if category and category in category_map:
            params['classificationName'] = ','.join(category_map[category])
        
        data = self._make_api_request('events', params)
        if data is None:
            return None
            
        # Process successful response
        if '_embedded' in data and 'events' in data['_embedded']:
            events = []
            for event in data['_embedded']['events']:
                event_data = {
                    'name': event.get('name', 'Unknown Event'),
                    'url': event.get('url', '#'),
                    'start': {
                        'local': self._format_event_time(event.get('dates', {}).get('start'))
                    },
                    'venue': self._get_venue_name(event)
                }
                events.append(event_data)
            return {'events': events}
        return None

    def _format_event_time(self, start_data):
        """Format event time from API response"""
        if not start_data:
            return datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        
        date = start_data.get('localDate', '')
        time = start_data.get('localTime', '00:00:00')
        return f"{date}T{time}" if date else datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    def _get_venue_name(self, event):
        """Extract venue name from event data"""
        if '_embedded' in event and 'venues' in event['_embedded']:
            return event['_embedded']['venues'][0].get('name', 'Unknown venue')
        return 'Unknown venue'


    def get_news(self, location, category="general"):
        """Fetch news headlines"""
        params = {
            "apiKey": self.api_keys['news'],
            "country": location['country'].lower(),
            "category": category,
            "pageSize": 3
        }
        return self._make_api_request('news', params)