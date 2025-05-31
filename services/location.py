import overpy
from geopy.geocoders import Nominatim
import random

api = overpy.Overpass()
geolocator = Nominatim(user_agent="coffee-finder-app")

def resolve_location_to_coords(location_str: str):
    if "," in location_str:
        try:
            lat, lon = map(float, location_str.split(","))
            return lat, lon
        except ValueError:
            pass  # fallback to geocoding below

    location = geolocator.geocode(location_str)
    if location:
        return location.latitude, location.longitude
    raise ValueError("Could not resolve location")

def find_coffee_shops(location_str: str, radius: int = 1000):
    lat, lon = resolve_location_to_coords(location_str)
    
    query = f"""
    node
      [amenity=cafe]
      (around:{radius},{lat},{lon});
    out;
    """
    result = api.query(query)
    shops = []
    for node in result.nodes:
        name = node.tags.get("name", "Unnamed Café")
        rating = round(random.uniform(3.0,5.0),1)
        shops.append({
            "name": name,
            "address": f"{node.lat}, {node.lon}",
            "rating": rating
        })
    return shops
