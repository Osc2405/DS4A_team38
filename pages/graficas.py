import dash
from dash import Input, Output, dcc, html,State, callback, callback_context
import dash_bootstrap_components as dbc
import pathlib

from app import app

import pandas as pd
import json
from pandas import json_normalize
from pandas.io.json import json_normalize

# get relative data folder
#PATH = pathlib.Path(__file__).parent
#DATA_PATH = PATH.joinpath("../datasets").resolve()
#departments = pd.read_csv(DATA_PATH.joinpath("department.csv"))
#departments['COD_DPTO']=departments['COD_DPTO'].astype(str)
#datatest = pd.read_csv(DATA_PATH.joinpath("department.csv"))
#print(departments)

#MAPA COLOMBIA
from components.maps.mapcol_departamentos import mapcol_departamentos
# dataset de prueba para el mapa
#datatest1=departments.to_json()
#print(datatest)

##PARA LOS FILTROS DEL MAPA COLOMBIA

df_finalCSV='https://raw.githubusercontent.com/ajrianop/projectDS4A/main/df_final.csv'
df=pd.read_csv(df_finalCSV,encoding='unicode_escape')

##FIN PARA LOS FILTROS DEL MAPA COLOMBIA

datatest ={"COD_DPTO":{"0":"05","1":"08","2":"11","3":"13","4":"15","5":"17","6":"18","7":"19","8":"20","9":"23","10":"25","11":"27","12":"41","13":"44","14":"47","15":"50","16":"52","17":"54","18":"63","19":"66","20":"68","21":"70","22":"73","23":"76","24":"81","25":"85","26":"86","27":"91","28":"94","29":"95","30":"97","31":"99","32":"88"},"DEPARTAMENTO":{"0":"ANTIOQUIA","1":"ATLANTICO","2":"SANTAFE DE BOGOTA D.C","3":"BOLIVAR","4":"BOYACA","5":"CALDAS","6":"CAQUETA","7":"CAUCA","8":"CESAR","9":"CORDOBA","10":"CUNDINAMARCA","11":"CHOCO","12":"HUILA","13":"LA GUAJIRA","14":"MAGDALENA","15":"META","16":"NARI\\u00d1O","17":"NORTE DE SANTANDER","18":"QUINDIO","19":"RISARALDA","20":"SANTANDER","21":"SUCRE","22":"TOLIMA","23":"VALLE DEL CAUCA","24":"ARAUCA","25":"CASANARE","26":"PUTUMAYO","27":"AMAZONAS","28":"GUAINIA","29":"GUAVIARE","30":"VAUPES","31":"VICHADA","32":"ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA"},"COUNT":{"0":525,"1":1193,"2":1518,"3":1839,"4":1541,"5":1676,"6":1864,"7":1096,"8":1652,"9":1131,"10":819,"11":1061,"12":1972,"13":1045,"14":739,"15":1057,"16":1269,"17":1708,"18":1948,"19":1525,"20":1743,"21":1441,"22":802,"23":1960,"24":792,"25":994,"26":1637,"27":682,"28":1352,"29":1173,"30":1115,"31":1151,"32":1758},"latitude":{"0":8.6192998894,"1":10.3612003326,"2":4.7951002121,"3":10.4236001975,"4":7.0275001523,"5":5.7526998521,"6":2.4978001119,"7":2.9751138688,"8":10.8562469488,"9":9.4230003359,"10":5.7488999368,"11":8.2716999057,"12":3.2739000325,"13":12.4235000614,"14":11.3276996617,"15":4.4449000365,"16":2.5773999689,"17":9.1339998247,"18":4.6946001053,"19":5.4751377105,"20":8.1150255208,"21":9.8849000932,"22":5.2814002036,"23":4.9735999108,"24":7.0592999452,"25":6.2479000086,"26":1.3164000513,"27":0.1186000023,"28":3.8605000963,"29":2.8375000958,"30":1.9852999444,"31":6.2795000082,"32":12.5945628115},"longitude":{"0":-76.3072967522,"1":-74.8705978394,"2":-74.0229034424,"3":-75.1595001224,"4":-72.2129974372,"5":-74.6949996949,"6":-74.6925964365,"7":-78.2116241452,"8":-73.2823181155,"9":-75.8195037842,"10":-74.3295974737,"11":-77.0213012688,"12":-74.6360015871,"13":-71.6212005615,"14":-74.0917968755,"15":-71.0799026493,"16":-77.9835968017,"17":-73.0177993776,"18":-75.6720962525,"19":-75.886505127,"20":-73.8001403806,"21":-75.4831008914,"22":-74.8399963373,"23":-76.0838012692,"24":-70.6986999517,"25":-70.17250061,"26":-76.5781021113,"27":-71.3863983161,"28":-67.687797549,"29":-71.2646026619,"30":-70.112998962,"31":-67.7968978901,"32":-81.7129569648}}

df_maptest = pd.DataFrame.from_dict(datatest)  

###With code_department_temp.csv
departament_temperature_CSV='https://raw.githubusercontent.com/ajrianop/projectDS4A/main/code_department_temp.csv'
temp_department=pd.read_csv(departament_temperature_CSV,encoding='utf-8', dtype = {'COD_DPTO': str})
departamentos=temp_department.DEPARTAMENTO.unique()

