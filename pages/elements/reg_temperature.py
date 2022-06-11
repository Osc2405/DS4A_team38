import dash
from dash import dcc,html
import dash_bootstrap_components as dbc

from app import app

## Layout national
layout=html.Div(
    children=[
        html.H1(
            children="Temperatura regional"
        ),
        html.P("Pagina para mostrar la temperatura regional",
        className="text-justify")
    ]
)