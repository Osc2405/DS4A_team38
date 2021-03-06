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

## Percentage Increase Dictionary of Variables
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
df_final=pd.read_csv("datasets/df_final.csv")

# Functions to denormalize data
def rev_min_max_func(scaled_val):
    max_val = 24.584000000000003
    min_val = 23.12900000000002
    og_val = (scaled_val*(max_val - min_val)) + min_val
    return og_val

def rev_min_max_func_variable(scaled_val,variable):
    max_val = max(df_final[variable])
    min_val = min(df_final[variable])
    og_val = (scaled_val*(max_val - min_val)) + min_val
    return og_val


# Layout Prediction page
layout = html.Div(className="seccion_home px-4 pt-5 pb-5",
    children=[
        html.Div(className="row text-center text-white pb-3 pt-2",children=[
            html.H2("Prediccion de temperatura",className="pt-5")
            ]),

        html.Section(className="row",children=[

            #Filtros
            html.Div(className="col-md-5",children=[
                html.H4("Filtros",className="text-white  text-center"),
                html.Div(className="sliders_filters",children=[
                    html.P("El slider a continuacion permite mostrar los posibles escenarios del cambio de temperatura a futuro modificando el cambio de cada variable por a??o.", className="text-white pt-3 text-justify"),
                    html.P(""),
                    dcc.Slider(id="slider1", min=-1, max=1,step=1,value=0,marks={-1:{"label":"Peor escenario", 'style': {'color': '#FFF'}},0:{"label":"Esperado", 'style': {'color': '#FFF'}},1:{"label":"Mejor escenario", 'style': {'color': '#FFF'}}}, className="pt-4 pb-5"),
                    dcc.Loading(
                        id="loading-1",
                        type="default",
                        children=html.Div(id="loading-output-1")
                    ),
                    ]),
                html.P(id="text_prediction",className="text-white") 
                ]),

            # Prediccion
            html.Div(className="prediction col-md-6",children=[
                    dcc.Graph(id="plot_prediction",figure={})
                ])
        ]),

        html.Section(className="row",children=[
            html.Div(className="col-md-4",children=[
                dcc.Graph(id="coal_plot",figure={})
                ]),
            html.Div(className="col-md-4",children=[
                dcc.Graph(id="fosil2_plot",figure={})
                ]),
            html.Div(className="col-md-4",children=[
                dcc.Graph(id="fosil_plot",figure={})
                ]),

            ]),

        html.Section(className="row justify-content-around",children=[
            html.Div(className="col-md-4",children=[
                dcc.Graph(id="gas_plot",figure={})
                ]),
            html.Div(className="col-4",children=[
                dcc.Graph(id="oil_plot",figure={})
                ]),
            html.Div(className="col-4",children=[
                dcc.Graph(id="population_plot",figure={})
                ]),
            ]),
    ]
)


# Callbacks
@callback(
    Output("plot_prediction","figure"),
    Output("text_prediction","children"),
    Output("loading-output-1","children"),
    Output("coal_plot","figure"),
    Output("fosil2_plot","figure"),
    Output("fosil_plot","figure"),
    Output("gas_plot","figure"),
    Output("oil_plot","figure"),
    Output("population_plot","figure"),
    Input("slider1","value")
    )
