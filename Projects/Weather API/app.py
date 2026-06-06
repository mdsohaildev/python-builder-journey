import streamlit as st
from weather_api import get_weather

st.title("GET WEATHER")
st.subheader("By city name")
city = st.text_input("ENTER CITY NAME:")
if st.button("get weather"):
    k = get_weather(city)
    st.success("Weather fetched successfully!")
    st.write(f"City: {k['CITY']}")
    st.write(f"Temperature: {k['TEMPERATURE']} °C")
    st.write(f"Humidity: {k['HUMIDITY']} %")
    st.write(f"Condition: {k['CONDITION']}")

