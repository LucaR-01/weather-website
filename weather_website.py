import streamlit as st
import requests

# ----------------------------------------------------------------------------------------------------

# BASE CODE

def format_response(weather):
    try:
        name = weather["name"]
        desc = weather["weather"][0]["description"].capitalize()
        temp = weather["main"]["temp"]

        finalStr = "%s \nConditions: %s ----- Temperature: %s °C" % (name, desc, temp)


    except:
        finalStr = "There was a problem retrieving the information."

    return finalStr

def get_weather(city, units):
    weather_key = "a4aa5e3d83ffefaba8c00284de6ef7c3"
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {"APPID": weather_key, "q": city, "units": units}
    response = requests.get(url, params=params)
    weather = response.json()
    formatted_weather = format_response(weather)

    if units == "Imperial":
        formatted_weather = formatted_weather.replace("C", "F")
        return formatted_weather

    else:
        return formatted_weather

# ----------------------------------------------------------------------------------------------------

# WEBSITE SETUP

st.header("Weather App")

city_input = st.text_input("City: ")
units_input = st.radio("Choose your units", ["Metric", "Imperial"])

if st.button("Go!"):
    st.subheader(get_weather(city_input, units_input))

