import dash_html_components as html
import dash_dangerously_set_inner_html
import dash_core_components as dcc
from env import env

def render():
    template = env.get_template("home.html")
    home_page = dash_dangerously_set_inner_html.DangerouslySetInnerHTML(template.render())
    return html.Div(children=[home_page])