import json

import dash

# Contains high-level interactive components
# and generated using React.js library
from dash import dcc

# Contains component for every HTML tag
from dash import html

from dash.dependencies import Input, Output
import plotly.express as px

#------------------------------------------------------
# Initialize a plotly figure
fig = px.line(
    x=range(1, 13), y=[1, 3, 2, 5, 3, 4, 6, 8, 7, 9, 3, 5],
    title="Demo Chart", height=625, width=1000
)

#------------------------------------------------------
# Initialize a dash application
app = dash.Dash(__name__)

# Can include external stylesheets in this way
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#------------------------------------------------------
# Specifying HTML+CSS with dashcomponents
# layour contains a tree of
# Like the DOM tree in a webpage

# First argument to a html component is the "children"
# Which can be a string, a number, another component
# or a list of components(as below)
app.layout = html.Div([
    # Render the graph(usually in a "div") with id "graph"
    # Uses a high-level React component "Graph" to render the figure
    # instead of handcrafting html
    dcc.Graph(id="graph", figure=fig),

])

# debug=True enables hot-reloading
# If you make any changes to your file and save it
# The webpage reloads with the changes
app.run_server(debug=True)

# Click on the above link to Open the plot
# Right click on the plot and click "Inspect". Compare it with the HTML specified above
# Click "Stop" at the top of this page to stop the server
