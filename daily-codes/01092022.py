from distutils.log import debug
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame({
    'Food': ['Curry', 'Sadza', 'Muriwo', 'Pumpkin'],
    'Price': [5, 3, 8, 10],
    'ID': ['Yum', 'Wow', 'Yum', 'Wow']
})

fig = px.bar(df, x='Food', y='Price', color='ID', barmode='group')

app.layout = html.Div(children=[
    html.H1(children='Hi!'),
    html.Div(children='Web app.'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)