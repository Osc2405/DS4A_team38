import dash
from dash import dcc,html, callback,Input, Output,State
import dash_bootstrap_components as dbc
import pathlib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from app import app

import json
from pandas import json_normalize
from pandas.io.json import json_normalize


#MAPA COLOMBIA
from components.maps.mapcol_departamentos import mapcol_departamentos
# dataset de prueba para el mapa
#datatest1=departments.to_json()
#print(datatest)

datatest ={"COD_DPTO":{"0":"05","1":"08","2":"11","3":"13","4":"15","5":"17","6":"18","7":"19","8":"20","9":"23","10":"25","11":"27","12":"41","13":"44","14":"47","15":"50","16":"52","17":"54","18":"63","19":"66","20":"68","21":"70","22":"73","23":"76","24":"81","25":"85","26":"86","27":"91","28":"94","29":"95","30":"97","31":"99","32":"88"},"DEPARTAMENTO":{"0":"ANTIOQUIA","1":"ATLANTICO","2":"SANTAFE DE BOGOTA D.C","3":"BOLIVAR","4":"BOYACA","5":"CALDAS","6":"CAQUETA","7":"CAUCA","8":"CESAR","9":"CORDOBA","10":"CUNDINAMARCA","11":"CHOCO","12":"HUILA","13":"LA GUAJIRA","14":"MAGDALENA","15":"META","16":"NARI\\u00d1O","17":"NORTE DE SANTANDER","18":"QUINDIO","19":"RISARALDA","20":"SANTANDER","21":"SUCRE","22":"TOLIMA","23":"VALLE DEL CAUCA","24":"ARAUCA","25":"CASANARE","26":"PUTUMAYO","27":"AMAZONAS","28":"GUAINIA","29":"GUAVIARE","30":"VAUPES","31":"VICHADA","32":"ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA"},"COUNT":{"0":525,"1":1193,"2":1518,"3":1839,"4":1541,"5":1676,"6":1864,"7":1096,"8":1652,"9":1131,"10":819,"11":1061,"12":1972,"13":1045,"14":739,"15":1057,"16":1269,"17":1708,"18":1948,"19":1525,"20":1743,"21":1441,"22":802,"23":1960,"24":792,"25":994,"26":1637,"27":682,"28":1352,"29":1173,"30":1115,"31":1151,"32":1758},"latitude":{"0":8.6192998894,"1":10.3612003326,"2":4.7951002121,"3":10.4236001975,"4":7.0275001523,"5":5.7526998521,"6":2.4978001119,"7":2.9751138688,"8":10.8562469488,"9":9.4230003359,"10":5.7488999368,"11":8.2716999057,"12":3.2739000325,"13":12.4235000614,"14":11.3276996617,"15":4.4449000365,"16":2.5773999689,"17":9.1339998247,"18":4.6946001053,"19":5.4751377105,"20":8.1150255208,"21":9.8849000932,"22":5.2814002036,"23":4.9735999108,"24":7.0592999452,"25":6.2479000086,"26":1.3164000513,"27":0.1186000023,"28":3.8605000963,"29":2.8375000958,"30":1.9852999444,"31":6.2795000082,"32":12.5945628115},"longitude":{"0":-76.3072967522,"1":-74.8705978394,"2":-74.0229034424,"3":-75.1595001224,"4":-72.2129974372,"5":-74.6949996949,"6":-74.6925964365,"7":-78.2116241452,"8":-73.2823181155,"9":-75.8195037842,"10":-74.3295974737,"11":-77.0213012688,"12":-74.6360015871,"13":-71.6212005615,"14":-74.0917968755,"15":-71.0799026493,"16":-77.9835968017,"17":-73.0177993776,"18":-75.6720962525,"19":-75.886505127,"20":-73.8001403806,"21":-75.4831008914,"22":-74.8399963373,"23":-76.0838012692,"24":-70.6986999517,"25":-70.17250061,"26":-76.5781021113,"27":-71.3863983161,"28":-67.687797549,"29":-71.2646026619,"30":-70.112998962,"31":-67.7968978901,"32":-81.7129569648}}

df_maptest = pd.DataFrame.from_dict(datatest)  
mapa_colombia_departamentos = mapcol_departamentos('Mapa Departamentos Colombia', 'div_municipios_fig2',df_maptest)

