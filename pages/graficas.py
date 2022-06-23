import dash
from dash import Input, Output, dcc, html,State, callback
import dash_bootstrap_components as dbc

from app import app


## Layout national
layout=html.Div(className="seccion_home px-4",
    children=[
        html.H1(className="pt-4 text-center text-white",
            children="Graficas"
        ),
        #EXAMPLE FOR  CALLBACKS
        html.P("Pagina para resumir graficas que podriamos usar a futuro",
        className="pt-4 text-justify text-white"),
        html.H6("Change the value in the text box to see callbacks in action!"),
        html.Div([
            "Input: ",
            dcc.Input(id='my-input', value='initial value', type='text')
        ]),
        html.Br(),
        html.Div(id='my-output'),
    ]
)

#CALLBACKS GRAFICAS

@callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'
