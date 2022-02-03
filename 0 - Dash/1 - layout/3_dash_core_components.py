import dash
from dash import dcc
from dash import html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


"""
This example highlights some of the most common user input elements that can be directly
defined in Python using the "Core Components" provided in Dash.
"""


app.layout = html.Div([

    # A dropdown menu
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],

        # default value of the dropdown is set to MTL (Montreal) initially
        value='MTL'
    ),


    # Select multiple elements using a multi-select dropdown
    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],

        # default values which are set initially
        value=['MTL', 'SF'],
        multi=True
    ),

    # Radio button
    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],

        # default value
        value='MTL'
    ),


    # Simple Checkbox
    html.Label('Checkboxes'),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],

        # and its default value
        value=['MTL', 'SF']
    ),


    # Text input
    html.Label('Text Input'),
    dcc.Input(value='MTL', type='text'),


    # Single range slider
    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i)
               for i in range(1, 10)},

        # default value
        value=5,
    ),
], style={'columnCount': 2})


# run the server
if __name__ == '__main__':
    app.run_server(debug=True)
