# Configuration file for API keys and settings

# OpenWeatherMap API (Weather data)
OPENWEATHER_API_KEY = "bebda8996ee02d83265ef88e95d3b7f3"

# AirVisual API (Air quality data)
AIRVISUAL_API_KEY = "dc47b586-4d4d-4be9-91f1-2efc06cfa503"

# TicketMaster API (Local events)
TICKETMASTER_API_KEY = "MaTBZ2Q53vhAsxIOlL6thfhhRlmAQDl1"

# NewsAPI (News)
NEWS_API_KEY = "7f81b33d570c4a01a0a21dfa7108e408"

# Default location (can be changed in GUI)
DEFAULT_LOCATION = {
    "city": "Chicago",
    "country": "US",
    "lat": 46.934913,
    "lon": -97.616377
}

# API endpoints
API_ENDPOINTS = {
    "weather": "https://api.openweathermap.org/data/2.5/weather",
    "air_quality": "http://api.airvisual.com/v2/nearest_city",
    "events": "https://app.ticketmaster.com/discovery/v2/events.json",
    "news": "https://newsapi.org/v2/top-headlines"
}