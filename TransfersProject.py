import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output, State
import DataPrep as dp

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

def plot_clwinners():
    clWinnersCount = ChampionsLeague.groupby("Winner").count().reset_index()
    clWinnersCount = clWinnersCount.rename(columns = {"Season":"Count"}).sort_values("Count", ascending = False)
    return px.bar(clWinnersCount, x = 'Winner', y = "Count", title = "Champions league winners")

def plot_mostexpensiveplayers():
    mostExpensivePlayers = Transfers.sort_values("Transfer_fee",ascending = False).head(5)
    return px.bar(mostExpensivePlayers, x = 'Name', y = "Transfer_fee", title = "Top 5 of Most Expensive Players",  labels=dict(Transfer_fee = "Transfer fee"))

def plot_scatterAgeTransferFee():
    return px.scatter(Transfers, x = "Age", y = "Transfer_fee", title = "Scatter plot of age and transfer fee",  labels=dict(Transfer_fee = "Transfer fee"))

def plot_mostTransferFeeTeams():
    df = Transfers.groupby("Team_to").sum().sort_values("Transfer_fee",ascending = False).reset_index()[['Team_to','Transfer_fee']].head(10)
    return px.bar(df, x = 'Team_to', y = "Transfer_fee", title = "Top 10 of teams with most transfer fees.", labels=dict(Team_to = "Team", Transfer_fee = "Transfer fee"))

def plot_scatterPointsTransferFeeSum():
    df = Transfers.groupby(["Team_to","Season"]).sum().reset_index()
    df = England.merge(df,left_on = ['Team','Season'],right_on = ['Team_to','Season'])
    return px.scatter(df, x = "Points", y = "Transfer_fee", title = "Scatter plot of points and transfer fee sum",  labels=dict(Transfer_fee = "Transfer fee"))

def plot_PositionTransferFee():
    df = Transfers.groupby("Position").mean().sort_values("Transfer_fee",ascending = False).reset_index()[['Position','Transfer_fee']]
    fig = px.bar(df, x = 'Position', y = "Transfer_fee", title = "Barplot of poition and transfer fee", labels=dict(Transfer_fee = "Transfer fee"))
    fig.update_xaxes(tickangle = 60)
    return fig


