import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from test_streaming_api import stream_hashtags
from dash.dependencies import Input, Output
import pandas as pd

# stream_hashtags(['donald']) # return table

app = dash.Dash(__name__)

df = pd.read_csv('table.csv')

app.layout = html.Div([html.Div(html.H1('Twitter Stream')),
                        dcc.Input(id='input_1', type='text'),
                        dcc.Interval('interval', n_intervals=1000),
                        dash_table.DataTable(
                                            id='table-sorting-filtering',
                                            style_data={
                                                'whiteSpace': 'normal',
                                                'height': 'auto'
                                            },
                                            style_table={
                                                'maxHeight': '800px'
                                                ,'overflowY': 'scroll'
                                            },
                                            columns=[
                                                {'name': i, 'id': i} for i in df.columns
                                            ])])


@app.callback(Output('table-sorting-filtering', 'data'), 
              [Input('input_1', 'value'),
              Input('interval', 'n_intervals')])
def stream_interval(value, n_intervals):
    return stream_hashtags([value])
    

if __name__ == '__main__':
    app.run_server(debug=True)

