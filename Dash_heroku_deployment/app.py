import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pickle
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

# ------------------------------------------------------------------------------
# Import data
df = pd.read_csv("export.df_supervised_rev1_land_homes.csv")
# df["period"] = df["Year"].astype(str) + '_' + df["Month"].astype(str)

# def loadmodel(filename):
    # loaded_model = pickle.load(open(filename, 'rb'))
    # return loaded_model
# model = loadmodel('finalized_model.pkl')
# ------------------------------------------------------------------------------

# lists of provinces
options1 = sorted(df["Province"].unique().tolist())

# lists of types
# options2 = sorted(df["Housing_Type"].unique().tolist())

# dictionary of Provinces - cities

all_options = (df.groupby('Province')
              .apply(lambda x: [y for y in x['City'].unique()])
              .to_dict())

# we add as first subcategory for each category `all`
for k, v in all_options.items():
    all_options[k].insert(0, 'all')


app.layout = html.Div([
    html.H1("Modelling housing market during COVID-19", style={'text-align': 'center'}),

    dcc.Markdown('''
![housing market](https://github.com/lskerrett/Covid_and_Real_Estate_Canada/blob/master/Resources/housing%20market.jpg?raw=true)


#### Links to Google Slides:

#### - [Project presentation](https://docs.google.com/presentation/d/1XloGJetDxiyN7Yh3OSNy-hipRLcIVP5_HimekSp4Ru0/edit?usp=sharing)


## **1._Description of the project** 

### ***Overview***

#### In Canada, the job market is remarkably concentrated in the big cities of the provinces across the country. This situation leads to higher demand of real state and rent activity in such cities, and many developers rely on such predictable outcome to invest. However, the economy in 2020 has been deeply affected by the COVID-19 pandemic which forced many to work from home, being no longer necessary to look for lodging in the big cities. In this  situation, it is important for private developers to know if COVID-19 has affected significantly the housing market in big and small cities across Canada. We are aiming to provide insight on how much the real estate market has changed in the months of the pandemic using as an  indicator the **House Price Index (HPI)**. We developed a tool to visualize the HPI values in the pandemic months compared to the "business-as-usual" values which we predict by modeling using a machine learning algorithm approach.

#### We finally would like to include an interactive dashboard from which the user can see the results of such comparison.  

### ***The questions we hope to answer are: ***
  
#### - How was the real estate market impacted by COVID-19?
#### - Does the city size in terms of population density play a role in this impact?
  
  
### ***Data sources:***
  
#### We will use data from 3 differents sources:
  
#### - [Canadian Mortgage and Housing Corporation](https://www.cmhc-schl.gc.ca/en/data-and-research)
#### - [Statistics Canada](https://www150.statcan.gc.ca/n1/en/type/data?subject_levels=46)
#### - [Canadian Real Estate Association](https://creastats.crea.ca/en-CA/) 

### ***Produced Database samples:***

#### - New housing prices (price_index_clean.csv)
#### - Canadian population 2011-2016 (cleaned_canada_pop_2011_2016.csv)

## **2._Process**
 
#### A combination of unsupervised and supervised machine learning techniques will be used to gain a better understanding of the impact that Covid-19 has had on the real estate market. Unsupervised machine learning was used to first identify any strong relationships between features, and then supervised machine learning will be used to build a model which predicts the HPI for a particular city. Furthermore, this prediction can be later compared to the actual HPI in 2020 and determine if a particular city's real estate market was impacted.
####  
#### [GitHub Repository of the project](https://github.com/lskerrett/Covid_and_Real_Estate_Canada) 
####  
####  
    '''),

    dcc.Tabs(id='tabs-example', value='tab-1', style={
#        'width': '50%',
        'font-size': '220%',
        'fontColor': 'blue'
#        'height': '50%'
    }, children=[
        dcc.Tab(label='Analysis', value='tab-1'),
        dcc.Tab(label='HPI variation', value='tab-2'),
    ]),
    html.Div(id='tabs-example-content')
])

