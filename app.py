#Imports
from sre_parse import State
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html,State, callback
import pathlib
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import pickle
import numpy as np
from callbacks import register_callbacks


# Path where local datasets are located

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("datasets").resolve()

# Read dataset with static values
df_finalCSV='https://raw.githubusercontent.com/ajrianop/projectDS4A/main/df_final.csv'
df=pd.read_csv(df_finalCSV,encoding='unicode_escape')

#suppress_callback_exceptions gives us the debug marker in the layout. 
app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP,dbc.icons.FONT_AWESOME],
    update_title='Cargando...', suppress_callback_exceptions=False
)
server = app.server

app.config.suppress_callback_exceptions=True


## Import other pages
from pages import prediction,home,regional,about,graficas,tabs_national,tabs_regional,home2, description,description_2
from pages.elements import nat_forest,nat_temperature,reg_forest,reg_temperature


# Path of the logo
PLOTLY_LOGO = "../assets/img/Logo.png"

### CUSTOM COMPONENTS
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
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px"),className="logo_navbar rounded-circle text-center"),
                        dbc.Col(dbc.NavbarBrand("ECO Temp", className="ms-2 text-white")),
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
                            html.I(className="bi bi-graph-up me-2"),
                            html.Span("Predicción",className="text-white"),
                        ],
                        href="/prediction",
                        active="exact",
                        className="text-white"
                    ),
                    dbc.NavLink(
                        [
                            html.I(className="fa-solid fa-chart-simple me-2"),
                            html.Span("Descripción",className="text-white"),
                        ],
                        href="/description",
                        active="exact",
                        className="text-white"
                    ),
                    dbc.NavLink(
                        [
                            html.I(className="fa-solid fa-people-group me-2"),
                            html.Span("About us",className="text-white"),
                        ],
                        href="/about",
                        active="exact",
                        className="text-white"
                    )]

            ),
        ]
    ),
    color="dark",
    id="navbar"
)




content = html.Div(id="page-content", className="content")


# App layout
app.layout = html.Div([dcc.Location(id="url"), navbar,content])

### Callbacks

# Routes callback
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home2.layout
    elif pathname == "/prediction":
        return prediction.layout
    elif pathname == "/description":
        return  description_2.layout
    elif pathname == "/about":
        return about.layout
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





# Toggle navbar Callback
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open



# Call to external function to register all callbacks
register_callbacks(app)


if __name__ == "__main__":
    app.run_server(debug=False, host="0.0.0.0", port=8080)

