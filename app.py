from sre_parse import State
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP]
)

## Import other pages
from pages import national,home,regional,about

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
                dbc.NavLink("National", href="/national", active="exact"),
                dbc.NavLink("Regional", href="/regional", active="exact"),
                dbc.NavLink("About", href="/about", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

sidebar_responsive=html.Div(className="container-fluid overflow-hidden",
    children=[
        html.Div(className="row vh-100 overflow-auto",
        children=[
            html.Div(className="col-12 col-sm-3 col-xl-2 px-sm-2 px-0 bg-dark d-flex sticky-top",
            children=[
                html.Div(className="d-flex flex-sm-column flex-row flex-grow-1 align-items-center align-items-sm-start px-3 pt-2 text-white",
                children=[
                    dbc.NavLink(href="/", className="d-flex align-items-center pb-sm-3 mb-md-0 me-md-auto text-white text-decoration-none",
                    children=[
                        html.Img(src="https://www.collinsdictionary.com/images/full/tree_267376982.jpg", className="w-25 rounded-circle"),
                        html.Span("COREST",className="d-none d-md-inline p-2")
                        ]),
                    html.Br(),
                    dbc.Nav(className="nav nav-pills flex-sm-column flex-row flex-nowrap flex-shrink-1 flex-sm-grow-0 flex-grow-1 mb-sm-auto mb-0 justify-content-center align-items-center align-items-sm-start pt-5",id="menu",
                    children=[
                        dbc.NavLink(className="nav-item",href="/",active="exact",
                        children=[
                            html.I(className="fs-5 bi-house"),
                            html.Span("Home",className="ms-1 d-none d-sm-inline") 
                        ]),
                        dbc.NavLink(className="nav-item",href="/national",active="exact",
                        children=[
                            html.I(className="fs-5 bi-tree-fill"),
                            html.Span("National",className="ms-1 d-none d-sm-inline") 
                        ]),
                        dbc.NavLink(className="nav-item",href="/regional",active="exact",
                        children=[
                            html.I(className="fs-5 bi-table"),
                            html.Span("Regional",className="ms-1 d-none d-sm-inline") 
                        ]),
                        dbc.NavLink(className="nav-item",href="/about",active="exact",
                        children=[
                            html.I(className="fs-5 bi-people-fill"),
                            html.Span("About",className="ms-1 d-none d-sm-inline") 
                        ]),
                        
                    ])
            ])
            ]),
            html.Div(id="page-content",className="col d-flex flex-column h-100")
        ]
        )
    ]
)


### LAYOUT AND CONTENT

content = html.Div(className="col d-flex flex-column h-100",
children=[html.Main(className="row")])

app.layout = html.Div([dcc.Location(id="url"), sidebar_responsive, content])


### Callbacks

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/national":
        return national.layout
    elif pathname == "/regional":
        return  regional.layout
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

if __name__ == "__main__":
    app.run_server(debug=True)