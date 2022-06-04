import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

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


### LAYOUT AND CONTENT

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


### Callbacks

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/national":
        return national.layout
    elif pathname == "/regional":
        return regional.layout
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
    app.run_server(port=8888,debug=True)