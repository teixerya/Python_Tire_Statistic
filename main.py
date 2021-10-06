import dash
import plotly.express as px
# pd is short version of pandas
import pandas as pd

# Data Exploration with Pandas (python)
# -----------------------------------------------------------------

# df = pd.read_excel("tirestatistic.excel")
df = pd.read_csv("tirestatistic.csv")

print(df[:5])#print first 5 rows

#iloc is for numbers
print("\n" + str(df.iloc[:13, [2,3,3,4]]))   #print first 5 rows and select columns in the square brackets.
print("\n")
#loc is for string
print(df.loc[:5, ["Tire"]])   #print first 5 rows and select columns in the square brackets.
print()

print("Number of Tire Types: " + str(df.Tire_Type.nunique())) #Count number of unique categories. 12k rows in the table.
print("Name of Tire Types: " + str(df.Tire_Type.unique()))  #To see the unique category names.
print()

print("Expected kilometers Sorted: " + str(sorted(df.Expected_km.unique())) + "\n")

# Data Visualization with Plotly (Python)
# -----------------------------------------------------------------

#fig_pie variable name of pie chart.
#data_frame is df = pd.read_csv("tirestatistic.csv")
#Select Tire for names
#Select Values for Expected_km

fig_pie = px.pie(data_frame=df, names='Tire', values='Expected_km')
#fig_pie.show() used to display my pie chart.
fig_pie.show()

fig_pie2 = px.pie(data_frame=df, names='Tire', values='Price_USD')
fig_pie2.show()


#data_frame is df = pd.read_csv("tirestatistic.csv")
#Select Tire_Type for x
#Select Expected_km for y
fig_bar = px.bar(data_frame=df, x='Tire_Type', y='Expected_km')
fig_bar.show()

fig_hist = px.histogram(data_frame=df, x='Tire', y='Expected_km')
fig_hist.show()

fig_histprice = px.histogram(data_frame=df, x='Tire', y='Price_USD')
fig_histprice.show()

# Interactive Dash Graph (Python, R)
# -----------------------------------------------------------------

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

#copy and paste
app = dash.Dash(__name__)

#app.layout=html.Div([anything in here will be the layout})
app.layout=html.Div([
    #Title
    html.H1("Charm Data Graph Analysis"),
    #Drop down
    dcc.Dropdown(id='genre-choice',
                 options=[{'label':x, 'value':x}
                          #make sure Tires are unique
                          for x in sorted(df.Tire.unique())],
                 #Sports is the default drop down value
                 value='Bridgestone_R197'
                 ),
    #graph
    dcc.Graph(id='my-graph',
              figure={}),
])

#To make layout interactive
@app.callback(
    #id of the graph and component property is something inside the 'figure'
    Output(component_id='my-graph', component_property='figure'),
    #id of the drop down 'genre-choice' and the value of the drop down 'value'
    Input(component_id='genre-choice', component_property='value')
)

def interactive_graphs(value_tire):
    print(value_tire)
    #filter data frame with the chosen genre.
    dff = df[df.Tire==value_tire]
    #fig will fill the empty dictionary on line 76.
    fig = px.bar(data_frame=dff, x='Tire', y='Expected_km')
    return fig

#copy and paste
if __name__=='__main__':
    app.run_server()
