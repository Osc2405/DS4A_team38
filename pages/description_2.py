import dash
from dash import dcc,html, callback,Input, Output,State
import dash_bootstrap_components as dbc
import pathlib
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
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

#INFORMACIÓN TEMPERATURA POR DEPARTAMENTOS_CSV
df_finalCSV='https://raw.githubusercontent.com/ajrianop/projectDS4A/main/df_final.csv'
df=pd.read_csv(df_finalCSV,encoding='unicode_escape')
# Convert landcover from "Hecta (100)" hectares to just hectares
df['Forest area'] = df['Forest area']*100
df['Agricultural land'] = df['Agricultural land']*100
#Datos departamento
#TEMPERATURA
departament_temperature_CSV='https://raw.githubusercontent.com/ajrianop/projectDS4A/main/code_department_temp.csv'
temp_department=pd.read_csv(departament_temperature_CSV,encoding='unicode_escape', dtype = {'COD_DPTO': str})
#PIB
departament_pib_CSV='https://raw.githubusercontent.com/ajrianop/projectDS4A/main/code_department_pib.csv'
pib_department=pd.read_csv(departament_pib_CSV,encoding='unicode_escape', dtype = {'COD_DPTO': str})
#DEFORESTACIÓN
departament_def_CSV='https://raw.githubusercontent.com/ajrianop/projectDS4A/main/code_department_def.csv'
def_department=pd.read_csv(departament_def_CSV,encoding='unicode_escape', dtype = {'COD_DPTO': str})

