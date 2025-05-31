import streamlit as st

def show_booking_form(shop_name: str, idx: int):
    form_key = f"booking_form_{idx}"

    with st.form(key=form_key):
        st.markdown(f"### Booking at {shop_name}")
        user_name = st.text_input("Your Name", key=f"name_{idx}")
        people = st.number_input("Number of People", min_value=1, max_value=20, key=f"people_{idx}")
        phone = st.text_input("Phone Number", key=f"phone_{idx}")
        submit = st.form_submit_button("Confirm Booking")

        if submit:
            st.success(f"✅ Booking confirmed at {shop_name} for {people} people. We will contact you at {phone}.")
            # Optional: store or return booking details here
