import dash
from dash import dcc,html
import dash_bootstrap_components as dbc

from app import app

## Layout national
layout=html.Div(
    children=[
        html.H1(
            children="About page"
        ),
        html.P("We are interested in seraching which are the main problems of deforestation in Colombia. Here we can see explicitly the changes along each year since 1990 to 2020",
        className="text-justify")
    ]
)