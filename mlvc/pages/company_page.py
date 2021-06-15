import dash_html_components as html
import dash_core_components as dcc
import dash_dangerously_set_inner_html
import pandas as pd
import dash_table
from env import env

def create_data_table(df):
    table = dash_table.DataTable(
        id="database-table",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        sort_action="native",
        sort_mode="single",
        page_size=300,
    )
    return table

def create_dataframe():
    df = pd.read_csv("data/crunchbase.csv")
    return df

df = create_dataframe()

def render():
    template = env.get_template("company.html")
    nav_bar = dash_dangerously_set_inner_html.DangerouslySetInnerHTML(template.render())
    return html.Div(children=[nav_bar,
                dcc.Graph(
                    id="histogram-graph",
                    figure={
                        "data": [
                            {
                                "x": df["location"],
                                "text": df["location"],
                                "name": "something.",
                                "type": "histogram",
                            }
                        ],
                        "layout": {
                            "title": "Some graph you want to plot.",
                            "height": 500,
                            "padding": 150,
                        },
                    },
                ),
                create_data_table(df),
            ])