@app.callback(Output('tabs-example-content', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            # html.H3('Tab content 1'),
            dcc.Markdown('''


### **Part 1: Unsupervised machine learning**


### * ***Jupyter notebooks:***

#### - Unsupervised Modelling - rev7 - Housing.ipynb
#### - Unsupervised Modelling - rev7 - Land.ipynb


### * ***Model characteristics:***

#### -**Variables**: 
#### Price Index (HPI), Population Density, Year.

#### -**Model algorithm**: K-means 

### * ***Analysis of results***

#### Two separate analyses were performed using unsupervised machine learning. We analized separately the data for "land" and "home" housing type . Identified clusters are not clearly separated in the 3D plots for the two analyses, however some tendencies can be identified.

#### For the "Land" housing type data, we observed that in recent years the HPI has remained mostly steady while most of the points are concentrated in medium size cities and lower, with no particular change for the year 2020.


Figure 1. Unsupervised machine learning result visualization - Land housing type
![Unsupervised machine learning result visualization - Land](https://github.com/lskerrett/Covid_and_Real_Estate_Canada/blob/master/Resources/Unsupervised_ML_plot_land.PNG?raw=true)


#### As for the "Home" housing type data, it can be seen that a shift towards medium sized cities has been taking place over the past few years, with some points with lower HPI, and such tendency has been exacerbated in 2020.

Figure 2. Unsupervised machine learning result visualization - Home housing type
![Unsupervised machine learning result visualization - Home](https://github.com/lskerrett/Covid_and_Real_Estate_Canada/blob/master/Resources/Unsupervised_ML_plot_housing.PNG?raw=true)


#### To improve this analysis, more features, such as city economic health factors should be considered.

### **Part 2: Supervised machine learning**


### * ***Jupyter notebooks:***

#### - Supervised Modelling - rev1 - Homes.ipynb 
#### - Supervised Modelling - rev1 - Land.ipynb

#### Supervised machine learning (Neural Networks) were used to initially build a model, but due to the low accuracy of the preliminary models, a simpler supervised machine learning technique such as multiple variable linear regression was chosen.

#### We divided our 2015-2019 data into training and evaluation subsets in order to predict Price-Index without the effect of the 2020 pandemic.

#### Low fit factors were obtained, implying that this analysis, although better than neural networks, still doesn't accurately depict a relationship between the features and the dependent variable (HPI).



### ***Analysis of results***


#### In the case of "Land" Housing type model, the coefficients tell us that the HPI has been increasing through the years, and that there is a slow market movement towards cities with high populaiton density.

Fig. 3. Supervised machine learning result summary - Land housing type

![Supervised machine learning result summary - Land](https://github.com/lskerrett/Covid_and_Real_Estate_Canada/blob/master/Resources/Supervised_ML_Summary_Land.PNG?raw=true)

#### As for the case of "House" Housing type model, the coefficients suggest also an increase of the HPI through the years. Nothing statistically sound can be said about the relationship between the population density and the HPI.

Fig. 4. Supervised machine learning result summary - Home housing type

![Supervised machine learning result summary - Home](https://github.com/lskerrett/Covid_and_Real_Estate_Canada/blob/master/Resources/Supervised_ML_Summary_Housing.PNG?raw=true)


## **3._Conclusion**

#### Overall, although both models has limitations given that the required data is hard to access, they can tell us that the House Price Index (HPI) had a tendency to increase through the years up to 2019, a year before the 2020 COVID-19 pandemic. Moreover, the data exploration phase showed us that in 2020 there was a shift towards medium sized cities in 2020 (COVID19 pandemic period) while HPI's increase rate has decreased. This suggests that the house market was indeed impacted, although as mentioned above, further features need to be considered to improve the models accuracy.
    ''')

        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3("VARIATION OF HOUSE PRICE INDEX PER CITY", style={'text-align': 'center'}),

            html.Br(),

            html.Div(
                children=[
                    html.Div([
                        html.Label("Select Province"),
                        dcc.Dropdown(
                            id='first-dropdown',
                            options=[{'label': k, 'value': k} for k in all_options.keys()],
                            value=options1[1]
                        ),
                    ],
                        className='six columns',style={'width': "30%"},
                    ),

                    html.Div([
                        html.Label("Select City"),
                        dcc.Dropdown(id='second-dropdown'
                        ),
                    ],
                        className='six columns',style={'width': "30%"},
                    ),
                    
                    html.Div([
                        html.Label("Select Housing type"),
                        dcc.Dropdown(id="third-dropdown",
                                    options=[
                                        {"label": "Land only", "value": "Land only"},
                                        {"label": "House only", "value": "House only"}],
                                    multi=False,
                                    value="House only"
                        ),
                    ],
                        className='six columns',style={'width': "30%"},
                    )
                ]
            ),

            html.Hr(),

            dcc.Graph(id='my_plot',figure={})
        ])




