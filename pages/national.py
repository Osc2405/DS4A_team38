import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

from app import app

# DataSets

# Layout national
layout = html.Div(
    children=[
        html.H1(
            children="National page", className="text-center text-success , mb-4"
        ),
        dbc.Container([

            # First row
            dbc.Row([
                dbc.Col([
                    html.P("Comparative percentage land uses",
                           className="text-center text-success"),
                    dcc.Graph(id='PiechartLandUsesReg', figure={}),
                ],  # width={'size': 7, 'offset': 0, 'order': 1}),
                    xs=12, sm=12, md=12, lg=5, xl=5),
                dbc.Col([
                    html.P("Relation between forest and other factors by amount (standarized)",
                           className="text-center text-success"),
                    dcc.Graph(id='LineChartForestAndFactors', figure={}),
                    # dcc.Dropdown(id='dpdnFactors', multi=False, value='Forest', options=[{'label': x, 'value': x} for x in sorted(df['data'].unique())])
                ],  # width={'size': 5, 'offset': 0, 'order': 1} #with this we can describe the size of the column
                    xs=12, sm=12, md=12, lg=5, xl=5  # columns according to the size
                )
            ], justify='around'),

            # Second row

            dbc.Row([
                dbc.Col([
                    html.P("Comparative percentage land uses",
                           className="text-center text-success"),
                    dcc.Graph(id='PiechartLandUsesReg', figure={}),
                ], width={'size': 4, 'offset': 0, 'order': 1}),
                dbc.Col([
                    html.P("Relation between forest and other factors by amount (standarized)",
                           className="text-center text-success"),
                    dcc.Graph(id='LineChartForestAndFactors', figure={}),
                    # dcc.Dropdown(id='dpdnFactors', multi=False, value='Forest', options=[{'label': x, 'value': x} for x in sorted(df['data'].unique())])
                ], width={'size': 4, 'offset': 0, 'order': 1}),
                dbc.Col([
                    html.P("Comparative percentage land uses",
                           className="text-center text-success"),
                    dcc.Graph(id='PiechartLandUsesReg', figure={}),
                ], width={'size': 4, 'offset': 0, 'order': 1}),

            ], justify='around'),

            # Final Container
        ], fluid=True)
    ]
)
