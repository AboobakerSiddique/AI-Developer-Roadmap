from datetime import datetime
from zoneinfo import ZoneInfo


CITY_TIMEZONES = {
    "kochi": "Asia/Kolkata",
    "thiruvananthapuram": "Asia/Kolkata",
    "bangalore": "Asia/Kolkata",
    "delhi": "Asia/Kolkata",
    "tokyo": "Asia/Tokyo",
    "london": "Europe/London",
    "new york": "America/New_York",
    "dubai": "Asia/Dubai"
}


def get_time(city: str) -> str:
    """
    Get the current local time for a city.

    Args:
        city: The city whose local time is requested.

    Returns:
        The current local time formatted as a string.
    """

    city_key = city.strip().lower()

    if city_key not in CITY_TIMEZONES:
        raise ValueError(
            f"Timezone unavailable for {city}."
        )

    timezone = ZoneInfo(
        CITY_TIMEZONES[city_key]
    )

    current_time = datetime.now(
        timezone
    )

    return current_time.strftime(
        "%Y-%m-%d %I:%M:%S %p"
    )