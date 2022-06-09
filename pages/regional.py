import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

from app import app

# Layout national
layout = html.Div(
    children=[
        html.H1(
            children="Regional page", className="text-center text-success , mb-4"
        )
    ]
)
