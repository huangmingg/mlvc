import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
from mlvc.pages.company_page import render as render_company
from mlvc.pages.home_page import render as render_home
from mlvc.pages.predict_page import render as render_predict

app = dash.Dash(
    __name__, 
    suppress_callback_exceptions=True, 
    external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def routing(pathname):
    if pathname == '/home/':
        return render_home()
    elif pathname == '/company/':
        return render_company()
    elif pathname == '/predict/':
        return render_predict()    
    else:
        pass

def main():
    app.run_server(debug=True, port=30000)

if __name__ == '__main__':
    main()