import requests
from config import API_KEY, BASE_URL


def get_weather(city):
    params = {
        "key": API_KEY,
        "q": city
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)

        if response.status_code == 200:
            data = response.json()

            weather = {
                "city": data["location"]["name"],
                "country": data["location"]["country"],
                "temperature": data["current"]["temp_c"],
                "feels_like": data["current"]["feelslike_c"],
                "humidity": data["current"]["humidity"],
                "pressure": data["current"]["pressure_mb"],
                "wind_speed": data["current"]["wind_kph"],
                "condition": data["current"]["condition"]["text"]
            }

            return weather

        elif response.status_code == 400:
            print("City not found.")
            return None

        elif response.status_code == 401:
            print("Invalid API Key.")
            return None

        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            return None

    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
        return None