import dash
from dash import dcc,html
import dash_bootstrap_components as dbc

from app import app

## Layout national
layout=html.Div(
    children=[
        html.H1(
            children="National page"
        )
    ]
)