def rendercontent(tab):
    if tab == 'tab1':
        return [
    html.Div([
        html.Div([dcc.Graph(id = 'points')], className = 'eleven columns')
            ], className = 'row'),
   
    html.Div([
        html.Div([dcc.Dropdown(
                                id = 'league1',
                                options = [
                                       {'label': "England", 'value':"England"},
                                       {'label': "Germany", 'value':"Germany"},
                                       {'label': "Italy",   'value':"Italy"},
                                       {'label': "Spain",   'value':"Spain"}
        ], value = 'England')], className = 'three columns'),
        
        html.Div([dcc.Dropdown(
                                id = 'team1',
                                options = [
                                       {'label':team, 'value':team} for team in England["Team"].sort_values().unique()
        ], value = 'Chelsea')], className = 'three columns'),
        
        html.Div([dcc.Dropdown(
                                id = 'stats1',
                                options = [
                                      {'label': "Points",  'value':"Points"},
                                      {'label': "Win",     'value':"Win"},
                                      {'label': "Draw",    'value':"Draw"},
                                      {'label': "Lost",    'value':"Lost"},
                                      {'label': "Position",'value':"Position"},
                                      {'label': "Goals Scored",'value':"Goals Scored"},
                                      {'label': "Goals Missed",'value':"Goals Missed"}
        ], value = 'Points')], className = 'three columns'),
        
        html.Div([html.Button(id = 'plot1', n_clicks = 0, children = 'Plot')], className = 'two columns')
                 ], className = 'row'),
    
    #Top 10 most played clubs in leagues
    html.Div([
        html.Div(dcc.Graph(id = 'top10played'), className = 'six columns'),
        html.Div(dcc.Graph(id = 'top10stats'), className = 'six columns')]),
        
    
    html.Div([
        html.Div([dcc.Dropdown(
                                id = 'league2',
                                options = [
                                       {'label': "England", 'value':"England"},
                                       {'label': "Germany", 'value':"Germany"},
                                       {'label': "Italy",   'value':"Italy"},
                                       {'label': "Spain",   'value':"Spain"}
        ], value = 'England')], className = 'five columns'),
        
        html.Div([html.Button(id = 'plot2', n_clicks = 0, children = 'Plot')], className = 'one column'),
                 
        
        html.Div([dcc.Dropdown(
                                id = 'league3',
                                options = [
                                       {'label': "England", 'value':"England"},
                                       {'label': "Germany", 'value':"Germany"},
                                       {'label': "Italy",   'value':"Italy"},
                                       {'label': "Spain",   'value':"Spain"}
        ], value = 'England')], className = 'three columns'),
        
        html.Div([dcc.Dropdown(
                                id = 'stats2',
                                options = [
                                      {'label': "Points",  'value':"Points"},
                                      {'label': "Win",     'value':"Win"},
                                      {'label': "Draw",    'value':"Draw"},
                                      {'label': "Lost",    'value':"Lost"},
                                      {'label': "Goals Scored",'value':"Goals Scored"},
                                      {'label': "Goals Missed",'value':"Goals Missed"}
        ], value = 'Points')], className = 'two columns'),
        
        
        html.Div([html.Button(id = 'plot3', n_clicks = 0, children = 'Plot')], className = 'one column')]
                 
        
        ,className = 'row'),
        
    html.Div([
        html.Div([dcc.Graph(id = 'clwinners', figure = plot_clwinners() )], className = 'twelve columns')
            ], className = 'row'),
        
        ]
    
    elif tab == 'tab2':
        return html.Div([
        html.Div([
            html.Div([dcc.Graph(id = 'expensiveplayers', figure = plot_mostexpensiveplayers())], className = 'six columns'),
            html.Div([dcc.Graph(id = 'positions', figure = plot_PositionTransferFee())], className = 'six columns')],
        className = 'row'),
        html.Div([
            html.Div([dcc.Graph(id = 'agefee', figure = plot_scatterAgeTransferFee())], className = 'twelve columns')],
        className = 'row'),
        html.Div([
            html.Div([dcc.Graph(id = 'teamtransferfee', figure = plot_mostTransferFeeTeams())], className = 'twelve columns')],
        className = 'row'),
        html.Div([
            html.Div([dcc.Graph(id = 'pointstransferfee', figure = plot_scatterPointsTransferFeeSum())], className = 'twelve columns')],
        className = 'row')],
            className = 'container')


England = dp.GetEnglandResults()
Italy = dp.GetItalyResults()
Spain = dp.GetSpainResults()
Germany = dp.GetGermanyResults()
ChampionsLeague = dp.GetChampionsLeagueResults()
Transfers = dp.GetTransfers()

app = dash.Dash(external_stylesheets = external_stylesheets)

app.layout = html.Div([
#             html.Div([html.H1('Dash2 App')], className = 'row'),
                 dcc.Tabs(id='tabs-example', value='tab-1', children=[
                        dcc.Tab(label='Tab one', value='tab-1',children = rendercontent("tab1") ),
                        dcc.Tab(label='Tab two', value='tab-2', children = rendercontent("tab2")),
             ])], className = 'container')
            
#plot1
    
@app.callback(
       [Output(component_id = 'team1', component_property = 'options'),
        Output(component_id = 'team1', component_property = 'value')
       ],
        [Input(component_id = 'league1', component_property = 'value')]
)
def update_team_dropdown(input1):
    if input1 == 'England':
        return [{'label':team, 'value':team} for team in England["Team"].sort_values().unique()], "Chelsea"
    elif input1 == 'Italy': 
        return [{'label':team, 'value':team} for team in Italy["Team"].sort_values().unique()], "Milan"
    elif input1 == 'Spain': 
        return [{'label':team, 'value':team} for team in Spain["Team"].sort_values().unique()], "Real Madrid"
    else:
        return [{'label':team, 'value':team} for team in Germany["Team"].sort_values().unique()], "Bayern Munchen"

    
