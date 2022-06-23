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
                            html.A(className="btn btn-secondary mx-3 border border-rounded text-black my-2", href="/prediction",children=[dbc.NavLink(className="text-black",children="Predicción de temperatura", href="/prediction", active="exact"),]),
                            html.A(className="btn btn-secondary mx-3 border border-rounded text-black my-2", href="/description",children=[dbc.NavLink(className="text-black",children="Ver datos hasta la fecha", href="/description", active="exact"),]),

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
        html.Section(className="text-white text-center container",children=[
            html.H3(className="text-center pb-5",children="Conoce a nuestro equipo")
        ]),
        html.Section(className="card-deck justify-content-around px-5 row text-white" ,children=[
            html.Div(className="col-xs-1 col-sm-1 col-md-3 d-flex justify-content-center",children=[
                html.Div(className="card card-person px-4 pt-4 pb-0",style={"width": "16rem"} ,children=[
                    html.Img(src="../assets/img/elsa.jpeg", alt="",className="card-img-top image-person"),
                    html.Div(className="card-body",children=[
                        html.H5(className="card-title",children="Elsa Magnolia Quicazan Rubio"),
                        
                        html.Div(className="d-flex justify-content-center mt-2",children=[
                            
                            html.A(className="mx-2 text-center",href="https://www.linkedin.com/in/elsaquicazanrubio/", target="_blank",children=[
                                html.Div(className="img__wrap text-center",children=[
                                    html.Span(className="social-icon social-linkedin text-center",children=[
                                        html.I(className="bi bi-linkedin fa-lg text-center")
                                    ]),
                                    html.P(className="img__description",children="LinkedIn")
                                ])
                            ]),
                        
                            html.A(className="mx-2 text-center",href="https://scholar.google.com/citations?hl=en&user=HIRj5dMAAAAJ&view_op=list_works&gmla=AJsN-F5jTRk_68bA_LuoApaP9QlGKHfEFsO7h5qZS-7RwSB6eyQHpj2-P4gGUiCWkLkrhGLfvM4Do6_b0MFRRJpe7BMWN9CQYDP6XiblZCQFOqguz5AKlRM", target="_blank",children=[
                                html.Div(className="img__wrap text-center",children=[
                                    html.Span(className="social-icon text-center",children=[
                                        html.Img(className="scholar-google text-center", src="../assets/img/icons/icons8-google-scholar2.svg", alt="Google scholar")
                                    ]),
                                    html.P(className="img__description",children="Google Scholar")
                                ])
                            ]),
                        
                        
                            html.A(className="mx-2 text-center",href="https://bioinspirada.com/", target="_blank",children=[
                                html.Div(className="img__wrap text-center",children=[
                                    html.Span(className="social-icon text-center",children=[
                                        html.Img(className="bioinspirada w-50 text-center",src="../assets/img/icons/bioinspirada.png", alt="Personal Page")
                                    ]),
                                    html.P(className="img__description",children="Personal Page")
                                ]),
                                
                            ])
                            
                        
                        ])
                        
                    ])
                    
                ]),
                
            ]),
            html.Div(className="col-xs-1 col-sm-1 col-md-3 d-flex justify-content-center",children=[
                html.Div(className="card card-person px-4 pt-4 pb-0 ",style={"width": "16rem"}, children=[
                    html.Img(src="../assets/img/gabriela.jpeg", alt="",className="card-img-top image-person"),
                    html.Div(className="card-body",children=[
                        html.H5(className="card-title",children="Gabriela Rincón Ariza"),
                        
                        html.Div(className="d-flex justify-content-center mt-2",children=[
                            
                            html.A(className="mx-2 text-center",href="https://www.linkedin.com/in/gabriela-rincon-ariza", target="_blank",children=[
                                html.Div(className="img__wrap text-center",children=[
                                    html.Span(className="social-icon social-linkedin text-center",children=[
                                        html.I(className="bi bi-linkedin fa-lg text-center")
                                    ]),
                                    html.P(className="img__description",children="LinkedIn")
                                ])
                            ]),

                            html.A(className="mx-2 text-center",href="https://github.com/GabrielaR-14", target="_blank",children=[
                                html.Div(className="img__wrap text-center",children=[
                                    html.Span(className="social-icon social-github text-center",children=[
                                        html.I(className="bi bi-github fa-lg text-center")
                                    ]),
                                    html.P(className="img__description",children="Github")
                                ])
                            ]),
                                      
                        ])
                        
                    ])
                    
                ]),
                
            ]),
            
            html.Div(className="col-xs-1 col-sm-1 col-md-3 d-flex justify-content-center",children=[
                html.Div(className="card card-person px-4 pt-4 pb-0",style={"width": "16rem"}, children=[
                    html.Img(src="../assets/img/oscar.jpeg", alt="",className="card-img-top image-person"),
                    html.Div(className="card-body",children=[
                        html.H5(className="card-title",children="Oscar Eduardo Rosero Ordoñez"),
                        
                        html.Div(className="d-flex justify-content-center mt-2",children=[
                            
                            html.A(className="mx-2 text-center",href="https://www.linkedin.com/in/oscrosero24/", target="_blank",children=[
                                html.Div(className="img__wrap text-center",children=[
                                    html.Span(className="social-icon social-linkedin text-center",children=[
                                        html.I(className="bi bi-linkedin fa-lg text-center")
                                    ]),
                                    html.P(className="img__description",children="LinkedIn")
                                ])
                            ]),

                            html.A(className="mx-2 text-center",href="https://github.com/Osc2405", target="_blank",children=[
                                html.Div(className="img__wrap text-center",children=[
                                    html.Span(className="social-icon social-github text-center",children=[
                                        html.I(className="bi bi-github fa-lg text-center")
                                    ]),
                                    html.P(className="img__description",children="Github")
                                ])
                            ]),

                            html.A(className="mx-2 text-center",href="https://github.com/Osc2405", target="_blank",children=[
                                html.Div(className="img__wrap text-center",children=[
                                    html.Span(className="social-icon social-twitter text-center",children=[
                                        html.I(className="bi bi-twitter fa-lg text-center")
                                    ]),
                                    html.P(className="img__description",children="Twitter")
                                ])
                            ]),
                                      
                        ])
                        
                    ])
                    
                ]),
                
            ]),





            html.Div(className="col-3",children=[
                html.Div(className="card card-person px-4 pt-4 pb-0",style={"width": "16rem"}, children=[
                    html.Img(src="https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png", alt="",className="card-img-top image-person"),
                    html.Div(className="card-body",children=[
                        html.H5(className="card-title",children="Ana"),
                        
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
                html.Div(className="card card-person px-2 pt-4 pb-0",style={"width": "16rem"}, children=[
                    html.Img(src="https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png", alt="",className="card-img-top image-person"),
                    html.Div(className="card-body",children=[
                        html.H5(className="card-title",children="Luis"),
                        
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
                html.Div(className="card card-person px-2 pt-4 pb-0",style={"width": "16rem"}, children=[
                    html.Img(src="https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png", alt="",className="card-img-top image-person"),
                    html.Div(className="card-body",children=[
                        html.H5(className="card-title",children="Juan Camilo"),
                        
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
                html.Div(className="card card-person px-2 pt-4 pb-0",style={"width": "16rem"}, children=[
                    html.Img(src="https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png", alt="",className="card-img-top image-person"),
                    html.Div(className="card-body",children=[
                        html.H5(className="card-title",children="Andres"),
                        
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