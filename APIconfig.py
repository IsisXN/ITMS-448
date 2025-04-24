# Configuration file for API keys and settings

# OpenWeatherMap API (Weather data)
OPENWEATHER_API_KEY = "your_openweather_api_key_here"

# AirVisual API (Air quality data)
AIRVISUAL_API_KEY = "your_airvisual_api_key_here"

# Eventbrite API (Local events)
EVENTBRITE_API_KEY = "your_eventbrite_api_key_here"

# NewsAPI (News)
NEWS_API_KEY = "your_newsapi_key_here"

# Default location (can be changed in GUI)
DEFAULT_LOCATION = {
    "city": "New York",
    "country": "US",
    "lat": 40.7128,
    "lon": -74.0060
}

# API endpoints
API_ENDPOINTS = {
    "weather": "https://api.openweathermap.org/data/2.5/weather",
    "air_quality": "http://api.airvisual.com/v2/nearest_city",
    "events": "https://www.eventbriteapi.com/v3/events/search/",
    "news": "https://newsapi.org/v2/top-headlines"
}