import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import pathlib

from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

LandCover = pd.read_csv(DATA_PATH.joinpath("LandCover.csv"))

# Plot Tree-covered areas
Land_cover = LandCover[["Domain", "Element", "Item", "Year", "Unit", "Value"]]
Land_cover = Land_cover[Land_cover["Element"] == "Area from CCI_LC"]
Land_cover = Land_cover[Land_cover["Item"].isin(
    ["Grassland", "Tree-covered areas", "Mangroves", "Shrub-covered areas", "Sparsely natural vegetated areas"])]
Land_cover_1 = Land_cover.groupby(["Year"])["Value"].sum().reset_index()
Land_cover_1 = pd.DataFrame(Land_cover_1).rename(
    columns={'Value': 'Land_Cover'})
fig = px.line(Land_cover_1, x='Year', y='Land_Cover', markers=True)

# Layout national
layout = html.Div(
    children=[
        html.H1(
            children="Home page"
        ),

        html.P("Our interest are focusing on the relation between several factors which could lead to a vast deforestation in Colombia",
               className="text-justify"),
        dcc.Graph(id='LineChartForest', figure=fig),

        # Button to show table
        dbc.Container([
            dbc.Button(
                "Toggle fade", id="fade-button", className="mb-3", n_clicks=0
            ),
            dbc.Fade(
                dbc.Card(
                    dbc.CardBody(
                        html.P(
                            "This content fades in and out", className="card-text"
                        )
                    )
                ),
                id="fade",
                is_in=True,
                appear=False,
            ),
        ]),

    ]
)


# Callbacks
@app.callback(
    Output("fade", "is_in"),
    [Input("fade-button", "n_clicks")],
    [State("fade", "is_in")],
)
def toggle_fade(n, is_in):
    if not n:
        # Button has never been clicked
        return False
    return not is_in
