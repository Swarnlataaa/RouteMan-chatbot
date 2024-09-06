import streamlit as st
import requests

# Define custom CSS for positioning the logo
st.markdown(
    """
    <style>
    .header-logo {
        position: fixed;
        top: 0;
        right: 0;
        margin: 10px 10px 0 0;
        font-family: 'Arial', sans-serif;
        font-size: 24px;
        font-weight: bold;
        color: #FF4B4B; /* Change color as needed */
    }
    .header-logo img {
        width: 50px;
        height: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the logo at the top-right corner
st.markdown(
    """
    <div class="header-logo">
        <!-- You can use an image instead of text as a logo -->
        <span>🚌 RouteMan</span> 
    </div>
    """,
    unsafe_allow_html=True
)

# Set up Streamlit page
st.title("Bus Route Chatbot")

# Create chatbot style input boxes
st.subheader("Enter your details below:")

pickup_point = st.text_input("Pickup Point")
destination_point = st.text_input("Destination Point")

# Button to submit the input and fetch data
if st.button("Find Routes"):
    if pickup_point and destination_point:
        st.write(f"Searching routes from {pickup_point} to {destination_point}...")

        # Placeholder for fetching bus route data
        routes = [
            {"bus": "Bus 101", "route": "Route A", "timing": "8:00 AM, 9:00 AM, 10:00 AM"},
            {"bus": "Bus 202", "route": "Route B", "timing": "8:30 AM, 9:30 AM, 10:30 AM"},
            {"bus": "Bus 303", "route": "Route C", "timing": "9:00 AM, 10:00 AM, 11:00 AM"}
        ]

        # Display the available routes
        for route in routes:
            st.write(f"Bus: {route['bus']}, Route: {route['route']}, Timings: {route['timing']}")
    else:
        st.error("Please enter both Pickup and Destination points.")

# Chatbot interaction
st.subheader("Chatbot Interaction")
user_message = st.text_input("Chat with the bot:")

if st.button("Send Message"):
    if user_message:
        # Placeholder for chatbot logic (e.g., integrate with OpenAI API or other chatbot engine)
        bot_response = f"You said: {user_message}. How can I assist further?"
        st.write(bot_response)
    else:
        st.error("Please enter a message.")
