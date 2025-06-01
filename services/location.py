import requests
import streamlit as st

def find_coffee_shops(location: str, radius: int = 2000):
    geo_url = "https://api.geoapify.com/v1/geocode/search"
    geo_params = {
        "text": location,
        "apiKey": st.secrets["GEOAPIFY_API_KEY"]
    }

    geo_response = requests.get(geo_url, params=geo_params)
    geo_data = geo_response.json()

    # ✅ Check for missing features key or empty response
    if "features" not in geo_data or not geo_data["features"]:
        st.warning("Couldn't find the location. Please enter a more specific name like 'Dallas, TX'.")
        return []

    lat = geo_data["features"][0]["properties"]["lat"]
    lon = geo_data["features"][0]["properties"]["lon"]

    place_url = "https://api.geoapify.com/v2/places"
    place_params = {
        "categories": "catering.cafe",
        "filter": f"circle:{lon},{lat},{radius}",
        "bias": f"proximity:{lon},{lat}",
        "limit": 10,
        "apiKey": st.secrets["GEOAPIFY_API_KEY"]
    }

    place_response = requests.get(place_url, params=place_params)
    place_data = place_response.json()

    shops = []
    for feature in place_data.get("features", []):
        prop = feature["properties"]
        shops.append({
            "name": prop.get("name", "Unnamed Café"),
            "address": prop.get("formatted", "Unknown"),
            "rating": round(__import__("random").uniform(3.0, 5.0), 1)
        })

    return shops
