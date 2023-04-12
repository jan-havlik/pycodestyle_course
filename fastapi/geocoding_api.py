import requests
from geopy.geocoders import Nominatim


class PlaceNotFound(Exception):
    pass


def get_coordinates_for_place(place_name: str) -> tuple:
    geolocator = Nominatim(user_agent="mendelu_python_course")
    location = geolocator.geocode(place_name)
    if location:
        return location.latitude, location.longitude
    else:
        raise PlaceNotFound(f"Location {place_name} not found")


def get_coordinates_current_location() -> tuple:
    r = requests.get("http://ip-api.com/json")
    return r.json()["lat"], r.json()["lon"]
