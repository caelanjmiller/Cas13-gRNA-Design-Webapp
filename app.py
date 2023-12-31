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
server = app.server
app._favicon = "assets/favicon.ico"
app.title = "Cas13 gRNA Design Tool"
app.layout = dbc.Container(
    id="main-container",
    fluid=False,
    children=[
        dcc.Store(id="stored-data", storage_type="memory"),
        site_header,
        dbc.Row(id="body-content", children=[sequence_input_form]),
        page_footer,
    ],
)


@app.callback(
    Output(component_id="stored-data", component_property="data"),
    Input(component_id="seq-input", component_property="n_submit"),
    State(component_id="seq-input", component_property="value"),
    prevent_initial_call=True,
)
def store_sequence_input(n_submit: int, user_input: str):
    sequence_input = user_input.strip().upper()
    if (n_submit == 0) and (sequence_input == None):
        raise PreventUpdate
    else:
        return sequence_input


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
                download_button,
            ]
        )

    return results_component


@app.callback(
    Output(component_id="csv-download", component_property="data"),
    Input(component_id="download-btn", component_property="n_clicks"),
    Input(component_id="stored-data", component_property="data"),
)
def download_sequence_csv(n_clicks: int, sequence_input: str):
    forward_primer = sequence_manipulation(sequence_input, "forward")
    reverse_primer = sequence_manipulation(sequence_input, "reverse")
    if n_clicks is None:
        raise PreventUpdate
    else:
        primer_dataframe = create_sequences_csv(forward_primer, reverse_primer)
        return dcc.send_data_frame(primer_dataframe.to_csv, "Sequences.csv")


# Development Testing
if __name__ == "__main__":
    app.run(debug=True)

# Author: Caelan Miller - 2023
