import dash
from dash import dcc,html
import dash_bootstrap_components as dbc
import pathlib
import pandas as pd

from app import app


# Cambiar
# Hay que cambiar esto para usar los datasets del github
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

# DataSets
df_land=pd.read_csv(DATA_PATH.joinpath("landcoverFAO.csv"))
df_data=pd.read_csv(DATA_PATH.joinpath("output_merge.csv"))


df_finalCSV='https://raw.githubusercontent.com/ajrianop/projectDS4A/main/df_final.csv'
df=pd.read_csv(df_finalCSV,encoding='unicode_escape')

temperature=df_data["Temperature"].iloc[-1]
Forest_area=df_data["Forest area (sq. km)"].iloc[-1]
renewables=df_data["renewables_consumption"].iloc[-1]
cattle=df_data["Cattle"].iloc[-1]

## End Cambiar

## Layout national
layout=html.Div(className="seccion_home px-4",
    children=[
        html.H1(className="pt-4 text-center text-white",children="Seccion descriptiva"),
        html.Section(className="text-center text-white",id="filtros-mapa", children=[
            html.Div(className="row text-center pt-5", children="Espacio para el mapa"),
            html.Div(className="row pt-5",children=[
                html.H4(className="py-2",children="Selecciona el rango de años que quieres observar"),
                dcc.RangeSlider(id="year_slider_d", min=df["Year"].min(), max=df["Year"].max(),step=1,value=[df["Year"].min(),df["Year"].max()],marks=None, className="pt-4 pb-5",tooltip={"placement": "bottom", "always_visible": True}),
        ])
        ]),
        
        # Indicadores
        html.Section(className="container text-white",children=[
            html.Div(className="card-body border rounded p-3",children=[
                html.H3("Datos del año mas reciente (2020):", className="text-center text-white", id="text_year"),
            html.Div(className="d-flex flex-wrap justify-content-xl-between container",children=[
                html.Div(className="d-none d-xl-flex border-md-right flex-grow-1 align-items-center justify-content-center p-3 item indicador m-3 border border-light rounded",children=[
                    html.I(className="fa-solid fa-temperature-half fa-xl me-3  text-warning"),
                    html.Div(className="d-flex flex-column justify-content-around",children=[
                        html.Small("Temperatura",className="mb-1 text-muted"),
                        html.H5(className="me-2 mb-0", id="indicador_temperatura")
                    ])

                ]),
                html.Div(className="d-none d-xl-flex border-md-right flex-grow-1 align-items-center justify-content-center p-3 item indicador m-3  border border-light rounded",children=[
                    html.I(className="fa-solid fa-smog fa-xl me-3 text-primary "),
                    html.Div(className="d-flex flex-column justify-content-around",children=[
                        html.Small("CO2",className="mb-1 text-muted"),
                        html.H5(className="me-2 mb-0",id="indicador_co2")
                    ])

                ]),
                html.Div(className="d-none d-xl-flex border-md-right flex-grow-1 align-items-center justify-content-center p-3 item indicador m-3  border border-light rounded",children=[
                    html.I(className="fa-solid fa-tree fa-xl me-3 text-success"),
                    html.Div(className="d-flex flex-column justify-content-around",children=[
                        html.Small("Cobertura de bosque",className="mb-1 text-muted"),
                        html.H5(className="me-2 mb-0",id="indicador_forest")
                    ])

                ]),
                html.Div(className="d-none d-xl-flex border-md-right flex-grow-1 align-items-center justify-content-center p-3 item indicador m-3  border border-light rounded",children=[
                    html.I(className="fa-solid fa-people-group fa-xl me-3 text-danger"),
                    html.Div(className="d-flex flex-column justify-content-around",children=[
                        html.Small("Poblacion",className="mb-1 text-muted"),
                        html.H5(className="me-2 mb-0",id="indicador_poblacion")
                    ])

                ]),
            ]),
            ]),
        ]),

        ## Espacio para variable importante con texto un solo grafico
        html.Section(className="pt-5 text-white",children=[
            html.Div(className="row",children=[
                html.Div(className="col-xl-4 col-md-4 col",children=[
                    html.H5(className="",children="Variable importante 1"),
                    html.P(className="text-justify",children="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
                    dcc.Dropdown(id="contamination_drop",multi=True, placeholder="Selecciona un gas de efecto infernadero...", options=[{'label': x, 'value': x} for x in ["coal_consumption", "gas_consumption","oil_consumption", "renewables_consumption"]]),
                ]),
                html.Div(className="col text-center",children=[
                    dcc.Graph(id="indicador_barras",figure={})
                ])
            ])
        ]),


        html.Section(className="pt-3 text-white",children=[
            html.Div(className="row",children=[
                html.Div(className="col text-center",children=[
                    dcc.Graph(id="plot_area_contaminacion",figure={})
                ]),
                html.Div(className="col text-center",children=[
                    dcc.Graph(id="plot_area_poblacion",figure={})
                ])
            ]),
        ]),

    ]
)

