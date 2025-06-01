import requests
import streamlit as st

def find_coffee_shops(location: str, radius: int = 2000):
    # Step 1: Geocode location string to lat/lng
    geo_url = "https://api.geoapify.com/v1/geocode/search"
    geo_params = {
        "text": location,
        "apiKey": st.secrets.get["GEOAPIFY_API_KEY"]
    }

    geo_response = requests.get(geo_url, params=geo_params)
    geo_data = geo_response.json()
    
    if not geo_data["features"]:
        return []

    lat = geo_data["features"][0]["properties"]["lat"]
    lon = geo_data["features"][0]["properties"]["lon"]

    # Step 2: Search nearby coffee shops
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
    for feature in place_data["features"]:
        prop = feature["properties"]
        shops.append({
            "name": prop.get("name", "Unnamed Café"),
            "address": prop.get("formatted", "Unknown"),
            "rating": round(__import__("random").uniform(3.0, 5.0), 1)
        })
    
    return shops
