import dash_bootstrap_components as dbc
from dash import html, dcc

dna_icon = html.I(className="fa-solid fa-dna")
scissors_icon = html.I(className="fa-solid fa-scissors")
upload_icon = html.I(
    className="fa-solid fa-cloud-arrow-up fa-2xl",
    style={"margin-top": "1%", "margin-bottom": "3%"},
)
download_icon = html.I(
    className="fa-solid fa-floppy-disk", style={"margin-right": "5px"}
)

site_header = dbc.Row(
    children=[
        dbc.Col(children=[
            html.H1(
                    id="gRNA-title",
                    children=[
                        scissors_icon,
                        "CRISPR Cas13 gRNA Design Tool",
                        dna_icon,
                    ],
                ),
        ])
    ]
)

sequence_input = dbc.Row(
    children=[
        dbc.Col(
            children=[
                dbc.Form(
                    children=[
                        dbc.Input(
                            id="seq-input",
                            placeholder="Input Sequence",
                            type="text",
                            value="",
                            autocomplete=False,
                        ),
                    ],
                ),
            ]
        )
    ]
)

download_button = dbc.Button(
    children=[
        download_icon,
        "Download Sequences",
        dcc.Download(id="gRNA-csv-download"),
    ],
    className="download-btn",
    title="Download gRNAs as CSV",
)


page_footer = dbc.Row(
    className="justify-content-center align-items-center",
    id="page-footer",
    children=[
        html.Div(
            children=[
                html.A(
                    children=[
                        "Caelan Miller",
                        html.I(
                            className="fa-brands fa-github fa-fw",
                            style={"margin": "auto"},
                        ),
                    ],
                    target="_blank",
                    href="https://github.com/caelanjmiller",
                    id="github-link",
                )
            ],
        ),
    ],
)