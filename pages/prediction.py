from logging import PlaceHolder
import dash
from dash import dcc, html,callback,Input, Output,State
import dash_bootstrap_components as dbc
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import pathlib
import plotly.express as px
import pickle
import numpy as np
import plotly.graph_objects as go 

from app import app

##Diccionario
dict_aumento={
    "Urban population": 2,
    "Rural population": 2,
    "Forest area": 2,
    'Agricultural land': 2,
    'Agricultural methane emissions' : 2,
    'Agricultural nitrous oxide emissions' : 2,
    'coal_consumption' : 2,
    'fossil_fuel_consumption' : 2,
    'gas_consumption' : 2,
    'hydro_consumption' : 2,
    'oil_consumption' : 2,
    'other_renewable_consumption' : 2,
    'primary_energy_consumption' : 2,
    'renewables_consumption' : 2,
    'population' : 2,
    'Temperature' : 2,
    'co2' : 2,
    'total_ghg' : 2,
    'methane' : 2,
    'nitrous_oxide' : 2,
    'gdp' : 2,
    'Cattle' : 2,
    'Pigs' : 2,
    "level_0":2,
    "index":2,
    'Unnamed: 0':2,
}


def rev_min_max_func(scaled_val):
    max_val = 24.584000000000003
    min_val = 23.12900000000002
    og_val = (scaled_val*(max_val - min_val)) + min_val
    return og_val








# Layout national
layout = html.Div(className="seccion_home px-4 pt-5 pb-5",
    children=[
        html.Div(className="row text-center text-white pb-3 pt-2",children=[
            html.H2("Prediccion de temperatura")
            ]),

        html.Section(className="row",children=[

            #Filtros
            html.Div(className="col-md-5",children=[
                html.H4("Filtros",className="text-white  text-center"),
                html.Div(className="sliders_filters",children=[
                    html.P("El slider a continuacion permite mostrar los posibles escenarios del cambio de temperatura a futuro modificando el cambio de cada variable por año.", className="text-white pt-3 text-justify"),
                    html.P(""),
                    dcc.Slider(id="slider1", min=-1, max=1,step=1,value=0,marks={-1:{"label":"Peor escenario", 'style': {'color': '#FFF'}},0:{"label":"Esperado", 'style': {'color': '#FFF'}},1:{"label":"Mejor escenario", 'style': {'color': '#FFF'}}}, className="pt-4 pb-5"),
                    ]),
                html.P(id="text_prediction",className="text-white") 
                ]),

            # Prediccion
            html.Div(className="prediction col-md-6",children=[
                    dcc.Graph(id="plot_prediction",figure={})
                ])
        ]),

        html.Section(className="row",children=[
            html.H3("Explicacion del modelo usado", className="text-center text-white"),
            html.P(className="pt-3",children="    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
            ])
    ]
)


@callback(
    Output("plot_prediction","figure"),
    Output("text_prediction","children"),
    Input("slider1","value")
    )
def plot_prediction(value):
    path_model="pages/model.pkl"
    model = pickle.load(open(path_model, 'rb'))
    X_test=pd.read_csv("datasets/X_test.csv")
    X_test=X_test.iloc[:,1:]
    variables=["coal_consumption","fossil_fuel_consumption",'gas_consumption','oil_consumption','population']
    X_test=X_test[variables]

    y_train=pd.read_csv("datasets/y_train.csv")
    y_train=y_train.iloc[:,1:]
    dict_aumento2={}
    if value==0:
        for k in dict_aumento.keys():
            dict_aumento2[k]=2
    elif value==-1:
        for k in dict_aumento.keys():
            dict_aumento2[k]=10
    else:
        for k in dict_aumento.keys():
            dict_aumento2[k]=1

    # Año hasta donde se quiere hacer la prediccion
    year=2040

    # Creacion de una lista donde cada nuevo valor es el anterior aumentado el porcentaje dado en dict_aumento
    lista=[]
    for i in range (year-2019):
      row=[]
      for j in range (len(X_test.columns)):
        if i==0:
          row.append(X_test.iloc[-1,j]*(1+dict_aumento2[X_test.columns[j]]/100))
        else:
          row.append(lista[i-1][j]*(1+dict_aumento2[X_test.columns[j]]/100))
      lista.append(row)

    # Se convierte la lista en un dataframe y se agrega al dataframe de prueba X_test en una nueva variable llamada X_futuro
    X_futuro = X_test.append(pd.DataFrame(lista, columns=X_test.columns))
    X_futuro.index = np.arange(2016,2041,1)

    # Se le agrega un ruido gausiano a los datos equivalente a un 10% de la desviacion estandar de cada columna
    for i in X_futuro.columns:
      X_futuro[i]=X_futuro[i]+np.random.normal(0,0.1*X_futuro[i].std(),X_futuro[i].shape)

    pred=model.predict(X_futuro)

    # Se crea una copia de los dataframes usados
    new_df=pred.copy()
    new_y=y_train.copy()

    # Desnormalizacion de los datos
    for i in range(len(new_df)):
        new_df[i] = rev_min_max_func(pred[i])
    for i in range(len(new_y)):
        new_y.iloc[i] = rev_min_max_func(new_y.iloc[i])

    # Generacion del grafico
    new_x=[x for x in range (2016,2016+len(new_df))]


    new_y.index=range(1990,2016,1)
    otro_df=pd.DataFrame(new_df,index=new_x)
    final_y=pd.concat([new_y, otro_df])

    fig = go.Figure()
    # Full line
    fig.add_scattergl(x=new_x, y=new_df, line={'color': '#636efa'})

    xs=[]
    for i in range(1990,2016,1):
      if i<2016:
        xs.append(i)
    # Above threshhgold
    #fig.add_scattergl(x=xs, y=new_y, line={'color': 'red'})
    

    fig.update_layout({
          "plot_bgcolor": "#040d10",
          "paper_bgcolor": "#040d10",
          "font_color":"white",
          "title_font_color":"white"
        })
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='gray',linewidth=1, linecolor='white',title_text='Año')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='gray',linewidth=1, linecolor='white',title_text='Temperatura media (°C)')

    texto="La temperatura en el año {} cambio {:.2f}°C con respecto a 1990".format(year,(new_df[-1]-23.458112600000025))
    return fig,texto