#DATA CLEANING DE TEMPERATURA DEPARTAMENTO
temp_department=temp_department.dropna(axis='rows')
erase_years_df_temp=['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '2020']
temp_department=temp_department.drop(columns=erase_years_df_temp, axis=1)
departamentos=temp_department.DEPARTAMENTO.unique()

#DATA CLEANING DE PIB
'''pib_department=pib_department.dropna(axis='rows')
pib_department=pib_department[pib_department['0']!='ARAUCA']
pib_department=pib_department[pib_department['0']!='GUAVIARE']
pib_department=pib_department[pib_department['0']!='AMAZONAS']
pib_department=pib_department[pib_department['0']!='CASANARE']
pib_department=pib_department[pib_department['0']!='GUAINIA']
pib_department=pib_department[pib_department['0']!='VICHADA']
pib_department=pib_department[pib_department['0']!='VAUPES']
pib_department=pib_department[pib_department['0']!='PUTUMAYO']
pib_department=pib_department[pib_department['0']!='ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA']'''

#print(pib_department['0']!='SANTAFE DE BOGOTA D.C')

#DATA CLEANING DE DEFORESTACION
for i in range(1990,2013):
    l=str(i)
    def_department[l]=def_department[l].str.replace(',','.').astype(float)
#print(def_department.info())

#print(temp_department[temp_department['DEPARTAMENTO']=='CUNDINAMARCA']['latitude']),
#print(temp_department[temp_department['DEPARTAMENTO']=='CUNDINAMARCA']['longitude']),
LAT_CUN=temp_department[temp_department['DEPARTAMENTO']=='CUNDINAMARCA']['latitude']
LON_CUN=temp_department[temp_department['DEPARTAMENTO']=='CUNDINAMARCA']['longitude']
#print(temp_department.columns[1:43])

mapa_colombia_departamentos_temp = mapcol_departamentos('Mapa Temperatura Colombia', 'div_departamentos_fig',temp_department)
mapa_colombia_departamentos_pib = mapcol_departamentos('Mapa PIB Colombia', 'div_departamentos_fig',pib_department)
mapa_colombia_departamentos_def = mapcol_departamentos('Mapa Deforestación Colombia', 'div_departamentos_fig',def_department)
############


'''
datatest ={"COD_DPTO":{"0":"05","1":"08","2":"11","3":"13","4":"15","5":"17","6":"18","7":"19","8":"20","9":"23","10":"25","11":"27","12":"41","13":"44","14":"47","15":"50","16":"52","17":"54","18":"63","19":"66","20":"68","21":"70","22":"73","23":"76","24":"81","25":"85","26":"86","27":"91","28":"94","29":"95","30":"97","31":"99","32":"88"},"DEPARTAMENTO":{"0":"ANTIOQUIA","1":"ATLANTICO","2":"SANTAFE DE BOGOTA D.C","3":"BOLIVAR","4":"BOYACA","5":"CALDAS","6":"CAQUETA","7":"CAUCA","8":"CESAR","9":"CORDOBA","10":"CUNDINAMARCA","11":"CHOCO","12":"HUILA","13":"LA GUAJIRA","14":"MAGDALENA","15":"META","16":"NARI\\u00d1O","17":"NORTE DE SANTANDER","18":"QUINDIO","19":"RISARALDA","20":"SANTANDER","21":"SUCRE","22":"TOLIMA","23":"VALLE DEL CAUCA","24":"ARAUCA","25":"CASANARE","26":"PUTUMAYO","27":"AMAZONAS","28":"GUAINIA","29":"GUAVIARE","30":"VAUPES","31":"VICHADA","32":"ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA"},"COUNT":{"0":525,"1":1193,"2":1518,"3":1839,"4":1541,"5":1676,"6":1864,"7":1096,"8":1652,"9":1131,"10":819,"11":1061,"12":1972,"13":1045,"14":739,"15":1057,"16":1269,"17":1708,"18":1948,"19":1525,"20":1743,"21":1441,"22":802,"23":1960,"24":792,"25":994,"26":1637,"27":682,"28":1352,"29":1173,"30":1115,"31":1151,"32":1758},"latitude":{"0":8.6192998894,"1":10.3612003326,"2":4.7951002121,"3":10.4236001975,"4":7.0275001523,"5":5.7526998521,"6":2.4978001119,"7":2.9751138688,"8":10.8562469488,"9":9.4230003359,"10":5.7488999368,"11":8.2716999057,"12":3.2739000325,"13":12.4235000614,"14":11.3276996617,"15":4.4449000365,"16":2.5773999689,"17":9.1339998247,"18":4.6946001053,"19":5.4751377105,"20":8.1150255208,"21":9.8849000932,"22":5.2814002036,"23":4.9735999108,"24":7.0592999452,"25":6.2479000086,"26":1.3164000513,"27":0.1186000023,"28":3.8605000963,"29":2.8375000958,"30":1.9852999444,"31":6.2795000082,"32":12.5945628115},"longitude":{"0":-76.3072967522,"1":-74.8705978394,"2":-74.0229034424,"3":-75.1595001224,"4":-72.2129974372,"5":-74.6949996949,"6":-74.6925964365,"7":-78.2116241452,"8":-73.2823181155,"9":-75.8195037842,"10":-74.3295974737,"11":-77.0213012688,"12":-74.6360015871,"13":-71.6212005615,"14":-74.0917968755,"15":-71.0799026493,"16":-77.9835968017,"17":-73.0177993776,"18":-75.6720962525,"19":-75.886505127,"20":-73.8001403806,"21":-75.4831008914,"22":-74.8399963373,"23":-76.0838012692,"24":-70.6986999517,"25":-70.17250061,"26":-76.5781021113,"27":-71.3863983161,"28":-67.687797549,"29":-71.2646026619,"30":-70.112998962,"31":-67.7968978901,"32":-81.7129569648}}

df_maptest = pd.DataFrame.from_dict(datatest)  
mapa_colombia_departamentos = mapcol_departamentos('Mapa Departamentos Colombia', 'div_municipios_fig2',df_maptest)

departamentosCSV='https://raw.githubusercontent.com/ajrianop/projectDS4A/main/department.csv'
departamentos=pd.read_csv(departamentosCSV,encoding='unicode_escape')
departamentos=departamentos.DEPARTAMENTO.unique()
'''
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
layout=html.Div(className="seccion_home px-4 pt-5",
    children=[
        html.H1(className="pt-4 text-center text-white pb-5",children="Seccion descriptiva"),
        html.Section(className="text-white row pb-5",id="filtros-mapa", children=[
            html.H4(className="py-2 text-center",children="Filtros"),
            html.Div(className="col-xs-12 col-sm-12 col-md-6 col-xl-6 pt-3",children=[
                html.H5(className="py-2",children="Selecciona el rango de años a observar:"),
                dcc.RangeSlider(id="year_slider_d", min=df["Year"].min(), max=df["Year"].max(),step=1,value=[df["Year"].min(),df["Year"].max()],marks=None, className="pt-4 pb-5",tooltip={"placement": "bottom", "always_visible": True}),
            ]),
            html.Div(className="col-xs-12 col-sm-12 col-md-6 col-xl-6 pt-3",children=[
                html.H5("Selecciona un departamento", className="pt-3 pb-2"),
                dcc.Dropdown(id="departamentos_drop",multi=False, placeholder="Selecciona un departamento...", options=[{'label': x, 'value': x} for x in departamentos]),
            ]),


            html.Div(className="col-xs-12 col-sm-12 col-md-4 col-xl-4 text-center pt-3", children=[
                html.Div(className="seccion_home px-4",
                    children=[
                        html.Div(id='my-output',children=[
                            html.Div([
                                    mapa_colombia_departamentos_temp.display()  
                                ],className="container", id="row_map_temp") 
                        ])
                    ]),
                    html.Div(className="d-flex flex-column justify-content-around",children=[
                        #html.H3("Info_drop", className="text-center text-black", id="Info_drop"),
                        html.H3("Temperatura departamento", className="text-center text-white", id="info_dep_temp"),
                    ]),
                ]),
                html.Div(className="col-xs-12 col-sm-12 col-md-4 col-xl-4 text-center pt-3", children=[
                html.Div(className="seccion_home px-4",
                    children=[
                        html.Div(id='my-output',children=[
                            html.Div([
                                    mapa_colombia_departamentos_pib.display()  
                                ],className="container", id="row_map_pib") 
                        ])
                    ]),
                    html.Div(className="d-flex flex-column justify-content-around",children=[
                        html.H3("PIB departamento", className="text-center text-white", id="info_dep_pib"),
                    ]),
                ]),
                html.Div(className="col-xs-12 col-sm-12 col-md-4 col-xl-4 text-center pt-3", children=[
                html.Div(className="seccion_home px-4",
                    children=[
                        html.Div(id='my-output',children=[
                            html.Div([
                                    mapa_colombia_departamentos_def.display()  
                                ],className="container", id="row_map_def") 
                        ])
                    ]),
                    html.Div(className="d-flex flex-column justify-content-around",children=[
                        #html.H3("Info_drop", className="text-center text-black", id="Info_drop"),
                        html.H3("Deforestación departamento", className="text-center text-white", id="info_dep_def"),
                    ]),
                ]),
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


        # Letras en blanco y estilo de color de gráfica
        fig_energy.update_layout({
          "plot_bgcolor": "#040d10",
          "paper_bgcolor": "#040d10",
          "font_color":"white",
          "title_font_color":"white"
        })

        # Leyenda arriba de gráfica
        fig_energy.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
        ))

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
        fig_gas.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
        ))

        # Letras en blanco y estilo de color de gráfica
        fig_gas.update_layout({
          "plot_bgcolor": "#040d10",
          "paper_bgcolor": "#040d10",
          "font_color":"white",
          "title_font_color":"white"
        })

        ##! PLOTLY Population
        fig_population = px.bar(df, 
                    x = "Year",
                    y = ["Urban population", "Rural population"],
                    template = 'plotly_dark',
                    title = 'Población', 
                    )
        fig_population.add_trace(
            go.Scatter(x=df["Year"], y=df["population"], name="Población",hoveron='points'),
            
        )

        # Leyenda arriba de gráfica
        fig_population.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))

        # Set x-axis title and range
        fig_population.update_xaxes(title_text="Año")
        fig_population.update_xaxes(range=(1990,2020))

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
        fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
        ))

        # Letras en blanco y estilo de color de gráfica
        fig_landcover.update_layout({
          "plot_bgcolor": "#040d10",
          "paper_bgcolor": "#040d10",
          "font_color":"white",
          "title_font_color":"white"
        })
        fig_landcover.update_traces(line_width=5)

        # Set x-axis title
        fig_landcover.update_xaxes(title_text="Año")

        # Set y-axes titles
        fig_landcover.update_yaxes(title_text="Hectareas")

        ##! Cattle and Agricultural Methane emissions
        # Create figure with secondary y-axis
        fig_cattle_methane = make_subplots(specs=[[{"secondary_y": True}]])

        # Add traces
        fig_cattle_methane.add_trace(
            go.Scatter(x=df_barras["Year"], y=df_barras["Cattle"], name="Ganado bovino"),
            secondary_y=False,
        )

        fig_cattle_methane.add_trace(
            go.Scatter(x=df_barras["Year"], y=df_barras["Agricultural methane emissions kT"], name="Emisiones metano agricultura"),
            secondary_y=True, 
        )



        # Set x-axis title and range
        fig_cattle_methane.update_xaxes(title_text="Año")
        #fig_cattle_methane.update_xaxes(range=(1990,2020))

        # Set y-axes titles
        fig_cattle_methane.update_yaxes(title_text="Ganado bovino (número de cabezas)", secondary_y=False)
        fig_cattle_methane.update_yaxes(title_text="Emisiones metano agricultura (kiloTons)", secondary_y=True)

        # Leyenda arriba de gráfica
        fig_cattle_methane.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1),
            #width=400, 
            #height=400,
        )
        # Letras en blanco y estilo de color de gráfica
        fig_cattle_methane.update_layout({
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
        "font_color":"white",
        "title_font_color":"white"
        })

        fig_cattle_methane.update_layout(template="plotly_dark")
        fig_cattle_methane.update_traces(line_width=5)

        ##! PLOTY GDP and rural population
        #Create figure with secondary y-axis
        fig_gdp_rural_pop = make_subplots(specs=[[{"secondary_y": True}]])

        # Add traces
        fig_gdp_rural_pop.add_trace(
            go.Scatter(x=df_barras["Year"], y=df_barras["gdp"], name="Producto Interno Bruto (PIB)"),
            secondary_y=False,
        )

        fig_gdp_rural_pop.add_trace(
            go.Scatter(x=df_barras["Year"], y=df_barras["Rural population"], name="Población rural"),
            secondary_y=True,
        )

        # Add figure title
        fig_gdp_rural_pop.update_layout(
            title_text="Producto Interno Bruto y Población rural"
        )

        # Set x-axis title and range
        fig_gdp_rural_pop.update_xaxes(title_text="Año")
        #fig_gdp_rural_pop.update_xaxes(range=(1990,2020))

        # Set y-axes titles
        fig_gdp_rural_pop.update_yaxes(title_text="Población rural (número de habitantes)", secondary_y=False)
        fig_gdp_rural_pop.update_yaxes(title_text="PIB (miles de millones de pesos)", secondary_y=True)

        # Leyenda arriba de gráfica
        fig_gdp_rural_pop.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))

        # Letras en blanco y estilo de color de gráfica
        fig_gdp_rural_pop.update_layout({
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
        "font_color":"white",
        "title_font_color":"white"
        })
        fig_gdp_rural_pop.update_traces(line_width=5)
        fig_gdp_rural_pop.update_layout(template="plotly_dark")

        ##! PLOTY GDP and CO2
        # #Create figure with secondary y-axis
        fig_gdp_co2 = make_subplots(specs=[[{"secondary_y": True}]])

        # Add traces
        fig_gdp_co2.add_trace(
            go.Scatter(x=df_barras["Year"], y=df_barras["gdp"], name="Producto Interno Bruto (PIB)"),
            secondary_y=False,
        )

        fig_gdp_co2.add_trace(
            go.Scatter(x=df_barras["Year"], y=df_barras["co2"], name="Emisiones de CO2"),
            secondary_y=True,
        )

        # Add figure title
        fig_gdp_co2.update_layout(
            title_text="Producto Interno Bruto y Emisiones de CO2"
        )

        # Set x-axis title and range
        fig_gdp_co2.update_xaxes(title_text="Año")
        #fig_gdp_co2.update_xaxes(range=(1990,2020))

        # Set y-axes titles
        fig_gdp_co2.update_yaxes(title_text="PIB (miles de millones de pesos)", secondary_y=False)
        fig_gdp_co2.update_yaxes(title_text="Emisiones de CO2 (Kilotoneladas)", secondary_y=True)

        # Leyenda arriba de gráfica
        fig_gdp_co2.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))

        # Letras en blanco y estilo de color de gráfica
        fig_gdp_co2.update_layout({
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
        "font_color":"white",
        "title_font_color":"white"
        })
        fig_gdp_co2.update_traces(line_width=5)
        fig_gdp_co2.update_layout(template="plotly_dark")

        ##!

        ##! 

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
                    html.Div(className="col-md-8",children=[
                        dcc.Graph(id="energy_consumption",figure=fig_energy)
                        ]),
                    html.Div(className="col-md-3",children=[
                        html.P(className="", style={'color': 'white', 'fontSize': 20},children="En Colombia, el petróleo es la fuente de energía que más se consume. Y a pesar de que ha pasado de ser alrededor del 50% del consumo en 1990 a alrededor del 30% en 2019, su cantidad neta se ha casi duplicado. El gas es la fuente de energía con mayor crecimiento, dada la gasificación de servicios importantes, principalmente servicios públicos, que sigue teniendo incentivos gubernamentales. ")
                        ]),
                    
                    ]),
                #Fila 2
                html.Div(className="row pb-5",children=[
                    html.Div(className="col-md-8",children=[
                        dcc.Graph(id="gas_consumption",figure=fig_gas)
                        ]),

                    html.Div(className="col-md-3",children=[
                        html.P(className="",style={'color': 'white', 'fontSize': 20},children="La población colombiana ha crecido en un 152% desde 1990 hasta 2019 y el crecimiento urbano ha sido más pronunciado que el rural. Actualmente el 81% de la población vive en las ciudades, lo que sobrepasa los estimados mundiales de 68% de la población mundial viviendo en ciudades para el 2050. Esto se debe en parte a los desplazamientos forzados causados por el conflicto armado del país.")
                        ]),
                    
                    ]),
                #Fila 3
                html.Div(className="row pb-5",children=[
                    html.Div(className="col-md-8",children=[
                        dcc.Graph(id="population_graph",figure=fig_population)
                        ]),
                    html.Div(className="col-md-3",children=[
                        html.P(className="",style={'color': 'white', 'fontSize': 20},children="La emisión de gases de efecto invernadero, como el dióxido de carbono (CO2), Metano (CH4), Óxido nitroso (N2O), Hidrofluorocarbonos (HFC), Hexafluoruro de azufre (SF6) y Perfluorocarbonos (PFC) aumenta a través del tiempo. Estos gases contribuyen a aumentar la temperatura del planeta, porque absorben y envían radiación infrarroja desde la superficie terrestre. Además, permanecen en la atmósfera durante años, décadas o incluso siglos.")
                        ]),
                    
                    ]),
                #Fila 4
                html.Div(className="row pb-5",children=[
                    html.Div(className="col-md-8",children=[
                        dcc.Graph(id="land_cover",figure=fig_landcover)
                        ]),
                    html.Div(className="col-md-3",children=[
                        html.P(className="",style={'color': 'white', 'fontSize': 20},children="En Colombia, la deforestación sucede a una tasa casi constante, mientras que las tierras usadas para la agricultura crecen y decrecen de forma escalonada. Cuando la cobertura de tierra usada para la agricultura decrece, esto puede indicar que su uso cambió, no necesariamente que se reforestó porque en dado caso, veríamos algún tipo de aumento en la curva de cobertura de bosque.")
                        ]),
                    ]),
                #Fila 5
                html.Div(className="row pb-5",children=[
                    html.Div(className="col-md-8",children=[
                        dcc.Graph(id="cattle_methane",figure=fig_cattle_methane)
                        ]),
                    html.Div(className="col-md-3",children=[
                        html.P(className="",style={'color': 'white', 'fontSize': 20},children="Las emisiones de metano provenientes de la agricultura y el número de cabezas de ganado siguen una tendencia similar en el tiempo. Esto se puede deber a que el gas metano es uno de los productos de la digestión del ganado y por tanto entre más ganado se incrementan las emisiones de este gas. Algunos estudios se enfocan en determinar el efecto del gas metano proveniente de las vacas como parte de los gases de efecto invernadero.")
                        ]),
                    ]),
                #Fila 6
                html.Div(className="row pb-5",children=[
                    html.Div(className="col-md-8",children=[
                        dcc.Graph(id="gdp_rural_pop",figure=fig_gdp_rural_pop)
                        ]),
                    html.Div(className="col-md-3",children=[
                        html.P(className="",style={'color': 'white', 'fontSize': 20},children="FALTA GRAFICA Es interesante ver la tendencia del Producto Interno Bruto (PIB) a lo largo de los años y en este caso, su relación con el número de habitantes del campo. Entre 1990 y 1999 hubo un ligero incremento en la población rural. A partir de 1999, año en el que hubo una grave crisis económica, esta población empezó de nuevo a reducirse muy posiblemente debido a la migración a las ciudades donde encontraban mayores posibilidades laborales.")
                        ]),
                    ]),
                #Fila 7
                html.Div(className="row pb-5",children=[
                    html.Div(className="col-md-8",children=[
                        dcc.Graph(id="gdp_co2",figure=fig_gdp_co2)
                        ]),
                    html.Div(className="col-md-3",children=[
                        html.P(className="",style={'color': 'white', 'fontSize': 20},children="En éstas gráficas se observa la relación entre el Producto Interno Bruto (PIB) y variables de consumo de energía, emisiones de gases de efecto invernadero, número de habitantes y cubierta o uso de la tierra.")
                        ]),
                    ]),
                ])

            ])
    else:
        #CREAR GRÁFICA
        layout_content=html.Div(className="text-center text-white", children=[
            #INFO DEPARTAMENTAL
            html.Section(className="container text-white pb-5",children=[
                html.H3(className="text-center text-white",children=value),
                #html.Div(className="col-md-6",children=[
                        #dcc.Graph(id="energy_consumption",figure=fig_energy)
                        #]),
                html.Div(className="col-md-5",children=[
                    html.P(className="",children="Podemos observar que el cambio de temperatura tiene una relación directamente proporcional con respecto al crecimiento del PIB y la deforestación en Colombia.")
                        ]),
            ]),
            ]),
        
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

