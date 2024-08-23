import streamlit as st
from datetime import datetime
import requests
import numpy as np

# TaxiFareModel front


st.title("Predict NYC taxi fare prices")
st.subheader("vroom vroom 🚕")

url = 'https://taxifare-659642642571.europe-west1.run.app/predict'

dt_col, pickup_col, dropoff_col, passengers_col = st.columns(4)

with dt_col:
    st.caption("Date and time of ride")
    date = st.date_input("Pickup date")
    time = st.time_input("Pickup time")

dt = datetime.combine(date, time)
dt_str = dt.strftime("%Y/%m/%d %H:%M:%S")

with pickup_col:
    st.caption("Pickup coordinates")
    p_longitude = st.number_input("Pickup longitude", format = "%.6f",
                                  min_value=-74.3, max_value=-73.7)
    p_latitude = st.number_input("Pickup latitude", format = "%.6f",
                                 min_value=40.5, max_value=40.9)

with dropoff_col:
    st.caption("Dropoff coordinates")
    d_longitude = st.number_input("Dropoff longitude", format = "%.6f",
                                  min_value=-74.3, max_value=-73.7)
    d_latitude = st.number_input("Dropoff latitude", format = "%.6f",
                                 min_value=40.5, max_value=40.9)

with passengers_col:
    st.caption("Number of passengers")
    passengers = st.number_input("Passenger count", step = 1)

params = {"pickup_datetime": dt_str,
          "pickup_longitude" : p_longitude,
          "pickup_latitude" : p_latitude,
          "dropoff_longitude" : d_longitude,
          "dropoff_latitude" : d_latitude,
          "passenger_count" : passengers}


button = st.button("Get prediction")
if button:
    response = requests.get(url, params = params)
    js = response.json()['fare']
    fare = np.round(js, 2)
    st.text(f"The predicted fare is {fare}!")
