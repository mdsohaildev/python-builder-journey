import streamlit as st
from weather_api import get_weather

st.title("🌦 Weather App")

city = st.text_input("Enter City Name")

if st.button("Get Weather"):

    data = get_weather(city)

    if "ERROR" in data:
        st.error(data["ERROR"])

    else:
        st.success("Weather fetched successfully!")

        st.write(f"📍 City: {data['CITY']}")
        st.write(f"🌡 Temperature: {data['TEMPERATURE']} °C")
        st.write(f"💧 Humidity: {data['HUMIDITY']} %")
        st.write(f"☁ Condition: {data['CONDITION']}")