#callback TEMPERATURA
@callback(
    Output("row_map_temp", 'children'),
    #Output("row_map_pib", 'children'),
    Output("info_dep_temp","children"),
    #Output("last_year", "children"),
    Input("departamentos_drop", "value"),
    [Input("year_slider_d", "value")]
)

def update_map(depart,years):
    if not depart:
        info_dep_temp=f'Temperatura en Colombia, año {str(years[1])}'
        #fig4=mapa_colombia_departamentos.display2(5.7489, -74.329597, str(years[1]),'Reds'),
        fig4=mapa_colombia_departamentos_temp.display2(3.958788, -73.608479,str(years[1]),'turbo'),#'RdBu_r')#,'Reds'),
        #fig5=mapa_colombia_departamentos_pib.display2(3.958788, -73.608479,str(years[1]),'dense'),
    else:
        LAT_CUN_DEP=temp_department[temp_department['DEPARTAMENTO']==depart]['latitude']
        LON_CUN_DEP=temp_department[temp_department['DEPARTAMENTO']==depart]['longitude']
        LAT_CUN_DEP=float(LAT_CUN_DEP.iloc[0])
        LON_CUN_DEP=float(LON_CUN_DEP.iloc[0])
        info_dep_temp=f'Temperatura en {depart}, año {str(years[1])}'
        fig4=mapa_colombia_departamentos_temp.display3(LAT_CUN_DEP, LON_CUN_DEP, str(years[1]),'turbo'),#'RdBu_r')# 'Reds')
    return fig4,info_dep_temp

