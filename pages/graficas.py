import dash
from dash import dcc,html
import dash_bootstrap_components as dbc

from app import app

## Layout national
layout=html.Div(
    children=[
        html.H1(
            children="Graficas"
        ),
        html.P("Pagina para resumir graficas que podriamos usar a futuro",
        className="text-justify")
    ]
)