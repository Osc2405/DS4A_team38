import dash
from dash import dcc,html
import dash_bootstrap_components as dbc

from app import app

layout = html.Div([
    dcc.Tabs(id="tabs_regional", value='tab_temperature_reg', children=[
        dcc.Tab(label='Temperatura', value='tab_temperature_reg'),
        dcc.Tab(label='Deforestacion', value='tab_eforestation_reg'),
    ]),
    html.Div(id='content_regional')
])