departamentosCSV='https://raw.githubusercontent.com/ajrianop/projectDS4A/main/department.csv'
departamentos=pd.read_csv(departamentosCSV,encoding='unicode_escape')
departamentos=departamentos.DEPARTAMENTO.unique()

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
        html.H1(className="pt-4 text-center text-white pb-5",children="Seccion descriptiva"),
        html.Section(className="text-white row pb-5",id="filtros-mapa", children=[

            html.Div(className="col-xs-12 col-sm-12 col-md-6 col-xl-6 pt-3",children=[
                html.H4(className="py-2 text-center",children="Filtros"),
                html.H5(className="py-2",children="Selecciona el rango de años a observar:"),
                dcc.RangeSlider(id="year_slider_d", min=df["Year"].min(), max=df["Year"].max(),step=1,value=[df["Year"].min(),df["Year"].max()],marks=None, className="pt-4 pb-5",tooltip={"placement": "bottom", "always_visible": True}),
                html.H5("Selecciona un departamento", className="pt-3 pb-2"),
                dcc.Dropdown(id="departamentos_drop",multi=False, placeholder="Selecciona un departamento...", options=[{'label': x, 'value': x} for x in departamentos]),
            ]),


            html.Div(className="col-xs-12 col-sm-12 col-md-6 col-xl-6 text-center pt-3", children=[
                html.Div(className="seccion_home px-4",
                    children=[
                        html.Div(id='my-output',children=[
                            html.Div([
                                    mapa_colombia_departamentos.display()  
                                ],className="container", id="row_map") 
                        ])
                    ])
                ])
            ]),
        html.Div(id="contenido")
    ]
)

## START CALLBACKS DESCRIPTION ##

@callback(
    Output("contenido","children"),
    Input("departamentos_drop","value"),
    [Input("year_slider_d","value")]
    )