mapa_colombia_departamentos = mapcol_departamentos('Mapa Departamentos Colombia', 'div_municipios_fig2',temp_department)




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
        ##### PARA HACER EL MAPA COLOMBIA
        dbc.Row([
            dbc.Col([
                html.Div([
                    mapa_colombia_departamentos.display()  
                ],className="container", id="row_map")   
            ]),
        ], className= "card"),

        ##DROPDOWN
        html.Div(className="col-xs-12 col-sm-12 col-md-6 col-xl-6 pt-3",children=[
            html.Div(id='dd-output-container'),
            dcc.Dropdown(['AMAZONAS', 'ANTIOQUIA', 'ARAUCA', 'ATLANTICO', 'BOLIVAR',
       'BOYACA', 'BUENAVENTURA', 'CALDAS', 'CAQUETA', 'CASANARE', 'CAUCA',
       'CESAR', 'CHOCO', 'CORDOBA', 'CUNDINAMARCA', 'GUAINIA',
       'LA GUAJIRA', 'GUAVIARE', 'HUILA', 'MAGDALENA', 'META', 'NARIÑO',
       'NORTE DE SANTANDER', 'PUTUMAYO', 'QUINDIO', 'RISARALDA',
       'ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA',
       'SANTANDER', 'SUCRE', 'TOLIMA', 'VALLE DEL CAUCA', 'VAUPES',
       'VICHADA'], 'Seleccione depto', id='demo-dropdown'),
        ]),
        ##END DROPDOWN
        ##MAP
        html.Div(className="col-xs-12 col-sm-12 col-md-6 col-xl-6 text-center pt-3",children=[
            mapa_colombia_departamentos.display2(2.9986111111111, -75.304444444444)
        ]),
        ##END MAP
        ##MAP
        html.Div(className="col-xs-12 col-sm-12 col-md-6 col-xl-6 text-center pt-3",children=[
            mapa_colombia_departamentos.display2(12.594563,-81.712957)
        ]),
        ##END MAP
        
        #MAP WITH DROPDOWN
        html.Div(className="col-xs-12 col-sm-12 col-md-6 col-xl-6 text-center pt-3",children=[
            dcc.Dropdown(
                    id="id_selector_municipio",
                    options=[
                        {"label": "TODOS", "value": "TODOS"},
                        {"label": "BOYACA", "value": "BOYACA"},
                        {"label": "CUNDINAMARCA", "value": "CUNDINAMARCA"},
                        {"label": "ANTIOQUIA", "value": "ANTIOQUIA"},
                        {"label": "SANTANDER", "value": "SANTANDER"},
                    ],
                    value=['BOYACA', 'SANTANDER', 'CUNDINAMARCA', 'ANTIOQUIA'],
                    multi = True
                ),
                html.Div(['Seleccione el rango de valores'], className="mb-2  selector-label"),
                        dcc.Slider(0, 6, 0.01,
                        id='slider-updatemode',
                        marks={i: '{}'.format(10 ** i) for i in range(7)},
                        value=6,
                        updatemode='drag'
                    ),
                dbc.Button([
                    'Filtrar'
                ],id="id_filtrar")

        ]),
        #END MAP WITH DROPDOWN


        #####FILTROS MAPA COLOMBIA


        html.Section(className="text-white row pb-5",id="filtros-mapa", children=[

            html.Div(className="col-xs-12 col-sm-12 col-md-6 col-xl-6 pt-3",children=[
                html.H4(className="py-2 text-center",children="Filtros"),
                html.H5(className="py-2",children="Selecciona el rango de años a observar:"),
                dcc.RangeSlider(id="year_slider_d2", min=df["Year"].min(), max=df["Year"].max(),step=1,value=[df["Year"].min(),df["Year"].max()],marks=None, className="pt-4 pb-5",tooltip={"placement": "bottom", "always_visible": True}),
                html.H5("Selecciona un departamento", className="pt-3 pb-2"),
                dcc.Dropdown(id="departamentos_drop",multi=False, placeholder="Selecciona un departamento...", options=[{'label': x, 'value': x} for x in departamentos]),
            ]),


            html.Div(className="col-xs-12 col-sm-12 col-md-6 col-xl-6 text-center pt-3", children=[
                html.Div(className="seccion_home px-4",
                    children=[
                        html.Div(id='my-output',children=[
                            html.Div([
                                    #mapa_colombia_departamentos.display()
                                    #dcc.Graph(id="plot_temperature_map",figure={})
                                    html.Div([
                                        mapa_colombia_departamentos.display()  
                                    ],id="plot_temperature_map"),
                                ],className="container", id="row_map") 
                        ])
                    ])
                ])
            ]),

        ###FIN FILTRO MAPA COLOMBIA

    ]
)

## START CALLBACKS
@callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    return f'You have selected {value}'


## INTERACTIVE MAPA
@callback(
    [Output("plot_temperature_map", 'children')],
    #Output("plot_temperature_map","figure"),
    Output("text_year2","children"),
    Output("type_year","children"),
    [Input("year_slider_d2","value")],
)
def plot_map(year):
    df_barras=df[(df["Year"]>=year[0]) & (df["Year"]<=year[1])]
    last_year=int(df_barras.iloc[-1]['Year'])
    texto_year=f'Datos del año mas reciente ({last_year})'
    str_year=str.df_barras.iloc[-1]['Year']
    ###INTERACTIVE MAP  figure4
    mapa_colombia_departamentos_temp = mapcol_departamentos('Mapa Departamentos Colombia', 'div_municipios_fig2',temp_department)
    fig4=mapa_colombia_departamentos_temp.display3(12.594563,-81.712957, temp_department[str_year])
    type_year=type(last_year)

    #for figura in [fig4]:
    #    figura.update_layout(transition_duration=500)
    #    figura.update_layout(showlegend=False)
    #    figura.update_layout({
    #      "plot_bgcolor": "#040d10",
    #      "paper_bgcolor": "#040d10",
    #    })
    ###END INTERACTIVE MAP
    return [fig4], texto_year



