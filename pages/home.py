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
    columns={'Value': 'Tree cover Area'})
Land_cover_1['Tree cover Area'] = Land_cover_1['Tree cover Area'].round(2)
fig = px.line(Land_cover_1, x='Year', y='Tree cover Area',
              markers=True)


# Layout national
layout = html.Div(
    children=[
        html.H1(
            children="Home page", className="text-center text-success , mb-4"
        ),

        dbc.Container([

            # First row
            dbc.Row([
                dbc.Col([
                    html.P("Our interest is focusing on the relation between several factors which could lead to the vast deforestation in Colombia. According to differents datasets, we explore information and look for some connection between them and the impact that it has with enviroment.",
                           className="text-justify text-success"),
                    dcc.Graph(id='LineChartForest', figure=fig),

                ],  # width={'size': 7, 'offset': 0, 'order': 1}),
                    xs=12, sm=12, md=12, lg=11, xl=11),
            ], justify='around'),

            # Button to show table
            dbc.Card([
                dbc.CardBody([
                    dbc.Button("Show table and datasets information",
                               color="success", className="me-1"),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            dbc.Table.from_dataframe(
                                Land_cover_1, striped=True, bordered=True, hover=False),
                        ]),
                        dbc.Col([
                            dbc.Card(
                                dbc.CardBody([
                                    html.P(
                                        "Since 1990 the amount of forest covering has been decreasing along the year, we are also interesting in studying which effects deforestation could be correlated with other phenomenum as the weather or the the increase in polluting emissions. ", className="text-justify text-success"),
                                ]),
                            ),
                            dbc.Card([
                                dbc.CardBody([
                                    html.P(
                                        "The datasets where extracted from differents resources the previous data was taken from https://www.fao.org/faostat/en/#data/LC ", className="text-justify text-success"),
                                ]),
                            ]),
                        ]),
                    ]),

                ])
            ], color="secondary", outline=True, inverse=True),

            dbc.Row([
                dbc.Col([
                    html.P("The problem of polution emissions is other problem that we have to take care, in order to give a brief view we are going to posed the increasing change of this emissions.",
                           className="text-justify text-success"),
                    dcc.Graph(id='LineChartForest', figure={}),

                ],  # width={'size': 7, 'offset': 0, 'order': 1}),
                    xs=12, sm=12, md=12, lg=11, xl=11),
            ], justify='around'),

            # Final Container
        ], fluid=True),




        # dbc.Container([
        #     dbc.Button(
        #         "Toggle fade", id="fade-button", className="mb-3", n_clicks=0
        #     ),
        #     dbc.Fade(
        #         dbc.Card(
        #             dbc.CardBody(
        #                 html.P(
        #                     "This content fades in and out", className="card-text"
        #                 )
        #             )
        #         ),
        #         id="fade",
        #         is_in=True,
        #         appear=False,
        #     ),
        # ]),

    ]
)

# Callbacks


# @app.callback(
#     Output("fade", "is_in"),
#     [Input("fade-button", "n_clicks")],
#     [State("fade", "is_in")],
# )
# def toggle_fade(n, is_in):
#     if not n:
#         # Button has never been clicked
#         return False
#     return not is_in
