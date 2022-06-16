from pydoc import classname
import dash
from dash import dcc,html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

from app import app

#Datos de ejemplo
fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])
#fig.update_layout(plot_bgcolor='#ffffff',paper_bgcolor= "#21222d")  Esta linea permite modificar el color del fondo, pero queda horrible, aunque es un inicio

## Layout national
layout=html.Div( className="seccion_home",
    children=[
        html.Header(
            className="masthead",children=[
                html.Div(className="container px-4 px-lg-5 d-flex h-100 align-items-center justify-content-center",children=[
                    html.Div(className="d-flex justify-content-center", children=[
                        html.Div(className="text-center",children=[
                            html.H1(className="mx-auto my-0 text-uppercase", children="ECO Rest"),
                            html.H2(children="Algun texto o frease introductoria",className="text-white-50 mx-auto mt-2 mb-5"),
                            html.A(className="btn btn-secondary mx-3  border border-rounded text-black", href="/tabs_national",children="Datos nacionales"),
                            html.A(className="btn btn-secondary mx-3 border border-rounded text-black", href="/tabs_regional",children="Datos regionales"),
                        ])
                    ])
                ])
            ]
        ),
        html.Section(className="seccion_home",children=[
            html.Div(className="container pt-4 pt-lg-5 text-white",children=[
                html.Div(className="row gx-0 mb-4 mb-lg-5 align-items-start pt-5 text-white justify-content-between",children=[
                    html.Div(className="col-5 text-center",children=[
                        html.H4(children="Nuestro proyecto"),
                        html.P(children="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Dictum sollicitudin condimentum nunc, lorem in lorem sit mattis. In ultrices egestas enim interdum ut tincidunt scelerisque. Orci, leo, fames duis duis et. Etiam feugiat sem porttitor odio id sit.",className="text-justify"),
                        html.Img(src="../assets/img/embrace-the-world.png",className="w-50")
                    ]),
                    html.Div(className="col-5 align-items-",children=[
                        html.H4(children="Objetivos"),
                        html.Ul(className="",children=[
                            html.Li(className="",children="Objetivo 1"),
                            html.Li(className="",children="Objetivo 2"),
                            html.Li(className="",children="Objetivo 3")
                        ]),
                    ])
                ])
            ])
        ]),
        html.Section(className="seccion_datos py-3 text-white text-center container pt-4 pt-lg-5",children=[
            html.H2("Nuestro pais en datos",className="py-3"),
            html.Div(className="row justify-content-between",children=[
                html.Div(className="col",children=[
                    html.H4("Temperatura",className="py-3"),
                    dcc.Graph(figure=fig)
                ]),
                html.Div(className="col",children=[
                    html.H4("Bosques",className="py-3"),
                    dcc.Graph(figure=fig)
                ]),
                html.Div(className="col",children=[
                    html.H4("Poblacion",className="py-3"),
                    dcc.Graph(figure=fig)
                ])
            ]),
            html.Div(className="text-center py-5",children=[
                html.H2(children="Revisa nuestros datos",className="text-white-50 mx-auto mt-2 mb-5"),
                html.A(className="btn btn-secondary mx-3  border border-rounded text-black", href="/tabs_national",children="Datos nacionales"),
                html.A(className="btn btn-secondary mx-3 border border-rounded text-black", href="/tabs_regional",children="Datos regionales"),
            ])
        ])

    ]
)