@app.callback(
       Output(component_id = 'points', component_property = 'figure'),
        [Input(component_id = 'plot1', component_property = 'n_clicks')],
          [State(component_id = 'league1', component_property = 'value'),
           State(component_id = 'team1', component_property = 'value'),
           State(component_id = 'stats1', component_property = 'value')]
)
def plot_points(n_clicks,league,team,stats):
    if stats == "Position":
        layout = go.Layout(title = team + " " + stats + " per season",  xaxis=dict(title="Seasons"),yaxis=dict(title=stats, autorange = "reversed"))
    else:    
        layout = go.Layout(title = team + " " + stats + " per season",  xaxis=dict(title="Seasons"),yaxis=dict(title=stats))
    
    if league == 'England':
        seasons = England[England["Team"] == team]["Season"]
        statvalues =  England[England["Team"] == team][stats]
    elif league == 'Italy': 
        seasons = Italy[Italy["Team"] == team]["Season"]
        statvalues =  Italy[Italy["Team"] == team][stats]
    elif league == 'Spain': 
        seasons = Spain[Spain["Team"] == team]["Season"]
        statvalues =  Spain[Spain["Team"] == team][stats]
    else:
        seasons = Germany[Germany["Team"] == team]["Season"]
        statvalues =  Germany[Germany["Team"] == team][stats]
    return go.Figure(data=go.Scatter(x = seasons, y = statvalues), layout = layout)

#plot2
@app.callback(
       Output(component_id = 'top10played', component_property = 'figure'),
        [Input(component_id = 'plot2', component_property = 'n_clicks')],
          [State(component_id = 'league2', component_property = 'value')]       
)
def plot_top10played(n_clicks, league):
    
    #layout = go.Layout(title = team + " " + stats + " per season",  xaxis=dict(title="Seasons"),yaxis=dict(title=stats))
    
    if league == 'England':
        playedCount = England.groupby("Team").Season.count().reset_index()
    elif league == 'Italy': 
        playedCount = Italy.groupby("Team").Season.count().reset_index()
    elif league == 'Spain': 
        playedCount = Spain.groupby("Team").Season.count().reset_index()
    else:
        playedCount = Germany.groupby("Team").Season.count().reset_index()
        
    playedCount = playedCount.rename(columns = {"Season":"Count"}).sort_values("Count", ascending = False).head(10)
    return px.bar(playedCount, x = 'Team', y = 'Count', title = "Top 10 teams who played most in " + league )

#plot3
@app.callback(
       Output(component_id = 'top10stats', component_property = 'figure'),
        [Input(component_id = 'plot3', component_property = 'n_clicks')],
          [State(component_id = 'league3', component_property = 'value'),
           State(component_id = 'stats2', component_property = 'value')]       
)
def plot_top10played(n_clicks, league,stats):
    
    if league == 'England':
        values = England.groupby("Team")[stats].sum().reset_index().sort_values(stats, ascending = False).head(10)
    elif league == 'Italy': 
        values = Italy.groupby("Team")[stats].sum().reset_index().sort_values(stats, ascending = False).head(10)
    elif league == 'Spain': 
        values = Spain.groupby("Team")[stats].sum().reset_index().sort_values(stats, ascending = False).head(10)
    else:
        values = Germany.groupby("Team")[stats].sum().reset_index().sort_values(stats, ascending = False).head(10)
    return px.bar(values, x = 'Team', y = stats, title = "Top 10 teams with most " + stats)



if __name__ == '__main__':
    app.run_server(debug = True)
    
    