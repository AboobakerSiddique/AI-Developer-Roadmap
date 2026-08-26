def get_weather(city: str) -> dict:
    """
    Get weather information for a city.

    Args:
        city: The city whose weather should be retrieved.

    Returns:
        A dictionary containing weather information.
    """

    weather_data = {
        "kochi": {
            "temperature_c": 29,
            "condition": "Cloudy",
            "humidity": 78
        },
        "thiruvananthapuram": {
            "temperature_c": 28,
            "condition": "Partly cloudy",
            "humidity": 80
        },
        "bangalore": {
            "temperature_c": 24,
            "condition": "Cloudy",
            "humidity": 68
        },
        "delhi": {
            "temperature_c": 32,
            "condition": "Sunny",
            "humidity": 45
        },
        "Manipal": {
            "temperature_c": 28,
            "condition": "Partly cloudy",
            "humidity": 80
        }
    }

    city_key = city.strip().lower()

    if city_key not in weather_data:
        raise ValueError(
            f"Weather data unavailable for {city}."
        )

    return weather_data[city_key]