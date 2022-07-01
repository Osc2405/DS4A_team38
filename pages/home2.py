from pydoc import classname
import dash
from dash import dcc,html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

from app import app

#Datos de ejemplo
fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])
#fig.update_layout(plot_bgcolor='#ffffff',paper_bgcolor= "#21222d")  Esta linea permite modificar el color del fondo, pero queda horrible, aunque es un inicio


# DF final# DF Final
df_finalCSV='https://raw.githubusercontent.com/ajrianop/projectDS4A/main/df_final.csv'
df=pd.read_csv(df_finalCSV,encoding='unicode_escape')

# Grafica temperatura
fig_temp=px.line(df,x=df["Year"],y=["Temperature"], template = 'plotly_dark',
                  labels={
                     "value": "Temperatura (Celcius)",
                     "variable": ""
                    },width=400, height=400,)
fig_temp.update_traces(line=dict(color='#FF0000', width=5))

# Set x-axis title and range
fig_temp.update_xaxes(title_text="Año")
fig_temp.update_xaxes(range=(1990,2020))

# Set y-axes titles
fig_temp.update_yaxes(title_text="Temperatura (Celcius)")

# Leyenda arriba de gráfica
fig_temp.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))

# Letras en blanco y estilo de color de gráfica
fig_temp.update_layout({
  "plot_bgcolor": "#111111",
  "paper_bgcolor": "#111111",
  "font_color":"white",
  "title_font_color":"white"
})



### Figura landcover
fig_landcover = px.line(df, 
             x = "Year",
             y = ["Forest area", "Agricultural land"],
             template = 'plotly_dark',
             #title = 'Uso de tierra (Hectareas)',
              width=400, height=400,
              labels={"variable": ""
                    }
             )


fig_landcover.update_layout(yaxis_range=[0,700000])

# Leyenda arriba de gráfica
fig_landcover.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))


fig_landcover.update_traces(line_width=5)
# Set x-axis title and range
fig_landcover.update_xaxes(title_text="Año")
fig_landcover.update_xaxes(range=(1990,2020))

# Set y-axes titles
fig_landcover.update_yaxes(title_text="Hectareas")

# Letras en blanco y estilo de color de gráfica
fig_landcover.update_layout({
  "plot_bgcolor": "#111111",
  "paper_bgcolor": "#111111",
  "font_color":"white",
  "title_font_color":"white"
})


### Figura poblacion
fig_poblacion = px.bar(df, 
             x = "Year",
             y = ["Urban population", "Rural population"],
             template = 'plotly_dark',
             #title = 'Población', width=400, height=400, 
             labels={"variable": ""
                    }
             )
fig_poblacion.add_trace(
    go.Scatter(x=df["Year"], y=df["population"], name="Población total",hoveron='points'),
    
)

# Leyenda arriba de gráfica
fig_poblacion.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
fig_poblacion.update_layout({
    "plot_bgcolor": "#111111",
    "paper_bgcolor": "#111111",
    })

# Set x-axis title and range
fig_poblacion.update_xaxes(title_text="Año")
fig_poblacion.update_xaxes(range=(1990,2020))

# Set y-axes titles
fig_poblacion.update_yaxes(title_text="Número de habitantes")



## Layout national
layout=html.Div( className="seccion_home",
    children=[
    html.Div(className="header_img",children=[
        html.Header(
            className="masthead",children=[
                html.Div(className="container px-4 px-lg-5 d-flex h-100 align-items-center justify-content-center",children=[
                    html.Div(className="d-flex justify-content-center", children=[
                        html.Div(className="text-center",children=[
                            html.H1(className="mx-auto my-0 text-uppercase", children="ECO Temp"),
                            html.H2(children="Team 30 - DS4A Colombia",className="text-white-50 mx-auto mt-2 mb-5"),
                            #html.A(className="btn btn-secondary mx-3  border border-rounded text-black", href="/prediction",children="Predicción de temperatura"),
                            #html.A(className="btn btn-secondary mx-3 border border-rounded text-black", href="/description",children="Ver datos hasta la fecha"),
                            html.A(className="btn btn-secondary mx-3 border border-rounded text-black my-2", href="/prediction",children=[dbc.NavLink(className="text-black",children="Predicción de temperatura", href="/prediction", active="exact"),]),
                            html.A(className="btn btn-secondary mx-3 border border-rounded text-black my-2", href="/description",children=[dbc.NavLink(className="text-black",children="Ver datos hasta la fecha", href="/description", active="exact"),]),

                        ])
                    ])
                ])
            ]
        ),
        ]),
        html.Section(className="seccion_home container-fluid",children=[
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


        # Section nuestro pais en datos
        html.Section(className="seccion_datos py-3 text-white text-center pt-4 px-3 pt-lg-5  container-fluid",children=[
            html.H2("Nuestro pais en datos",className="py-3"),
            html.Div(className="row",children=[
                html.Div(className="col-md-4 pais_datos",children=[
                    html.H4("Temperatura",className="py-3"),
                    dcc.Graph(figure=fig_temp)
                ]),
                html.Div(className="col-md-4 pais_datos",children=[
                    html.H4("Bosques",className="py-3"),
                    dcc.Graph(figure=fig_landcover)
                ]),
                html.Div(className="col-md-4 pais_datos",children=[
                    html.H4("Poblacion",className="py-3"),
                    dcc.Graph(figure=fig_poblacion)
                ])
            ])
        ]),

        html.Section(className="seccion_datos py-3 text-white text-center container pt-4 pt-lg-5",children=[
                html.Div(className="text-center py-5",children=[
                html.H2(children="Revisa nuestros datos",className="text-white mx-auto mt-2 mb-5"),
                html.A(className="btn btn-secondary mx-3 border border-rounded text-black", href="/prediction",children=[dbc.NavLink(className="text-black",children="Predicción de temperatura", href="/prediction", active="exact"),]),
                html.A(className="btn btn-secondary mx-3 border border-rounded text-black", href="/description",children=[dbc.NavLink(className="text-black",children="Ver datos hasta la fecha", href="/description", active="exact"),]),
            ])
        ])

    ]
)