def plot_prediction(value):
    # Load model
    path_model="pages/model_BR6.pkl"
    model = pickle.load(open(path_model, 'rb'))

    # Read datasets
    X_test=pd.read_csv("datasets/X_test.csv")
    X_train=pd.read_csv("datasets/X_train.csv")
    df_final=pd.read_csv("datasets/df_final.csv")
    X_test=X_test.iloc[:,1:]
    
    # Variables used in the model
    variables=["Forest area","fossil_fuel_consumption","renewables_consumption","population","total_ghg","gdp"]

    # If the variable "Unnamed: 0" exists
    X_train=X_train.iloc[:,1:]


    y_train=pd.read_csv("datasets/y_train.csv")
    y_train=y_train.iloc[:,1:]
    dict_aumento2={}
    if value==0:
        for k in dict_aumento.keys():
            # Normal scenario
            dict_aumento2[k]=2
            color_pred="#636efa"
    elif value==-1:
        for k in dict_aumento.keys():
            # Bad scenario
            dict_aumento2[k]=7
            color_pred="#ff9b34"
    else:
        for k in dict_aumento.keys():
            # Good scenario
            dict_aumento2[k]=0.05
            color_pred="#73ec84"

    # Year to predict
    year=2040

    # Creation of a list where each new value is the previous one increased by the percentage given in dict_increase
    lista=[]
    for i in range (year-2019):
      row=[]
      for j in range (len(X_test.columns)):
        if i==0:
          row.append(X_test.iloc[-1,j]*(1+dict_aumento2[X_test.columns[j]]/100))
        else:
          row.append(lista[i-1][j]*(1+dict_aumento2[X_test.columns[j]]/100))
      lista.append(row)

    X_futuro = X_test.append(pd.DataFrame(lista, columns=X_test.columns))
    X_futuro.index = np.arange(2016,2041,1)

    # Add random noise to the input variables
    for i in X_futuro.columns:
      X_futuro[i]=X_futuro[i]+np.random.normal(0,0.1*X_futuro[i].std(),X_futuro[i].shape)

    pred=model.predict(X_futuro)

    # Copy the used dataframes
    new_df=pred.copy()
    new_y=y_train.copy()
    new_X_futuro=X_futuro.copy()
    new_X_train=X_train.copy()

    # Denormalize the data
    for i in range(len(new_df)):
        new_df[i] = rev_min_max_func(pred[i])
    for i in range(len(new_y)):
        new_y.iloc[i] = rev_min_max_func(new_y.iloc[i])

    for i in range (len(new_X_futuro)):
        for j in range(len(new_X_futuro.columns)):
            new_X_futuro.iloc[i,j] = rev_min_max_func_variable(new_X_futuro.iloc[i,j],new_X_futuro.columns[j])

    for i in range (len(new_X_train)):
        for j in range(len(new_X_train.columns)):
            new_X_train.iloc[i,j] = rev_min_max_func_variable(new_X_train.iloc[i,j],new_X_train.columns[j])


    # Change index values 
    new_x=[x for x in range (2016,2016+len(new_df))]
    new_y.index=range(1990,2016,1)
    otro_df=pd.DataFrame(new_df,index=new_x)
    final_y=pd.concat([new_y, otro_df])

    # Prediction plot creation
    fig = go.Figure()
    fig.add_scattergl(x=new_x, y=new_df, line={'color': color_pred},name="Prediccion")

    # Add original data
    xs=[]
    for i in range(1990,2016,1):
        xs.append(i)
    fig.add_scattergl(x=new_y.index.values, y=new_y.Temperature.tolist(), line={'color': 'red'},name="Original")    

    # Update chart
    fig.update_layout({
          "plot_bgcolor": "#040d10",
          "paper_bgcolor": "#040d10",
          "font_color":"white",
          "title_font_color":"white"
        })
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='gray',linewidth=1, linecolor='white',title_text='A??o')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='gray',linewidth=1, linecolor='white',title_text='Temperatura media (??C)')
    fig.update_traces(line_width=5)
    fig.update_yaxes(range=[22,27], dtick=1)

    texto="La temperatura en el a??o {} cambio {:.2f}??C con respecto a 1990".format(year,(new_df[-1]-23.458112600000025))

    texto_loader="Cargado"

    X_train.index=new_y.index.values
    new_X_train.index=X_train.index


    # Creation of the graphs of the input variables
    fig_coal=go.Figure()
    fig_coal.add_scattergl(x=new_x, y=new_X_futuro[variables[0]], line={'color': color_pred},name="Prediccion")
    fig_coal.add_scattergl(x=new_X_train.index.values, y=new_X_train[variables[0]].tolist(), line={'color': 'red'},name="Original")
    fig_coal.update_xaxes(showgrid=True, gridwidth=1, gridcolor='gray',linewidth=1, linecolor='white',title_text='A??o')
    fig_coal.update_yaxes(showgrid=True, gridwidth=1, gridcolor='gray',linewidth=1, linecolor='white',title_text="Kilometros cuadrados")
    fig_coal.update_layout(title_text='Area de bosque', title_x=0.5)

    fig_fosil2=go.Figure()
    fig_fosil2.add_scattergl(x=new_x, y=new_X_futuro[variables[1]], line={'color': color_pred},name="Prediccion")
    fig_fosil2.add_scattergl(x=new_X_train.index.values, y=new_X_train[variables[1]].tolist(), line={'color': 'red'},name="Original")
    fig_fosil2.update_xaxes(showgrid=True, gridwidth=1, gridcolor='gray',linewidth=1, linecolor='white',title_text='A??o')
    fig_fosil2.update_yaxes(showgrid=True, gridwidth=1, gridcolor='gray',linewidth=1, linecolor='white',title_text="TWh")
    fig_fosil2.update_layout(title_text='Consumo de combustible fosil', title_x=0.5)


    fig_fosil=go.Figure()
    fig_fosil.add_scattergl(x=new_x, y=new_X_futuro[variables[2]], line={'color': color_pred},name="Prediccion")
    fig_fosil.add_scattergl(x=new_X_train.index.values, y=new_X_train[variables[2]].tolist(), line={'color': 'red'},name="Original")
    fig_fosil.update_xaxes(showgrid=True, gridwidth=1, gridcolor='gray',linewidth=1, linecolor='white',title_text='A??o')
    fig_fosil.update_yaxes(showgrid=True, gridwidth=1, gridcolor='gray',linewidth=1, linecolor='white',title_text="TWh")
    fig_fosil.update_layout(title_text='Consumo de E. renovables', title_x=0.5)

    fig_gas=go.Figure()
    fig_gas.add_scattergl(x=new_x, y=new_X_futuro[variables[3]], line={'color': color_pred},name="Prediccion")
    fig_gas.add_scattergl(x=new_X_train.index.values, y=new_X_train[variables[3]].tolist(), line={'color': 'red'},name="Original")
    fig_gas.update_xaxes(showgrid=True, gridwidth=1, gridcolor='gray',linewidth=1, linecolor='white',title_text='A??o')
    fig_gas.update_yaxes(showgrid=True, gridwidth=1, gridcolor='gray',linewidth=1, linecolor='white',title_text="# de habitantes")
    fig_gas.update_layout(title_text='Poblacion', title_x=0.5)

    fig_oil=go.Figure()
    fig_oil.add_scattergl(x=new_x, y=new_X_futuro[variables[4]], line={'color': color_pred},name="Prediccion")
    fig_oil.add_scattergl(x=new_X_train.index.values, y=new_X_train[variables[4]].tolist(), line={'color': 'red'},name="Original")
    fig_oil.update_xaxes(showgrid=True, gridwidth=1, gridcolor='gray',linewidth=1, linecolor='white',title_text='A??o')
    fig_oil.update_yaxes(showgrid=True, gridwidth=1, gridcolor='gray',linewidth=1, linecolor='white',title_text="Consumo (kT)")
    fig_oil.update_layout(title_text='Gases de efecto invernadero', title_x=0.5)


    # To change the order of magnitude
    new_X_train[variables[5]]=new_X_train[variables[5]].apply(lambda x: x/1000)
    new_X_futuro[variables[5]]=new_X_futuro[variables[5]].apply(lambda x: x/1000)

    fig_population=go.Figure()
    fig_population.add_scattergl(x=new_x, y=new_X_futuro[variables[5]], line={'color': color_pred},name="Prediccion")
    fig_population.add_scattergl(x=new_X_train.index.values, y=new_X_train[variables[5]].tolist(), line={'color': 'red'},name="Original")
    fig_population.update_xaxes(showgrid=True, gridwidth=1, gridcolor='gray',linewidth=1, linecolor='white',title_text='A??o')
    fig_population.update_yaxes(showgrid=True, gridwidth=1, gridcolor='gray',linewidth=1, linecolor='white',title_text="Miles de millones")
    fig_population.update_layout(title_text='PIB', title_x=0.5)

    # Uptade all figure layouts
    for figura in [fig_coal,fig_fosil2,fig_fosil,fig_gas,fig_oil,fig_population]:
        figura.update_layout({
          "plot_bgcolor": "#040d10",
          "paper_bgcolor": "#040d10",
          "font_color":"white",
          "title_font_color":"white"
        })
        figura.update_traces(line_width=5)


    return fig,texto,texto_loader,fig_coal,fig_fosil2,fig_fosil,fig_gas,fig_oil,fig_population

