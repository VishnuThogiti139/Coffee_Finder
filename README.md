# ☕ Coffee Finder — Streamlit + Gemini AI

I built a web app using Python and Streamlit that helps people find nearby coffee shops. The user can enter any location, and the app uses OpenStreetMap’s API to find cafes around that area. Then, I use Google’s Gemini AI through LangChain to write a short, friendly description for each place.

Users can also book a table by entering their name, number of people, and phone number. I made the code modular, so everything is organized — location handling, AI text generation, and the booking form are in separate files.

Through this, I learned how to integrate APIs, work with location services, use AI models with LangChain, and build a clean, interactive frontend using Streamlit.

---

## 🌟 Features

- 🌍 Enter any location (city name or lat,lng) to search for nearby coffee shops.
- 🗺 Uses **OpenStreetMap (Overpass API)** — completely free, no API key needed.
- 🤖 Generates a unique, friendly summary for each coffee shop using **Google Gemini (via LangChain)**.
- 📋 Lets users book a table with name, number of people, and contact info.
- 📌 Designed to be modular, extensible, and easy to run from VS Code or Streamlit Cloud.

---

## 🧠 How It Works (Code Overview)

### `app.py`

- Main entry point using **Streamlit**
- Handles:
  - Location input and search trigger
  - Display of nearby cafes
  - Gemini-generated summaries
  - Booking form handling with session state

### `services/location.py`

- Uses:
  - `geopy` to convert user input (e.g., "Dallas, TX") to lat/lng
  - `overpy` to query cafes (`amenity=cafe`) around that location

### `services/summary.py`

- Connects to **Gemini** using LangChain’s `ChatGoogleGenerativeAI`
- Generates a paragraph about each shop using:


🔮 Future Enhancements
📡 1. Real-Time Table Booking API
Add a backend API endpoint:

🗺 2. Map Integration (Folium or Leaflet)
Show cafe pins on a map with popup summaries

📦 3. Database Integration
Store all bookings in SQLite or Google Sheets

📨 4. Email / SMS Confirmation
Send user a booking confirmation automatically