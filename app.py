import streamlit as st
from services.location import find_coffee_shops
from services.summary import generate_summary
from services.booking import show_booking_form

st.set_page_config(page_title="Find Coffee Shops", layout="centered")

# Search input
st.title("☕ Find Nearby Coffee Shops")
location = st.text_input("Enter your location")

if not location:
    st.warning("Please enter a location to search for coffee shops.")
    st.stop()

# Initialize session state
if "shops" not in st.session_state:
    st.session_state.shops = []
if "active_booking" not in st.session_state:
    st.session_state.active_booking = None

# Search
if st.button("Search"):
    with st.spinner("Finding coffee shops..."):
        st.session_state.shops = find_coffee_shops(location)
        st.session_state.active_booking = None

# Show results
if st.session_state.shops:
    for idx, shop in enumerate(st.session_state.shops[:5]):
        name = shop["name"]
        address = shop["address"]
        rating = shop["rating"]
        summary = generate_summary(name, address, rating)

        st.subheader(name)
        st.write(summary)
        st.text(f"📍 {address} | ⭐ {rating}")

        if st.button(f"Book Table at {name}", key=f"book_btn_{idx}"):
            st.session_state.active_booking = idx

        if st.session_state.active_booking == idx:
            show_booking_form(name, idx)

        st.markdown("---")
