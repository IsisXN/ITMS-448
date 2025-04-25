class RecommendationEngine:
    def __init__(self, api_client):
        self.api_client = api_client

    def generate_recommendations(self, location):
        """Generate lifestyle recommendations based on current conditions"""
        recommendations = []
        
        # Get all necessary data
        weather_data = self.api_client.get_weather_data(location)
        air_quality_data = self.api_client.get_air_quality_data(location)
        
        if not weather_data or not air_quality_data:
            return ["Unable to fetch data. Please check your internet connection and try again."]
        
        # Weather-based recommendations
        temp = weather_data['main']['temp']
        weather_main = weather_data['weather'][0]['main']
        weather_desc = weather_data['weather'][0]['description']
        
        recommendations.append(f"Current weather: {weather_desc}")
        
        if temp < 10:
            recommendations.append("❄️ It's very cold! Wear heavy winter clothing.")
        elif temp < 15:
            recommendations.append("☁️ It's chilly. A jacket would be good.")
        elif temp < 25:
            recommendations.append("🌤 Pleasant weather! Light clothing recommended.")
        else:
            recommendations.append("☀️ It's hot! Stay hydrated and wear light clothes.")
            
        if "rain" in weather_desc.lower():
            recommendations.append("☔ Don't forget your umbrella! It's raining.")
        elif "snow" in weather_desc.lower():
            recommendations.append("⛄ Snow expected! Be careful if driving.")
            
        # Air quality recommendations
        aqi = air_quality_data.get('data', {}).get('current', {}).get('pollution', {}).get('aqius', 0)
        
        if aqi > 0:
            recommendations.append(f"Air Quality Index: {aqi}")
            if aqi <= 50:
                recommendations.append("😊 Air quality is good. Great day for outdoor activities!")
            elif aqi <= 100:
                recommendations.append("🙂 Air quality is moderate. Decent for outdoor activities.")
            elif aqi <= 150:
                recommendations.append("😷 Air quality is unhealthy for sensitive groups. Consider limiting outdoor activities.")
            elif aqi <= 200:
                recommendations.append("🤒 Air quality is unhealthy. Reduce outdoor activities.")
            elif aqi <= 300:
                recommendations.append("😨 Air quality is very unhealthy. Avoid outdoor activities.")
            else:
                recommendations.append("⚠️ Air quality is hazardous. Stay indoors if possible.")
        
        # Activity suggestions based on weather
        if weather_main in ['Clear', 'Clouds'] and temp > 15 and aqi <= 100:
            events = self.api_client.get_local_events(location, "outdoors")
            if events and events.get('events'):
                recommendations.append("🎟️ Great day for outdoor activities! Check out these events:")
                for event in events['events'][:3]:  # Show top 3 events
                    time_str = event['start']['local'].split('T')[1][:5] if 'T' in event['start']['local'] else "all day"
                    recommendations.append(f"- {event['name']} at {event['venue']} ({time_str})")
        
        # News headlines
        news = self.api_client.get_news(location)
        if news and news.get('articles'):
            recommendations.append("📰 Top news headlines:")
            for article in news['articles'][:3]:
                recommendations.append(f"- {article['title']}")
        
        return recommendations