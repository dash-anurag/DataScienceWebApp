import streamlit as st
import pandas as pd
import numpy as np

DATE_TIME = "date/time"
DATA_URL = (
    "Motor_Vehicles_Collision_DataSet.csv"
)
st.title("Motor Vehicle Collisions in New York City")
st.markdown("This is a streamlit dashboard that can be used "
            "to analyse motor vehicles collisions in NYC 🗽💥🚗")


@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, parse_dates=[['CRASH_DATE','CRASH_TIME']])
    data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.rename(columns={'crash_date_crash_time': 'date/time'}, inplace=True)
    return data


data = load_data(1000)

st.header("Where are the most people injured in NYC?")
injured_people = st.slider("Number of persons injured in vehicle collisions",0,19)
st.map(data.query("injured_persons >= @injured_people")
       [["latitude","longitude"]].dropna(how="any"))


if st.checkbox("Show Raw Data", False):
    st.subheader('Raw Data')
    st.write(data)