# app.layout = html.Div([
#     html.H1("VARIATION OF HOUSE PRICE INDEX PER CITY", style={'text-align': 'center'}),

#     html.Br(),

#     html.Div(
#         children=[
#             html.Div([
#                 html.Label("Select Province"),
#                 dcc.Dropdown(
#                     id='first-dropdown',
#                     options=[{'label': k, 'value': k} for k in all_options.keys()],
#                     value=options1[1]
#                 ),
#             ],
#                 className='six columns',style={'width': "30%"},
#             ),

#             html.Div([
#                 html.Label("Select City"),
#                 dcc.Dropdown(id='second-dropdown'
#                 ),
#             ],
#                 className='six columns',style={'width': "30%"},
#             ),
            
#             html.Div([
#                 html.Label("Select Housing type"),
#                 dcc.Dropdown(id="third-dropdown",
#                             options=[
#                                 {"label": "Land only", "value": "Land only"},
#                                 {"label": "House only", "value": "House only"}],
#                             multi=False,
#                             value="House only"
#                 ),
#             ],
#                 className='six columns',style={'width': "30%"},
#             )
#         ]
#     ),

#     html.Hr(),

#     dcc.Graph(id='my_plot',figure={})
# ])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components

@app.callback(
    Output('second-dropdown', 'options'),
    [Input('first-dropdown', 'value')])
def set_2_options(first_option):
    return [{'label': i, 'value': i} for i in all_options[first_option]]

@app.callback(
    Output('second-dropdown', 'value'),
    [Input('second-dropdown', 'options')])
def set_2_value(available_options):
    return available_options[1]['value']

@app.callback(
    Output('my_plot', 'figure'),
    [Input('first-dropdown', 'value'),
     Input('second-dropdown', 'value'),
     Input('third-dropdown', 'value'),])
def update_graph(selected_first, selected_second, selected_third):
    if selected_second == 'all':
        ddf = df[df["Province"]==selected_first]
    else:
        ddf = df[(df["Province"]==selected_first) &
                 (df["City"]==selected_second) &
                 (df["Housing_Type"]==selected_third)]

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=ddf["REF_DATE"],
                   y=ddf["PRICE_INDEX_P"],
                   name='HPI Prediction',
                   marker = dict(size=15, color='red'),
                   mode='markers'))
    fig.add_trace(
        go.Scatter(x=ddf["REF_DATE"],
                   y=ddf["PRICE_INDEX"],
                   name='HPI',
                   marker = dict(size=15, color='green'),
                   mode='markers'))
    fig.update_layout(
#        title='    ',
        xaxis_title='Date',
        yaxis_title='House Price Index (HPI)',
        plot_bgcolor = 'white',
        paper_bgcolor = 'whitesmoke',
        font=dict(
            family='Verdana',
            size=16,
            color='black'),
        shapes = [dict(
            x0='2020-01-01', x1='2020-01-01', y0=0, y1=1, xref='x', yref='paper',
            line_width=2)],
        annotations=[dict(
            x='2020-01-01', y=0.05, xref='x', yref='paper',
            showarrow=False, xanchor='left', text='COVID-19 Pandemic Period Begins')])
    fig.update_xaxes(
        showline=True,
        linewidth=2,
        linecolor='black',
        mirror=True,
        showgrid=False)
    fig.update_yaxes(
        showline=True,
        linewidth=2,
        linecolor='black',
        mirror=True,
        showgrid=True,
        gridwidth=1,
        gridcolor='grey',
        range=[85, 125])


    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
