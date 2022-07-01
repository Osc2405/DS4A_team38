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
layout = html.Div(className="seccion_home px-4 pt-5",
    children=[
        html.H1("AAAAAAAA", className="text-white")

    ]
)




