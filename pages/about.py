import dash
#from dash import dcc,html
#import dash_bootstrap_components as dbc

from app import app

############The last try
############
from dash import dcc,html, callback,Input, Output,State
import dash_bootstrap_components as dbc
import pathlib
import pandas as pd
import plotly.express as px
#MAPA COLOMBIA
from components.maps.mapcol_departamentos import mapcol_departamentos


df_finalCSV='https://raw.githubusercontent.com/ajrianop/projectDS4A/main/df_final.csv'
df=pd.read_csv(df_finalCSV,encoding='unicode_escape')

departament_temperature_CSV='https://raw.githubusercontent.com/ajrianop/projectDS4A/main/code_department_temp.csv'
temp_department=pd.read_csv(departament_temperature_CSV,encoding='unicode_escape', dtype = {'COD_DPTO': str})

temp_department=temp_department.dropna(axis='rows')
erase_years_df_temp=['1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '2020']
temp_department=temp_department.drop(columns=erase_years_df_temp, axis=1)
departamentos=temp_department.DEPARTAMENTO.unique()

erase_years_df_pib=['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '2020']

#print(temp_department[temp_department['DEPARTAMENTO']=='CUNDINAMARCA']['latitude']),
#print(temp_department[temp_department['DEPARTAMENTO']=='CUNDINAMARCA']['longitude']),
LAT_CUN=temp_department[temp_department['DEPARTAMENTO']=='CUNDINAMARCA']['latitude']
LON_CUN=temp_department[temp_department['DEPARTAMENTO']=='CUNDINAMARCA']['longitude']
#print(temp_department.columns[1:43])

mapa_colombia_departamentos = mapcol_departamentos('Mapa Temperatura Colombia', 'div_departamentos_fig',temp_department)
mapa_colombia_departamentos_pib = mapcol_departamentos('Mapa PIB Colombia', 'div_departamentos_fig',temp_department)
mapa_colombia_departamentos_def = mapcol_departamentos('Mapa Deforestación Colombia', 'div_departamentos_fig',temp_department)
############
############


## Layout national
layout=html.Div(
    children=[
        html.H1(
            children="About page"
        ),
        html.P("We are interested in searching which are the main problems of deforestation in Colombia. Here we can see explicitly the changes along each year since 1990 to 2020",
        className="text-justify"),

        ## The last try
        ###############
        html.Section(className="text-white row pb-5",id="filtros-mapa", children=[

            html.Div(className="col-xs-12 col-sm-12 col-md-6 col-xl-6 pt-3",children=[
                html.H4(className="py-2 text-center",children="Filtros"),
                html.H5(className="py-2",children="Selecciona el rango de años a observar:"),
                dcc.RangeSlider(id="slider-updatemode", min=df["Year"].min(), max=df["Year"].max(),step=1,value=[df["Year"].min(),df["Year"].max()],marks=None, className="pt-4 pb-5",tooltip={"placement": "bottom", "always_visible": True}),
                html.H5("Selecciona un departamento", className="pt-3 pb-2"),
                dcc.Dropdown(id="id_selector_municipio",multi=False, placeholder="Selecciona un departamento...", options=[{'label': x, 'value': x} for x in departamentos]),
                dbc.Row([
                    dbc.Col([
                        dbc.Button(['Filtrar'],id="id_filtrar")
                        ],class_name="d-flex justify-content-end mt-2"),
                ]),
            ]),


            html.Div(className="col-xs-12 col-sm-12 col-md-6 col-xl-6 text-center pt-3", children=[
                html.Div(className="seccion_home px-4",
                    children=[
                        html.Div(id='my-output',children=[
                            html.Div([
                                    mapa_colombia_departamentos.display3(5.7489, -74.329597, '2000','Reds'),
                                    #mapa_colombia_departamentos.display3(LAT_CUN.iloc[-1], LON_CUN.iloc[-1], '2000'),
                                    #mapa_colombia_departamentos.display3(12.594563,-81.712957, temp_department['1990'])
                                    #dcc.Graph(id="plot_temperature_map",figure={})
                                ],className="container", id="row_map2") 
                        ]),
                    ]),

                    #####PARA BORRAR LUEGO
                    html.Div(className="d-flex flex-column justify-content-around",children=[
                        #html.H3("Info_drop", className="text-center text-black", id="Info_drop"),
                        html.H3("información departamento", className="text-center text-black", id="info_dep"),
                    ]),
                    #####PARA BORRAR LUEGO
                ]),
            ]),
        #############################
        #############################
        
    ]
)


## START CALLBACKS DESCRIPTION ##
""" @callback(
        [Output("row_map", 'children')], 
        #Output("Info_drop",'children'), 
        Output("texto_year",'children'),
        [State("id_selector_municipio", "value"), #selector_municipio
         State("slider-updatemode","value"), #selector_year
         Input("id_filtrar", "n_clicks"),   #nclicks    
        ],prevent_initial_call=True
    )
def update_map(selector_municipio,selector_year,nclicks):
        df_filtrado = mapa_colombia_departamentos.df[mapa_colombia_departamentos.df['DEPARTAMENTO'].isin(selector_municipio)]
        df_filtrado = df_filtrado[df_filtrado['COUNT']<(10**selector_year)]
        mapa_colombia_departamentos.df = df_filtrado
        nuevo_mapa = mapa_colombia_departamentos.display()
        #mapa_filtrado = mapcol_departamentos('Mapa Filtrado', 'id_filtrado', df_filtrado )
        #nuevo_mapa = mapa_filtrado.display()
        #info_drop=f'Info_drop{selector_municipio}'
        texto_year=f'Año desde {selector_year[0]} hasta {selector_year[1]}'
        #return [nuevo_mapa],info_drop, texto_year
        return [nuevo_mapa], texto_year """
@callback(
    Output("row_map2", 'children'),
    Output("info_dep","children"),
    #Output("last_year", "children"),
    Input("id_selector_municipio", "value"),
    [Input("slider-updatemode", "value")]
)

def update_map(depart,years):
    if not depart:
        info_dep_temp=f'Temperatura en Colombia, año {str(years[1])}'
        fig4=mapa_colombia_departamentos.display3(5.7489, -74.329597, str(years[1]),'Reds'),
    else:
        LAT_CUN_DEP=temp_department[temp_department['DEPARTAMENTO']==depart]['latitude']
        LON_CUN_DEP=temp_department[temp_department['DEPARTAMENTO']==depart]['longitude']
        LAT_CUN_DEP=float(LAT_CUN_DEP.iloc[0])
        LON_CUN_DEP=float(LON_CUN_DEP.iloc[0])
        info_dep_temp=f'Temperatura en {depart}, año {str(years[1])}'
        fig4=mapa_colombia_departamentos.display3(LAT_CUN_DEP, LON_CUN_DEP, str(years[1], 'Reds'),'dense')
        #fig4=mapa_colombia_departamentos.display3(5.7489, -74.329597, str(years[1]))
    return fig4,info_dep_temp
    #return info_dep #[fig4],info_dep


## END CALLBACKS DESCRIPTION