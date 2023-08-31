from dash import Dash, dash, callback, Input, Output, State
from dash.exceptions import PreventUpdate
from components import *
from sequence_manipulation import *

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.MINTY, dbc.icons.FONT_AWESOME, dbc_css],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)
# server = app.server
app._favicon = "assets/favicon.ico"
app.title = "Cas13 gRNA Design Tool"
app.layout = dbc.Container(
    id="main-container", fluid=False, children=[site_header, dbc.Row(id="body-content", children=[sequence_input]), page_footer]
)


@app.callback(
    Output(component_id="body-content", component_property="children"),
    Input(component_id="seq-input", component_property="n_submit"),
    State(component_id="seq-input", component_property="value"),
    prevent_initial_call=True,
)
def display_generated_gRNA_primers(n_submit: int, sequence_input: str):
    forward_primer = sequence_manipulation(sequence_input, "forward")
    reverse_primer = sequence_manipulation(sequence_input, "reverse")
    
    if (n_submit == 0) and (sequence_input == None):
        raise PreventUpdate
    else:
        results_component = dbc.Row(
            children=[
                html.H2(f"Forward Primer: {forward_primer}", className="result-seq"),
                html.H2(f"Reverse Primer: {reverse_primer}", className="result-seq"),
                download_button
            ]
        )
    
    return results_component


# Development Testing
if __name__ == "__main__":
    app.run(debug=True)

# Needed for server deployment later on
# if __name__ == "__main__":
#     server.run(host="0.0.0.0", port="8080")

# Author: Caelan Miller - 2023
