from sre_parse import State
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html,State
import pathlib
import plotly.express as px
import pandas as pd


from callbacks import register_callbacks


# Df de las pruebas

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("datasets").resolve()

df_finalCSV='https://raw.githubusercontent.com/ajrianop/projectDS4A/main/df_final.csv'
df=pd.read_csv(df_finalCSV,encoding='unicode_escape')

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP,dbc.icons.FONT_AWESOME],
    update_title='Cargando...', suppress_callback_exceptions=True 
)

app.config.suppress_callback_exceptions=True

## Import other pages
from pages import national,home,regional,about,graficas,tabs_national,tabs_regional,home2, description
from pages.elements import nat_forest,nat_temperature,reg_forest,reg_temperature


PLOTLY_LOGO = "https://www.collinsdictionary.com/images/full/tree_267376982.jpg"

# Style of the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# Content style
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

### CUSTOM COMPONENTS

sidebar = html.Div(
    [
        html.H2("Corest", className="display-4"),
        html.Hr(),
        html.P(
            "lorem ipsum", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("National", href="/prediction", active="exact"),
                dbc.NavLink("Regional", href="/description", active="exact"),
                dbc.NavLink("About", href="/about", active="exact"),
                dbc.NavLink("Graficas", href="/graficas", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


sidebar_responsive_estasi= html.Nav(className="navbar navbar-inverse fixed-top",id="sidebar-wrapper", role="navigation",children=[
    html.Ul(className="nav sidebar-nav",children=[
        html.Div(className="sidebar-header",children=[
            html.Div(className="sidebar-brand",children=[
                html.A(href="/",children="ECO Rest")
                ])
            ]),
        html.Li(html.A(href="/home",children="Home")),
        html.Li(html.A(href="/prediction",children="Predicción")),
        html.Li(html.A(href="/description",children="Descripción"))
        ])
    ])


sidebar_responsive2=html.Div(className="container-fluid overflow-hidden",
    children=[
        html.Div(className="row vh-100 overflow-auto",
        children=[
            html.Div(className="col-12 col-sm-3 col-xl-2 px-sm-2 px-0 bg-black d-flex sticky-top",
            children=[
                html.Div(className="d-flex flex-sm-column flex-row flex-grow-1 align-items-center align-items-sm-start px-3 pt-4 text-white",
                children=[
                    dbc.NavLink(href="/", className="d-flex align-items-center pb-sm-3 mb-md-0 me-md-auto text-white text-decoration-none",
                    children=[
                        html.Img(src="https://www.collinsdictionary.com/images/full/tree_267376982.jpg", className="w-25 rounded-circle"),
                        html.Span("ECO REST",className="d-none d-md-inline p-2")
                        ]),
                    html.Br(),
                    dbc.Nav(className="nav nav-pills flex-sm-column flex-row flex-nowrap flex-shrink-1 flex-sm-grow-0 flex-grow-1 mb-sm-auto mb-0 justify-content-center align-items-center align-items-sm-start pt-5",id="menu",
                    children=[
                        dbc.NavLink(className="nav-item",href="/",active="exact",
                        children=[
                            html.I(className="fs-5 bi-house"),
                            html.Span("Home",className="ms-1 d-none d-sm-inline") 
                        ]),
                        dbc.NavLink(className="nav-item",href="/prediction",active="exact",
                        children=[
                            html.I(className="fa-solid fa-temperature-low"),
                            html.Span("Predicción",className="ms-1 d-none d-sm-inline") 
                        ]),
                        dbc.NavLink(className="nav-item",href="/description",active="exact",
                        children=[
                            html.I(className="bi bi-graph-up"),
                            html.Span("Area descriptiva",className="ms-1 d-none d-sm-inline") 
                        ]),
                        
                        
                    ])
            ])
            ]),
            html.Div(id="page-content",className="col d-flex flex-column h-100 nopadding")
        ]
        )
    ]
)




sidebar = html.Div(
    [
        html.Div(
            [
                html.Img(src=PLOTLY_LOGO, style={"width": "3rem"}),
                html.H2("ECO Rest",className="text-white"),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="fas fa-home me-2"), html.Span("Home")],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-calendar-alt me-2"),
                        html.Span("Predicción"),
                    ],
                    href="/prediction",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-envelope-open-text me-2"),
                        html.Span("Descripción"),
                    ],
                    href="/description",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)

navbar = dbc.Navbar(
    dbc.Container(className="justify-content-between",children=
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("ECO Rest", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                id="navbar-collapse",
                is_open=False,
                navbar=True,
                className="mr-auto",
                children=[
                    dbc.NavLink(
                        [html.I(className="fas fa-home me-2"), html.Span("Home",className="text-white")],
                        href="/",
                        active="exact",
                        className="text-white"
                    ),
                    dbc.NavLink(
                        [
                            html.I(className="fas fa-calendar-alt me-2"),
                            html.Span("Predicción",className="text-white"),
                        ],
                        href="/prediction",
                        active="exact",
                        className="text-white"
                    ),
                    dbc.NavLink(
                        [
                            html.I(className="fas fa-envelope-open-text me-2"),
                            html.Span("Descripción",className="text-white"),
                        ],
                        href="/description",
                        active="exact",
                        className="text-white"
                    )]

            ),
        ]
    ),
    color="dark",
    dark=True,
)



content = html.Div(id="page-content", className="content")

app.layout = html.Div([dcc.Location(id="url"), navbar, content])


### LAYOUT AND CONTENT




### Callbacks

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home2.layout
    elif pathname == "/prediction":
        return national.layout
    elif pathname == "/description":
        return  description.layout

##Enlaces no usados por ahora
    elif pathname == "/about":
        return about.layout
    elif pathname == "/graficas":
        return graficas.layout
    elif pathname == "/tabs_national":
        return tabs_national.layout
    elif pathname == "/tabs_regional":
        return tabs_regional.layout
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
    dbc.Container(
        [
            
            html.H1("404: Not found", className="display-3 text-danger"),
            html.P(
                f"The pathname {pathname} was not recognised...",
                className="lead",
            ),
            html.Hr(className="my-2"),

            
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-light rounded-3",
)


### CALLBACKS TABS NATIONAL ###

@app.callback(Output('content_national', 'children'),
              Input('tabs_national', 'value'))
def render_content(tab):
    if tab == 'tab_temperature':
        return nat_temperature.layout
    elif tab == 'tab_eforestation':
        return nat_forest.layout

### END CALLBACKS TABS NATIONAL ###

### CALLBACKS TABS REGIONAL ###

@app.callback(Output('content_regional', 'children'),
              Input('tabs_regional', 'value'))
def render_content(tab):
    if tab == 'tab_temperature_reg':
        return reg_temperature.layout
    elif tab == 'tab_eforestation_reg':
        return reg_forest.layout

### END CALLBACKS TABS REGIONAL ###



## CALLBACKS NATIONAL ##

## Callback Slider
@app.callback(
    Output("LandUsePie","figure"),
    Output("LandUseLines","figure"),
    [Input("year_slider","value")],
    [Input("land_use_drop","value")])

def update_output(value,value_drop):
    df_land=pd.read_csv(DATA_PATH.joinpath("landcoverFAO.csv"))
    df_land["Year"]=df_land["Year"].astype(int)
    df=df_land[(df_land["Year"]>=value[0]) & (df_land["Year"]<=value[1])]
    fig = px.pie(df,values="Value", names="Item")
    fig.update_layout(transition_duration=500)
    fig.update_layout(showlegend=False)

    if value_drop is None:
        fig2 = px.line(df,x="Year", y="Value",color="Item")
    else:
        dff=df[df.Item.str.contains('|'.join(value_drop))]
        fig2 = px.line(dff,x="Year", y="Value",color="Item")
    fig2.update_layout(transition_duration=500)
    fig2.update_layout(showlegend=False)
    return fig,fig2

@app.callback(
    Output('parrafo', 'children'),
    [Input('year_slider', 'value')])
def update_output(value):
    string_exit='Estas viendo datos desde {} hasta {}'.format(value[0],value[1])
    return string_exit


@app.callback(
    Output("forestvs","figure"),
    [Input("year_slider","value")],
    [Input("forestvs_drop","value")]
)
def forestvs(year,variable):
    df_data=pd.read_csv(DATA_PATH.joinpath("output_merge.csv"))
    df=df_data[(df_data["year"]>=year[0]) & (df_data["year"]<=year[1])]
    if variable is None:
        fig2 = px.line(df,x="year",y=df.columns[1:])
    else:
        variable.append("year")
        dff=df[variable]
        fig2 = px.line(dff,x="year", y=dff.columns[:-1])
    fig2.update_layout(transition_duration=500)
    fig2.update_layout(showlegend=False)
    return fig2

## END CALLBACKS NATIONAL ##

## START CALLBACKS DESCRIPTION ##

@app.callback(
    Output("indicador_barras","figure"),
    Output("plot_area_contaminacion","figure"),
    Output("plot_area_poblacion","figure"),
    Output("text_year","children"),
    Output("indicador_temperatura","children"),
    Output("indicador_co2","children"),
    Output("indicador_forest","children"),
    Output("indicador_poblacion","children"),
    [Input("year_slider_d","value")],
    [Input("contamination_drop","value")]
)
def plot_barras(year,variable):
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
    texto_co2="{:.2f} U".format((df_barras.iloc[-1]["co2"]))
    texto_forest="{:.2f} U".format((df_barras.iloc[-1]["Forest area"]))
    texto_poblacion="{:.2f} Millones".format((df_barras.iloc[-1]["population"])/1000000)
    

    return fig,fig2,fig3,texto_year,texto_temp,texto_co2,texto_forest,texto_poblacion

## END CALLBACKS DESCRIPTION


@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


#CALLBACKS GRAFICAS


# Call to external function to register all callbacks
register_callbacks(app)


if __name__ == "__main__":
    app.run_server(debug=True)


