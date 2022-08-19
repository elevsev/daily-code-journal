#  Welcome to Streamlit. Check out our demo in your browser.
#   Local URL: http://localhost:8501
#   Network URL: http://192.168.1.71:8501

import streamlit as st
import pandas as pd
import numpy as np

# df = pd.DataFrame({
#     'first_col': [1,2,3,4],
#     'second_col': [10,20,30,40]
# })

# print(df)

# st.write("Data for a table:")
# st.write(pd.DataFrame({
#     'first_col': [1,2,3,4],
#     'second_col': [10,20,30,40]
# }))

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def data_load(rows):
    data = pd.read_csv(DATA_URL, nrows=rows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_loading = st.text("Loading the data...")
data = data_load(rows=10_000)
data_loading = st.text("Data successfully loaded!")
st.write(data.head())

st.subheader("Pickups per hour:")
pickups = np.histogram(
    data[DATE_COLUMN].dt.hour,
    bins=24,
    range=(0,24)
)[0]

st.bar_chart(pickups)