def cambio_contenido(value,year):
    if not value:
        variables=["coal_consumption", "gas_consumption","oil_consumption", "renewables_consumption"]
        df_barras=df[(df["Year"]>=year[0]) & (df["Year"]<=year[1])]
        fig = px.bar(df_barras, 
                 x = "Year",
                 y = variables,
                 template = 'plotly_dark'
            )
        fig2 = px.area(df_barras, 
                 x = "Year",
                 y = variables,
                 template = 'plotly_dark'
            )

        fig3 = px.area(df_barras, 
                 x = "Year",
                 y = ["Urban population", "Rural population"],
                 template = 'plotly_dark'
            )

        for figura in [fig,fig2,fig3]:
            figura.update_layout(transition_duration=500)
            figura.update_layout(showlegend=False)
            figura.update_layout({
              "plot_bgcolor": "#040d10",
              "paper_bgcolor": "#040d10",
            })
        last_year=int(df_barras.iloc[-1]['Year'])
        texto_year=f'Datos del año mas reciente ({last_year})'

        #Indicadores
        texto_temp="{:.2f} °C".format((df_barras.iloc[-1]["Temperature"]))
        texto_co2="{:.2f} KT".format((df_barras.iloc[-1]["co2"]))
        texto_forest="{:.2f} Ha".format((df_barras.iloc[-1]["Forest area"]))
        texto_poblacion="{:.2f} Millones".format((df_barras.iloc[-1]["population"])/1000000)
        
        ## Graficos seccion final
        ## Energy cosumption
        fig_energy = px.bar(df_barras, 
                 x = "Year",
                 y = ["coal_consumption", "gas_consumption","oil_consumption", "renewables_consumption"],
                 template = 'plotly_dark',
                 title = 'Consumo de energía', 
                 )
        fig_energy.add_trace(
            go.Scatter(x=df_barras["Year"], y=df_barras["primary_energy_consumption"], name="Consumo de energía primaria",hoveron='points'),
        )

        fig_energy.update_layout(yaxis_range=[0,600])

        # Set x-axis title
        fig_energy.update_xaxes(title_text="Año")

        # Set y-axes titles
        fig_energy.update_yaxes(title_text="Consumo de energía (tWh)")

        # Leyenda arriba de gráfica
        

        # Letras en blanco y estilo de color de gráfica
        fig_energy.update_layout({
          "plot_bgcolor": "#040d10",
          "paper_bgcolor": "#040d10",
          "font_color":"white",
          "title_font_color":"white"
        })

        ##! Gas emissions ##

        fig_gas = px.bar(df_barras, 
                 x = "Year",
                 y = ["co2", "methane", "nitrous_oxide"],
                 template = 'plotly_dark',
                 title = 'Emisión de gases efecto invernadero',  
                 )
        fig_gas.add_trace(
            go.Scatter(x=df_barras["Year"], y=df_barras["total_ghg"], name="Total Greenhouse Gasses",hoveron='points'),
            
        )

        # Set x-axis title
        fig_gas.update_xaxes(title_text="Año")

        # Set y-axes titles
        fig_gas.update_yaxes(title_text="Emisión de gases (Kilotoneladas)")

        fig_gas.update_layout(yaxis_range=[0,300])

        # Leyenda arriba de gráfica
        

        # Letras en blanco y estilo de color de gráfica
        fig_gas.update_layout({
          "plot_bgcolor": "#040d10",
          "paper_bgcolor": "#040d10",
          "font_color":"white",
          "title_font_color":"white"
        })

        ##! Poblacion
        fig_population = px.bar(df_barras, 
                 x = "Year",
                 y = ["Urban population", "Rural population"],
                 template = 'plotly_dark',
                 title = 'Población', 
                 )
        fig_population.add_trace(
            go.Scatter(x=df_barras["Year"], y=df_barras["population"], name="Población",hoveron='points'),
            
        )

        # Leyenda arriba de gráfica
        

        # Set x-axis title
        fig_population.update_xaxes(title_text="Año")

        # Set y-axes titles
        fig_population.update_yaxes(title_text="Número de habitantes")

        # Letras en blanco y estilo de color de gráfica
        fig_population.update_layout({
          "plot_bgcolor": "#040d10",
          "paper_bgcolor": "#040d10",
          "font_color":"white",
          "title_font_color":"white"
        })

        ##! Land cover

        fig_landcover = px.line(df_barras, 
                 x = "Year",
                 y = ["Forest area", "Agricultural land"],
                 template = 'plotly_dark',
                 title = 'Uso de tierra (Hectareas)', 
                 )


        fig_landcover.update_layout(yaxis_range=[0,700000])

        # Leyenda arriba de gráfica
        
        # Letras en blanco y estilo de color de gráfica
        fig_landcover.update_layout({
          "plot_bgcolor": "#040d10",
          "paper_bgcolor": "#040d10",
          "font_color":"white",
          "title_font_color":"white"
        })

        # Set x-axis title
        fig_landcover.update_xaxes(title_text="Año")

        # Set y-axes titles
        fig_landcover.update_yaxes(title_text="Hectareas")




        layout_content=html.Div(children=[
            # Indicadores
            html.Section(className="container text-white pb-5",children=[
                html.Div(className="card-body border rounded p-3",children=[
                    html.H3(className="text-center text-white", id="text_year",children=texto_year),
                html.Div(className="d-flex flex-wrap justify-content-xl-between container",children=[
                    html.Div(className="d-none d-xl-flex border-md-right flex-grow-1 align-items-center justify-content-center p-3 item indicador m-3 border border-light rounded",children=[
                        html.I(className="fa-solid fa-temperature-half fa-xl me-3  text-warning"),
                        html.Div(className="d-flex flex-column justify-content-around",children=[
                            html.Small("Temperatura",className="mb-1 text-muted"),
                            html.H5(className="me-2 mb-0", id="indicador_temperatura",children=texto_temp)
                        ])

                    ]),
                    html.Div(className="d-none d-xl-flex border-md-right flex-grow-1 align-items-center justify-content-center p-3 item indicador m-3  border border-light rounded",children=[
                        html.I(className="fa-solid fa-smog fa-xl me-3 text-primary "),
                        html.Div(className="d-flex flex-column justify-content-around",children=[
                            html.Small("CO2",className="mb-1 text-muted"),
                            html.H5(className="me-2 mb-0",id="indicador_co2",children=texto_co2)
                        ])

                    ]),
                    html.Div(className="d-none d-xl-flex border-md-right flex-grow-1 align-items-center justify-content-center p-3 item indicador m-3  border border-light rounded",children=[
                        html.I(className="fa-solid fa-tree fa-xl me-3 text-success"),
                        html.Div(className="d-flex flex-column justify-content-around",children=[
                            html.Small("Cobertura de bosque",className="mb-1 text-muted"),
                            html.H5(className="me-2 mb-0",id="indicador_forest",children=texto_forest)
                        ])

                    ]),
                    html.Div(className="d-none d-xl-flex border-md-right flex-grow-1 align-items-center justify-content-center p-3 item indicador m-3  border border-light rounded",children=[
                        html.I(className="fa-solid fa-people-group fa-xl me-3 text-danger"),
                        html.Div(className="d-flex flex-column justify-content-around",children=[
                            html.Small("Poblacion",className="mb-1 text-muted"),
                            html.H5(className="me-2 mb-0",id="indicador_poblacion",children=texto_poblacion)
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
                        dcc.Graph(id="indicador_barras",figure=fig)
                    ])
                ])
            ]),

            ## Area dos graficas solas
            html.Section(className="pt-3 text-white",children=[
                html.Div(className="row",children=[
                    html.Div(className="col text-center",children=[
                        dcc.Graph(id="plot_area_contaminacion",figure=fig2)
                    ]),
                    html.Div(className="col text-center",children=[
                        dcc.Graph(id="plot_area_poblacion",figure=fig3)
                    ])
                ]),
            ]),

            
            ## Area graficas con texto
            html.Section(className="pt-3 text-white text-justify",children=[
                #Fila 1
                html.Div(className="row pb-5",children=[
                    html.Div(className="col-md-6",children=[
                        dcc.Graph(id="energy_consumption",figure=fig_energy)
                        ]),
                    html.Div(className="col-md-5",children=[
                        html.P(className="",children="A través de los años en Colombia el consumo de energía aumenta. La fuente de energía que más se consume es el petróleo. En 1990 esta era la fuente principal de energía, porque representaba más del 50% del consumo de energía primaria (Una fuente de energía primaria es toda forma de energía disponible en la naturaleza antes de ser convertida o transformada. Tomado de Wikipedia). Para 2019, el petróleo representa menos de la tercera parte de la energía consumida, sin embargo la cantidad neta que se consume es casi el doble de lo que se consumía en 1990. La fuente de energía que ha tenido un mayor crecimiento es el gas, dada la gasificación de servicios importantes, principalmente servicios públicos. Esta gasificación a la fecha, 2022, sigue teniendo incentivos gubernamentales por lo que se espera siga creciendo. El consumo de energía continuará aumentando en el tiempo, dado el crecimiento de población, la migración de la población de lo rural a lo urbano, entre otros factores.")
                        ]),
                    
                    ]),
                #Fila 2
                html.Div(className="row pb-5",children=[
                    html.Div(className="col-md-6",children=[
                        dcc.Graph(id="gas_consumption",figure=fig_gas)
                        ]),

                    html.Div(className="col-md-5",children=[
                        html.P(className="",children="La población colombiana ha crecido en un 152% desde 1990 hasta 2019. Pero este crecimiento se ha debido principalmente al aumento de la población en las ciudades. En 1990 la población rural representaba un 30.51% y la urbana un 69.48%. Para 2019 la población rural disminuyo a un 18.90% mientras que la urbana representaba un 81.10%. Este es un fenómeno especial dentro de los pronósticos mundiales, donde se espera que a 2050 la población urbana alcance un 68%. Colombia ya había sobrepasado este pronóstico en 1990, y esto se puede explicar por la situación social del país donde el conflicto armado y la disminución de políticas de fomento para el campo, entre otros, han propiciado la migración del campo a la ciudad. El crecimiento rápido y no planeado de ciudades aumenta la producción de gases de efecto invernadero, las islas de calor generadas por grandes áreas construidas, entre otros.")
                        ]),
                    
                    ]),
                #Fila 3
                html.Div(className="row pb-5",children=[
                    html.Div(className="col-md-6",children=[
                        dcc.Graph(id="population_graph",figure=fig_population)
                        ]),
                    html.Div(className="col-md-5",children=[
                        html.P(className="",children="Así como el consumo de energía aumenta a través de los años, también lo hace la emisión de gases de efecto invernadero, como el dióxido de carbono (CO2), Metano (CH4), Óxido nitroso (N2O), Hidrofluorocarbonos (HFC), Hexafluoruro de azufre (SF6) y Perfluorocarbonos (PFC). Estos gases contribuyen a aumentar la temperatura del planeta, porque absorben y envían radiación infrarroja desde la superficie terrestre. Además, permanecen en la atmósfera durante años, décadas o incluso siglos. Se producen en muchas actividades humanas como actividades industriales, transporte, producción agrícola, deforestación, disposición de desechos sólidos y líquidos, conversión de páramos y humedales en tierras de cultivo o actividades mineras, entre otras (www.siac.gov.co). Hasta la fecha máxima de los datos de este estudio, 2019, el gas que más se emite es el dióxido de carbono, seguido por el metano y el óxido nitroso. ")
                        ]),
                    
                    ]),
                #Fila 4
                html.Div(className="row pb-5",children=[
                    html.Div(className="col-md-6",children=[
                        dcc.Graph(id="land_cover",figure=fig_landcover)
                        ]),
                    html.Div(className="col-md-5",children=[
                        html.P(className="",children="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
                        ]),
                    
                    
                    ])
                ])

            ])
    else:
        layout_content=html.Div(className="text-center text-white", children=[
            html.H3(className="text-center text-white",children=value)])
    
    return layout_content

@callback(Output("indicador_barras","fig"),
    [Input("contamination_drop","value")],
    [Input("year_slider_d","value")]
    )
def drop_updater(variable,year):
    if not variable:
        variables=["coal_consumption", "gas_consumption","oil_consumption", "renewables_consumption"]
    else:
        variables=variable

    df_barras=df[(df["Year"]>=year[0]) & (df["Year"]<=year[1])]
    fig = px.bar(df_barras, 
             x = "Year",
             y = variables,
             template = 'plotly_dark'
        )
    fig.update_layout(transition_duration=500)
    fig.update_layout(showlegend=False)
    fig.update_layout({
      "plot_bgcolor": "#040d10",
      "paper_bgcolor": "#040d10",
    })

    return fig