#callback PIB
@callback(
Output("row_map_pib", 'children'),
Output("info_dep_pib","children"),
Input("departamentos_drop", "value"),
[Input("year_slider_d", "value")]
)

def update_map(depart,years):
    if not depart:
        info_dep_pib=f'PIB en Colombia, año {str(years[1])}.\n (*) En negro estan los departamentos con información faltante.'
        fig5=mapa_colombia_departamentos_pib.display2(3.958788, -73.608479,str(years[1]),'turbo'),#'hot_r'),
    else:
        LAT_CUN_DEP=pib_department[pib_department.iloc[:,0]==depart]['latitude']
        LON_CUN_DEP=pib_department[pib_department.iloc[:,0]==depart]['longitude']
        LAT_CUN_DEP=float(LAT_CUN_DEP.iloc[0])
        LON_CUN_DEP=float(LON_CUN_DEP.iloc[0])
        info_dep_pib=f'PIB en {depart}, año {str(years[1])}'
        fig5=mapa_colombia_departamentos_pib.display3(LAT_CUN_DEP, LON_CUN_DEP, str(years[1]), 'turbo'),#'hot_r')
    return fig5,info_dep_pib

#callback PIB
@callback(
Output("row_map_def", 'children'),
Output("info_dep_def","children"),
Input("departamentos_drop", "value"),
[Input("year_slider_d", "value")]
)

def update_map(depart,years):
    if not depart:
        info_dep_def=f'Deforestación en Colombia, año {str(years[1])}'
        fig6=mapa_colombia_departamentos_def.display2(3.958788, -73.608479,str(years[1]),'turbo'),#'aggrnyl'),
    else:
        LAT_CUN_DEP=def_department[def_department['DEPARTAMENTO']==depart]['latitude']
        LON_CUN_DEP=def_department[def_department['DEPARTAMENTO']==depart]['longitude']
        LAT_CUN_DEP=float(LAT_CUN_DEP.iloc[0])
        LON_CUN_DEP=float(LON_CUN_DEP.iloc[0])
        info_dep_def=f'Deforestación en {depart}, año {str(years[1])}'
        fig6=mapa_colombia_departamentos_def.display3(LAT_CUN_DEP, LON_CUN_DEP, str(years[1]),'turbo'),#'aggrnyl')
    return fig6,info_dep_def



#Figuras regional 



## END CALLBACKS DESCRIPTION
