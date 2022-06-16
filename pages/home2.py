from pydoc import classname
import dash
from dash import dcc,html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

from app import app

#Datos de ejemplo
fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])
#fig.update_layout(plot_bgcolor='#ffffff',paper_bgcolor= "#21222d")  Esta linea permite modificar el color del fondo, pero queda horrible, aunque es un inicio

## Layout national
layout=html.Div( className="seccion_home",
    children=[
        html.Header(
            className="masthead",children=[
                html.Div(className="container px-4 px-lg-5 d-flex h-100 align-items-center justify-content-center",children=[
                    html.Div(className="d-flex justify-content-center", children=[
                        html.Div(className="text-center",children=[
                            html.H1(className="mx-auto my-0 text-uppercase", children="ECO Rest"),
                            html.H2(children="Algun texto o frease introductoria",className="text-white-50 mx-auto mt-2 mb-5"),
                            #html.A(className="btn btn-secondary mx-3  border border-rounded text-black", href="/prediction",children="Predicción de temperatura"),
                            #html.A(className="btn btn-secondary mx-3 border border-rounded text-black", href="/description",children="Ver datos hasta la fecha"),
                            html.A(className="btn btn-secondary mx-3 border border-rounded text-black", href="/prediction",children=[dbc.NavLink(className="text-black",children="Predicción de temperatura", href="/prediction", active="exact"),]),
                            html.A(className="btn btn-secondary mx-3 border border-rounded text-black", href="/description",children=[dbc.NavLink(className="text-black",children="Ver datos hasta la fecha", href="/description", active="exact"),]),

                        ])
                    ])
                ])
            ]
        ),
        html.Section(className="seccion_home",children=[
            html.Div(className="container pt-4 pt-lg-5 text-white",children=[
                html.Div(className="row gx-0 mb-4 mb-lg-5 align-items-start pt-5 text-white justify-content-between",children=[
                    html.Div(className="col-5 text-center",children=[
                        html.H4(children="Nuestro proyecto"),
                        html.P(children="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Dictum sollicitudin condimentum nunc, lorem in lorem sit mattis. In ultrices egestas enim interdum ut tincidunt scelerisque. Orci, leo, fames duis duis et. Etiam feugiat sem porttitor odio id sit.",className="text-justify"),
                        html.Img(src="../assets/img/embrace-the-world.png",className="w-50")
                    ]),
                    html.Div(className="col-5 align-items-",children=[
                        html.H4(children="Objetivos"),
                        html.Ul(className="",children=[
                            html.Li(className="",children="Objetivo 1"),
                            html.Li(className="",children="Objetivo 2"),
                            html.Li(className="",children="Objetivo 3")
                        ]),
                    ])
                ])
            ])
        ]),
        #Start about us section
        html.Section(className="text-white text-center",children=[
            html.H3(className="text-center pb-5",children="Conoce a nuestro equipo")
        ]),
        html.Section(className="card-deck justify-content-around px-5 row text-white" ,children=[
            html.Div(className="col-3",children=[
                html.Div(className="card card-person px-4 pt-4 pb-0", children=[
                    html.Img(src="https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png", alt="",className="card-img-top image-person"),
                    html.Div(className="card-body",children=[
                        html.H5(className="card-title",children="Elsa"),
                        html.P(className="card-text",children="Titulo"),
                        html.Div(className="d-flex justify-content-center mt-2",children=[
                            
                            html.A(href="https://www.google.com", target="_blank",children=[
                                html.Span(className="social-icon social-linkedin",children=[
                                    html.I(className="bi bi-linkedin")
                                ])
                            ]),
                        
                            html.A(href="https://www.google.com", target="_blank",children=[
                                html.Span(className="social-icon social-twitter",children=[
                                    html.I(className="bi bi-twitter")
                                ])
                            ]),
                        
                        
                            html.A(href="https://www.google.com", target="_blank",children=[
                                html.Span(className="social-icon social-github",children=[
                                    html.I(className="bi bi-github")
                                ])
                            ])
                            
                        
                        ])
                        
                    ])
                    
                ]),
                
            ]),
            html.Div(className="col-3",children=[
                html.Div(className="card card-person px-4 pt-4 pb-0", children=[
                    html.Img(src="https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png", alt="",className="card-img-top image-person"),
                    html.Div(className="card-body",children=[
                        html.H5(className="card-title",children="Gabriela"),
                        html.P(className="card-text",children="Titulo"),
                        html.Div(className="d-flex justify-content-center mt-2 card-body",children=[
                            
                            html.A(href="https://www.google.com", target="_blank",children=[
                                html.Span(className="social-icon social-linkedin",children=[
                                    html.I(className="bi bi-linkedin")
                                ])
                            ]),
                            
                            
                            html.A(href="https://www.google.com", target="_blank",children=[
                                html.Span(className="social-icon social-twitter",children=[
                                    html.I(className="bi bi-twitter")
                                ])
                            ]),
                            
                            
                            html.A(href="https://www.google.com", target="_blank",children=[
                                html.Span(className="social-icon social-github",children=[
                                    html.I(className="bi bi-github")
                                ])
                            ])
                            
                        ])
                    ])
                    
                ])
                    
            ]),
            html.Div(className="col-3",children=[
                html.Div(className="card card-person px-4 pt-4 pb-0", children=[
                    html.Img(src="https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png", alt="",className="card-img-top image-person"),
                    html.Div(className="card-body",children=[
                        html.H5(className="card-title",children="Andres"),
                        html.P(className="card-text",children="Titulo"),
                        html.Div(className="d-flex justify-content-center mt-2",children=[
                            
                            html.A(href="https://www.google.com", target="_blank",children=[
                                html.Span(className="social-icon social-linkedin",children=[
                                    html.I(className="bi bi-linkedin")
                                ])
                            ]),
                        
                            html.A(href="https://www.google.com", target="_blank",children=[
                                html.Span(className="social-icon social-twitter",children=[
                                    html.I(className="bi bi-twitter")
                                ])
                            ]),
                        
                        
                            html.A(href="https://www.google.com", target="_blank",children=[
                                html.Span(className="social-icon social-github",children=[
                                    html.I(className="bi bi-github")
                                ])
                            ])
                            
                        
                        ])
                        
                    ])
                    
                ]),
                
            ]),
            html.Div(className="col-3",children=[
                html.Div(className="card card-person px-4 pt-4 pb-0", children=[
                    html.Img(src="https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png", alt="",className="card-img-top image-person"),
                    html.Div(className="card-body",children=[
                        html.H5(className="card-title",children="Ana"),
                        html.P(className="card-text",children="Titulo"),
                        html.Div(className="d-flex justify-content-center mt-2",children=[
                            
                            html.A(href="https://www.google.com", target="_blank",children=[
                                html.Span(className="social-icon social-linkedin",children=[
                                    html.I(className="bi bi-linkedin")
                                ])
                            ]),
                        
                            html.A(href="https://www.google.com", target="_blank",children=[
                                html.Span(className="social-icon social-twitter",children=[
                                    html.I(className="bi bi-twitter")
                                ])
                            ]),
                        
                        
                            html.A(href="https://www.google.com", target="_blank",children=[
                                html.Span(className="social-icon social-github",children=[
                                    html.I(className="bi bi-github")
                                ])
                            ])
                            
                        
                        ])
                        
                    ])
                    
                ]),
                
            ]),
                
            ]),
             
        html.Section(className="card-deck justify-content-around px-5 row text-white pt-3" ,children=[
            html.Div(className="col-3",children=[
                html.Div(className="card card-person px-2 pt-4 pb-0", children=[
                    html.Img(src="https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png", alt="",className="card-img-top image-person"),
                    html.Div(className="card-body",children=[
                        html.H5(className="card-title",children="Luis"),
                        html.P(className="card-text",children="Titulo"),
                        html.Div(className="d-flex justify-content-center mt-2",children=[
                            html.Ul(className="list-social",children=[
                            html.Li(children=[
                                html.A(href="https://www.google.com", target="_blank",children=[
                                    html.Span(className="social-icon social-linkedin",children=[
                                        html.I(className="bi bi-linkedin")
                                    ])
                                ])
                            ]),
                            html.Li(children=[
                                html.A(href="https://www.google.com", target="_blank",children=[
                                    html.Span(className="social-icon social-twitter",children=[
                                        html.I(className="bi bi-twitter")
                                    ])
                                ])
                            ]),
                            html.Li(children=[
                                html.A(href="https://www.google.com", target="_blank",children=[
                                    html.Span(className="social-icon social-github",children=[
                                        html.I(className="bi bi-github")
                                    ])
                                ])
                            ])
                        ])
                        ])
                        
                    ])
                    
                ])
            ]),
            html.Div(className="col-3",children=[
                html.Div(className="card card-person px-2 pt-4 pb-0", children=[
                    html.Img(src="https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png", alt="",className="card-img-top image-person"),
                    html.Div(className="card-body",children=[
                        html.H5(className="card-title",children="Juan Camilo"),
                        html.P(className="card-text",children="Titulo"),
                        html.Div(className="d-flex justify-content-center mt-2",children=[
                            html.Ul(className="list-social",children=[
                            html.Li(children=[
                                html.A(href="https://www.google.com", target="_blank",children=[
                                    html.Span(className="social-icon social-linkedin",children=[
                                        html.I(className="bi bi-linkedin")
                                    ])
                                ])
                            ]),
                            html.Li(children=[
                                html.A(href="https://www.google.com", target="_blank",children=[
                                    html.Span(className="social-icon social-twitter",children=[
                                        html.I(className="bi bi-twitter")
                                    ])
                                ])
                            ]),
                            html.Li(children=[
                                html.A(href="https://www.google.com", target="_blank",children=[
                                    html.Span(className="social-icon social-github",children=[
                                        html.I(className="bi bi-github")
                                    ])
                                ])
                            ])
                        ])
                        ])
                        
                    ])
                    
                ])
            ]),
            html.Div(className="col-3",children=[
                html.Div(className="card card-person px-2 pt-4 pb-0", children=[
                    html.Img(src="https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png", alt="",className="card-img-top image-person"),
                    html.Div(className="card-body",children=[
                        html.H5(className="card-title",children="Oscar"),
                        html.P(className="card-text",children="Titulo"),
                        html.Div(className="d-flex justify-content-center mt-2",children=[
                            html.Ul(className="list-social",children=[
                            html.Li(children=[
                                html.A(href="https://www.google.com", target="_blank",children=[
                                    html.Span(className="social-icon social-linkedin",children=[
                                        html.I(className="bi bi-linkedin")
                                    ])
                                ])
                            ]),
                            html.Li(children=[
                                html.A(href="https://www.google.com", target="_blank",children=[
                                    html.Span(className="social-icon social-twitter",children=[
                                        html.I(className="bi bi-twitter")
                                    ])
                                ])
                            ]),
                            html.Li(children=[
                                html.A(href="https://www.google.com", target="_blank",children=[
                                    html.Span(className="social-icon social-github",children=[
                                        html.I(className="bi bi-github")
                                    ])
                                ])
                            ])
                        ])
                        ])
                        
                    ])
                    
                ])
            ]),
        ]),
        #End about us section
        html.Section(className="seccion_datos py-3 text-white text-center container pt-4 pt-lg-5",children=[
            html.H2("Nuestro pais en datos",className="py-3"),
            html.Div(className="row justify-content-between",children=[
                html.Div(className="col",children=[
                    html.H4("Temperatura",className="py-3"),
                    dcc.Graph(figure=fig)
                ]),
                html.Div(className="col",children=[
                    html.H4("Bosques",className="py-3"),
                    dcc.Graph(figure=fig)
                ]),
                html.Div(className="col",children=[
                    html.H4("Poblacion",className="py-3"),
                    dcc.Graph(figure=fig)
                ])
            ]),
            html.Div(className="text-center py-5",children=[
                html.H2(children="Revisa nuestros datos",className="text-white mx-auto mt-2 mb-5"),
                html.A(className="btn btn-secondary mx-3 border border-rounded text-black", href="/prediction",children=[dbc.NavLink(className="text-black",children="Predicción de temperatura", href="/prediction", active="exact"),]),
                html.A(className="btn btn-secondary mx-3 border border-rounded text-black", href="/description",children=[dbc.NavLink(className="text-black",children="Ver datos hasta la fecha", href="/description", active="exact"),]),
            ])
        ])

    ]
)