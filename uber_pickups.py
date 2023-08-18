import streamlit as st
import numpy as np
import pandas as pd

st.title("Uber Pickups")

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


st.markdown(" load_data is a plain old function that downloads \
             some data, puts it in a Pandas dataframe, and converts \
             the date column from text to datetime. \
             The function accepts a single parameter (nrows), which \
             specifies the number of rows that you want to load \
             into the dataframe.")

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns',inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data ...')
data = load_data(10000)
data_load_state.text('Done! (using st.cache_data)')

st.subheader("Raw data")
st.write(data)

st.subheader("Number of pickups by hour")
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24)
)[0]

#  st.bar_chart() method 
st.bar_chart(hist_values)

st.subheader('Map of all pickups')
st.map(data)