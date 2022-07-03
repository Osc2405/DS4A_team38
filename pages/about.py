import dash
from dash import dcc,html
import dash_bootstrap_components as dbc

from app import app

## Layout national
layout=html.Div(className="",
    children=[
        html.Div(className="pt-5"),
        html.Div(className="row seccion_home pt-5 pt-3 justify-content-around primera_parte",children=[
            html.Div(className="col-md-6",children=[
                html.H3(className="text-white text-center",children="Nuestro proyecto"),
                html.P(className="text-justify text-white",children=["ECO Temp nace en el programa "," ",html.A("DS4A-Colombia",href="https://www.correlation-one.com/data-science-for-all-colombia", className="enlace")," "," por parte del equipo 38 de la sexta cohorte. El objetivo es generar un proyecto que pueda impactar de forma positiva, pero a la vez que permita usar todos los conocimientos adquiridos durante el ciclo de formación. "]),
                html.Div(className="row",children=[
                    html.Div(className="brand-item col",children=[
                        html.Img(src="assets/img/correlation_one.jpg", className="brand_img")
                        ]),
                    html.Div(className="brand-item col",children=[
                        html.Img(src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Logo_MINTIC.svg/2560px-Logo_MINTIC.svg.png", className="brand_img")
                        ]),
                ]),
                ]),
            html.Div(className="col-md-4",children=[
                html.Div(className="row",children=[
                    html.Img(src="assets/img/Logo_with_text2.png",className="w-50")
                ]),
                ]),
            ]),
        #Start about us section
        html.Div(className="seccion_home pt-5 pt-3",children=[
            html.Section(className="text-white text-center container-fluid seccion_home",children=[
                html.H3(className="text-center pb-5",children="Conoce a nuestro equipo")
            ]),
            html.Section(className="card-deck justify-content-around px-5 row text-white container-fluid" ,children=[
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
                        html.Img(src=app.get_asset_url("../assets/img/gabriela.jpeg"), alt="",className="card-img-top image-person"),
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
                        html.Img(src=app.get_asset_url("../assets/img/oscar.jpeg"), alt="",className="card-img-top image-person"),
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





                html.Div(className="col-xs-1 col-sm-1 col-md-3 d-flex justify-content-center",children=[
                    html.Div(className="card card-person px-4 pt-4 pb-0 ",style={"width": "16rem"}, children=[
                        html.Img(src=app.get_asset_url("../assets/img/andres.jpg"), alt="",className="card-img-top image-person"),
                        html.Div(className="card-body",children=[
                            html.H5(className="card-title",children="Andres Jhovany Riaño Pulido"),
                            
                            html.Div(className="d-flex justify-content-center mt-2",children=[
                                
                                html.A(className="mx-2 text-center",href="https://github.com/ajrianop", target="_blank",children=[
                                    html.Div(className="img__wrap text-center",children=[
                                        html.Span(className="social-icon social-github text-center",children=[
                                            html.I(className="bi bi-github fa-lg text-center")
                                        ]),
                                        html.P(className="img__description",children="Github")
                                    ])
                                ]),

                                html.A(className="mx-2 text-center",href="https://www.linkedin.com/in/andres-jhovany-riano-pulido-975994202/", target="_blank",children=[
                                    html.Div(className="img__wrap text-center",children=[
                                        html.Span(className="social-icon social-linkedin text-center",children=[
                                            html.I(className="bi bi-linkedin fa-lg text-center")
                                        ]),
                                        html.P(className="img__description",children="LinkedIn")
                                    ])
                                ]),

                                html.A(className="mx-2 text-center",href="https://scienti.minciencias.gov.co/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0000071210", target="_blank",children=[
                                    html.Div(className="img__wrap text-center",children=[
                                        html.Span(className="social-icon social-github text-center",children=[
                                            html.I(className="bi bi-file-earmark-person fa-lg text-center")
                                        ]),
                                        html.P(className="img__description",children="CV")
                                    ])
                                ]),
                                          
                            ])
                            
                        ])
                        
                    ]),
                    
                ]),
                    
                ]),
            
            html.Section(className="card-deck justify-content-around px-5 row text-white container-fluid pb-5" ,children=[
            html.Div(className="col-xs-1 col-sm-1 col-md-3 d-flex justify-content-center",children=[
                html.Div(className="card card-person px-4 pt-4 pb-0",style={"width": "16rem"} ,children=[
                    html.Img(src="../assets/img/ana.jpg", alt="",className="card-img-top image-person"),
                    html.Div(className="card-body",children=[
                        html.H5(className="card-title",children="Ana María Cruz Pacheco"),
                        
                        html.Div(className="d-flex justify-content-center mt-2",children=[
                            
                            html.A(className="mx-2 text-center",href="https://www.linkedin.com/in/elsaquicazanrubio/", target="_blank",children=[
                                html.Div(className="img__wrap text-center",children=[
                                    html.Span(className="social-icon social-linkedin text-center",children=[
                                        html.I(className="bi bi-linkedin fa-lg text-center")
                                    ]),
                                    html.P(className="img__description",children="LinkedIn")
                                ])
                            ]),
                        
                                
                            ])
                            
                        
                        ])
                        
                    ])
                    
                ]),
                
            html.Div(className="col-xs-1 col-sm-1 col-md-3 d-flex justify-content-center",children=[
                html.Div(className="card card-person px-4 pt-4 pb-0 ",style={"width": "16rem"}, children=[
                    html.Img(src="https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png", alt="",className="card-img-top image-person"),
                    html.Div(className="card-body",children=[
                        html.H5(className="card-title",children="Luis"),
                        
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
                    html.Img(src="https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png", alt="",className="card-img-top image-person"),
                    html.Div(className="card-body",children=[
                        html.H5(className="card-title",children="Juan"),
                        
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
            ]),
        ])
             
        
        #End about us section
    ]
)