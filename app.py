import random
import datetime
import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# ---- Sensor Simulation ----
def generate_sensor_data():
    temp = random.randint(25, 40)
    hum = random.randint(40, 90)
    time = datetime.datetime.now()
    return temp, hum, time

# ---- Data Storage ----
df = pd.DataFrame(columns=["Time", "Temperature", "Humidity"])

# ---- Dash App ----
app = Dash(__name__)

app.layout = html.Div(style={"fontFamily": "Arial", "padding": "20px"}, children=[

    html.H1("IoT Temperature & Humidity Monitoring Dashboard",
            style={"textAlign": "center"}),

    dcc.Dropdown(
        id="sensor-dropdown",
        options=[
            {"label": "Temperature", "value": "Temperature"},
            {"label": "Humidity", "value": "Humidity"},
            {"label": "Both", "value": "Both"}
        ],
        value="Both",
        clearable=False
    ),

    dcc.Graph(id="line-chart"),
    dcc.Graph(id="bar-chart"),
    dcc.Graph(id="gauge-chart"),

    dcc.Interval(
        id="interval",
        interval=1000,
        n_intervals=0
    )
])

@app.callback(
    [Output("line-chart", "figure"),
     Output("bar-chart", "figure"),
     Output("gauge-chart", "figure")],
    Input("interval", "n_intervals"),
    Input("sensor-dropdown", "value")
)
def update_dashboard(n, selected):
    global df
    temp, hum, time = generate_sensor_data()
    df.loc[len(df)] = [time, temp, hum]

    # Line chart
    lines = []
    if selected in ["Temperature", "Both"]:
        lines.append(go.Scatter(x=df["Time"], y=df["Temperature"],
                                mode="lines", name="Temperature"))
    if selected in ["Humidity", "Both"]:
        lines.append(go.Scatter(x=df["Time"], y=df["Humidity"],
                                mode="lines", name="Humidity"))

    line_fig = go.Figure(lines)
    line_fig.update_layout(title="Live Sensor Trends")

    # Bar chart
    bar_fig = go.Figure([
        go.Bar(x=["Temperature", "Humidity"], y=[temp, hum])
    ])
    bar_fig.update_layout(title="Latest Readings")

    # Gauge chart
    gauge_fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=temp,
        title={"text": "Temperature Gauge (°C)"},
        gauge={"axis": {"range": [0, 50]}}
    ))

    return line_fig, bar_fig, gauge_fig

if __name__ == "__main__":
    app.run(port=8060, debug=False)

