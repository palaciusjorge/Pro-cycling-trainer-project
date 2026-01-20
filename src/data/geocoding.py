import requests


def geocode_city(city_name, country="Spain"):
    """
    Geocode a city name using Nominatim (OpenStreetMap).

    Returns:
        (lat, lon) or (None, None) if not found
    """
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": f"{city_name}, {country}",
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "pro-cycling-trainer"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        raise Exception("Error connecting to geocoding service")

    data = response.json()

    if len(data) == 0:
        return None, None

    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])

    return lat, lon
