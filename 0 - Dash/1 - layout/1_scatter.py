import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# sample dataset for GDP and life expectancy
data_source = 'https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv'
df = pd.read_csv(data_source)


# generate a figure using plotly
# Note that we are directly using a pandas dataframe to generate the plot
fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60, height=625, width=1500)


# add this figure to the html and render it using dash
app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])


# start the server
if __name__ == '__main__':
    app.run_server(debug=True)
