import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("Weather_API_KEY")

def get_weather_alerts(city):
    # Security Check: Ensure the application has a key before proceeding
    if not API_KEY:
        print("Configuration Error: API Key is missing.")
        return None

    # Task 3: Removed city logging to protect user privacy.
    # REASON: In a healthcare context, location data combined with health 
    # service usage can be considered Protected Health Information (PHI). 
    # Under HIPAA (Health Insurance Portability and Accountability Act), 
    # logging specific identifiers like geography increases the risk of 
    # unauthorized data exposure.
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    
    try:
        response = requests.get(url)
        
        # Task 2: Handle Status Codes and Rate Limiting
        if response.status_code == 429:
            print("Notice: Weather service is currently busy (Rate limit reached). Please try again in a minute.")
            return None
        
        # Raise an exception for other HTTP errors (4xx or 5xx)
        response.raise_for_status()
        
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        # Prevents the app from crashing on connection or timeout issues
        print(f"Connection error: {req_err}")
    except KeyError:
        print("Error: Unexpected data format received from the weather service.")
    
    return None

if __name__ == "__main__":
    # Example usage for a clinic location
    weather_data = get_weather_alerts("Hyderabad")
    if weather_data:
        print("Weather alert system active.")

