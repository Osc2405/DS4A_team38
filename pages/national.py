from logging import PlaceHolder
import dash
from dash import dcc, html,Input,Output
import dash_bootstrap_components as dbc
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import pathlib
import plotly.express as px

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

from app import app

# DataSets
df_land=pd.read_csv(DATA_PATH.joinpath("landcoverFAO.csv"))
df_data=pd.read_csv(DATA_PATH.joinpath("output_merge.csv"))

temperature=df_data["Temperature"].iloc[-1]
Forest_area=df_data["Forest area (sq. km)"].iloc[-1]
renewables=df_data["renewables_consumption"].iloc[-1]
cattle=df_data["Cattle"].iloc[-1]


#fig = px.pie(df_land,values="Value", names="Item")

#fig = px.line(df_land, x='Year', y='Value', markers=True,color='Item')
#fig.update_layout(showlegend=False)
#fig.update_layout(legend=dict(
#    orientation="h",
#    yanchor="bottom",
#    y=1.02,
#    xanchor="right",
#    x=1
#))


#fig = sns.relplot(data=df, x = "Year", y = "Value", kind = "line", hue = "Item")


# Layout national
layout = html.Div(
    children=[
        html.Div(className=" p-3 m-2",children=[
            html.H1(
            children="National page", className="me-md-3 me-xl-5 text-center"
            ),
            html.P(id="parrafo", className="text-success text-center"),
        ]),
        
        dcc.RangeSlider(id="year_slider",
                        min=df_land["Year"].min(), max=df_land["Year"].max(),step=None,value=[df_land["Year"].min(),df_land["Year"].max()],marks={int(i):str(i) for i in df_land["Year"].unique()}, className="pt-4 pb-5"),
        dbc.Container([
            html.Div(className="card-body border rounded p-3",children=[
                html.H3("Data from the most recent year (2020):", className="text-center"),
            html.Div(className="d-flex flex-wrap justify-content-xl-between",children=[
                html.Div(className="d-none d-xl-flex border-md-right flex-grow-1 align-items-center justify-content-center p-3 item",children=[
                    html.I(className="fs-5 bi-cloud me-3 text-warning"),
                    html.Div(className="d-flex flex-column justify-content-around",children=[
                        html.Small("Temperature",className="mb-1 text-muted"),
                        html.H5(f'{temperature} °K',className="me-2 mb-0",id="temp_data")
                    ])

                ]),
                html.Div(className="d-none d-xl-flex border-md-right flex-grow-1 align-items-center justify-content-center p-3 item",children=[
                    html.I(className="fs-5 bi-tree-fill me-5 text-success"),
                    html.Div(className="d-flex flex-column justify-content-around",children=[
                        html.Small("Forest area",className="mb-1 text-muted"),
                        html.H5(f'{Forest_area} sq km',className="me-2 mb-0",id="CO2_data")
                    ])

                ]),
                html.Div(className="d-none d-xl-flex border-md-right flex-grow-1 align-items-center justify-content-center p-3 item",children=[
                    html.I(className="fs-5 bi-battery-charging me-3 text-primary"),
                    html.Div(className="d-flex flex-column justify-content-around",children=[
                        html.Small("Renewable energy",className="mb-1 text-muted"),
                        html.H5(renewables,className="me-2 mb-0",id="population_data")
                    ])

                ]),
                html.Div(className="d-none d-xl-flex border-md-right flex-grow-1 align-items-center justify-content-center p-3 item",children=[
                    html.I(className="fs-5 bi-exclamation-octagon-fill me-3 text-danger"),
                    html.Div(className="d-flex flex-column justify-content-around",children=[
                        html.Small("Livestock",className="mb-1 text-muted"),
                        html.H5(cattle,className="me-2 mb-0",id="cattle_data")
                    ])

                ]),
            ]),
            ]),
            # First row
            html.Div(className="pt-3 border border-rounded",children=[

            
            dbc.Row([
                dbc.Col([
                    html.P("Comparative percentage land uses",
                           className="text-center text-success"),
                    dcc.Graph(id='LandUsePie'),
                    
                ],  # width={'size': 7, 'offset': 0, 'order': 1}),
                    xs=12, sm=12, md=12, lg=5, xl=5),
                dbc.Col([
                    html.P("Comparation between land use",
                           className="text-center text-success"),
                    dcc.Dropdown(id="land_use_drop",multi=True, placeholder="Select the types of land cover...", options=[{'label': x, 'value': x} for x in sorted(df_land['Item'].unique())]),
                    html.Div(id='table-container'),
                    dcc.Graph(id='LandUseLines'),
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
            ]),
            html.Div(className="",children=[
                html.P("Comparative between forest area and other variables", className="text-center"),
                dcc.Dropdown(id="forestvs_drop",multi=True, placeholder="Select variables to show...", options=[{'label': x, 'value': x} for x in sorted(df_data.columns[1:])]),
                dcc.Graph(id="forestvs")
            ])

            # Final Container
        ], fluid=True)
    ]
)




