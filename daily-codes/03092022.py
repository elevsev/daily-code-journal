import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import numpy as np

df = pd.read_csv('/Users/Kerryn/daily-code-journal/daily-codes/DATA/listings.csv.gz')
cols = ['id', 'scrape_id', 'last_scraped', 'name', 'description',
       'neighborhood_overview', 'picture_url', 'host_id', 'host_url',
       'host_name', 'host_since', 'host_location', 'host_about', 'bathrooms',
       'host_response_time', 'host_response_rate', 'host_acceptance_rate',
       'host_is_superhost', 'host_thumbnail_url', 'host_picture_url',
       'host_neighbourhood', 'host_listings_count',
       'host_total_listings_count', 'host_verifications',
       'host_has_profile_pic', 'host_identity_verified', 'neighbourhood',
       'neighbourhood_cleansed', 'neighbourhood_group_cleansed', 
       'minimum_minimum_nights', 'calendar_last_scraped',
       'maximum_minimum_nights', 'minimum_maximum_nights',
       'maximum_maximum_nights', 'minimum_nights_avg_ntm',
       'maximum_nights_avg_ntm', 'calendar_updated', 'has_availability',
       'availability_30', 'availability_60', 'availability_90',
       'number_of_reviews_ltm', 'number_of_reviews_l30d', 'first_review',
       'last_review', 
       ]

df = df.drop(columns=cols)
df.dropna(inplace=True)

df['above_3_stars'] = np.where(df['review_scores_rating'] > 3, 1,0)

# df.info()
# print(df['review_scores_rating'].mean())
# print(df.isna().sum())

# px.set_mapbox_access_token(open(".mapbox_token").read())

