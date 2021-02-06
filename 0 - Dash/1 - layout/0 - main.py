import json

import dash

# Contains high-level interactive components
# and generated using React.js library
import dash_core_components as dcc

# Contains component for every HTML tag
import dash_html_components as html

from dash.dependencies import Input, Output
import plotly.express as px

#------------------------------------------------------
# Initialize a plotly figure
fig = px.line(
    x=["a","b","c"], y=[1,3,2], 
    title="sample figure", height=325
)

#------------------------------------------------------
# Initialize a dash application
app = dash.Dash(__name__)

# Can include external stylesheets in this way
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#------------------------------------------------------
# Specifying HTML+CSS with dash
# layour contains a tree of components
# Like the DOM tree in a webpage

# First argument to a html component is the "children"
# Which can be a string, a number, another component
# or a list of components(as below)
app.layout = html.Div([
    # Render the graph(usually in a "div") with id "graph"
    # Uses a high-level React component "Graph" to render the figure
    # instead of handcrafting html
    dcc.Graph(id="graph", figure=fig),
    
    # Render a html "pre" tag with "id" and "style"
    # This is handcrafted html
    # NOTE - unlike plain-css styles, the keys of styles are
    # in camelCase (to comply with React.js requirement)
    html.Pre(
        id='structure',
        style={
            'border': 'thin lightgrey solid', 
            'overflowY': 'scroll',
            'height': '275px'
        }
    )
])

#------------------------------------------------------
# callback functions: Python functions that are automatically called 
# by Dash whenever an input component's property changes.

# Whenever an input property changes, the function wrapped by the decorator is called

# First argument to Input is "component_id" and second is "component_property"
# i.e. Call the function when "component_property" of the component with "component_id" changes

# First argument to Output is "component_id" and second is "component_property"
# i.e. pass the return value of function to the "component_property"
# of the component with id "component_id"

# This function is called when "figure" property of "graph" changes 
# The return value is passed as value of "children" property to "structure"

# More examples of callbacks and interactivity in the next programs

@app.callback(
    Output("structure", "children"), 
    [Input("graph", "figure")])
def display_structure(fig_json):
    return json.dumps(fig_json, indent=2)

# debug=True enables hot-reloading
# If you make any changes to your file and save it
# The webpage reloads with the changes
app.run_server(debug=True)

# Click on the above link to Open the plot
# Right click on the plot and click "Inspect". Compare it with the HTML specified above
# Click "Stop" at the top of this page to stop the server