import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

PATH = "/Users/Kerryn/daily-code-journal/daily-codes/DATA/"
FILE = "UK House price index.xlsx"

cols = ['Date', 'City of London', 'Barking & Dagenham', 'Barnet', 'Bexley',
       'Brent', 'Bromley', 'Camden', 'Croydon', 'Ealing', 'Enfield',
       'Greenwich', 'Hackney', 'Hammersmith & Fulham', 'Haringey', 'Harrow',
       'Havering', 'Hillingdon', 'Hounslow', 'Islington',
       'Kensington & Chelsea', 'Kingston upon Thames', 'Lambeth', 'Lewisham',
       'Merton', 'Newham', 'Redbridge', 'Richmond upon Thames', 'Southwark',
       'Sutton', 'Tower Hamlets', 'Waltham Forest', 'Wandsworth',
       'Westminster',]

st.title("London Housing Prices: 1995 - 2022")

@st.cache
def load_data():
    '''Returns dataframe, ignores first row and uses boroughs as columns'''
    df = pd.read_excel(PATH + FILE, sheet_name="Average price")
    df = df.iloc[1:, :]
    df = df.rename(columns={"Unnamed: 0": "Date"})
    df = df[cols]
    df[cols[1:]] = df[cols[1:]].apply(pd.to_numeric)
    df['Average Price London'] = df[cols[1:]].mean(axis=1)
    df[cols[1:]] = round(df[cols[1:]], 0)

    return df

housing_df = load_data() 

print(housing_df.info()
)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(housing_df.head(10))

st.subheader('Average Annual Price per Borough')
no_years = 2022 - 1995
# ave_price = sns.lineplot(x='Date', y='Average Price London', data=housing_df)
st.line_chart(data=housing_df, x='Date', y='Average Price London')

if st.checkbox('Show Average Price per Borough'):
    st.subheader('Price per Borough')
    st.line_chart(housing_df, x=cols[0], y=cols[1:], width=700, use_container_width=True)
    # c = alt.Chart(housing_df).mark_line().encode(x=cols[0], y=cols[1:])
    # st.altair_chart(c)
    # st.balloons()
    # st.write(housing_df.head(10))



