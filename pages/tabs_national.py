import dash
from dash import dcc,html
import dash_bootstrap_components as dbc

from app import app

layout = html.Div([
    dcc.Tabs(id="tabs_national", value='tab_temperature', children=[
        dcc.Tab(label='Temperatura', value='tab_temperature'),
        dcc.Tab(label='Deforestacion', value='tab_eforestation'),
    ]),
    html.Div(id='content_national')
])