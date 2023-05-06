import streamlit as st
import plotly.express as px
from backend import get_data

# Title of the page
st.title("Weather Forecast for the Next Days")

# Input for place
place = st.text_input("Place:")

# No.of Forecast days
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

# Select type of data to display
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")


if place:
    # Get temperature/sky data
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        # Create a temperature plot
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date",
                                                          "y": "Temperature(c)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Rain": "images/rain.png", "Clear": "images/clear.png",
                  "Cloud": "images/cloud.png", "Snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=115)