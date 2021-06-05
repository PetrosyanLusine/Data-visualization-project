import pandas as pd


def GetTransfers():
    transfers = pd.read_csv("top250-00-19.csv")
    transfers["Team_to"] = transfers["Team_to"].str.replace("Spurs","Tottenham Hotspur")
    transfers["Team_to"] = transfers["Team_to"].str.replace("Man City","Manchester City")
    transfers["Team_to"] = transfers["Team_to"].str.replace("Man Utd","Manchester United")
    transfers["Team_to"] = transfers["Team_to"].str.replace("Birmingham","Birmingham City")
    transfers["Team_to"] = transfers["Team_to"].str.replace("Blackburn","Blackburn Rovers")
    transfers["Team_to"] = transfers["Team_to"].str.replace("Bolton","Bolton Wanderers")
    transfers["Team_to"] = transfers["Team_to"].str.replace("Brighton","Brighton & Hove Albion")
    transfers["Team_to"] = transfers["Team_to"].str.replace("Cardiff","Cardiff City")
    transfers["Team_to"] = transfers["Team_to"].str.replace("Charlton","Charlton Athletic")
    transfers["Team_to"] = transfers["Team_to"].str.replace("Derby","Derby County")
    transfers["Team_to"] = transfers["Team_to"].str.replace("Huddersfield","Huddersfield Town")
    transfers["Team_to"] = transfers["Team_to"].str.replace("Ipswich","Ipswich Town")
    transfers["Team_to"] = transfers["Team_to"].str.replace("Leeds","Leeds United")
    transfers["Team_to"] = transfers["Team_to"].str.replace("Leicester","Leicester City")
    transfers["Team_to"] = transfers["Team_to"].str.replace("Newcastle","Newcastle United")
    transfers["Team_to"] = transfers["Team_to"].str.replace("Norwich","Norwich City")
    transfers["Team_to"] = transfers["Team_to"].str.replace("QPR","Queens Park Rangers")
    transfers["Team_to"] = transfers["Team_to"].str.replace("Sheffield Utd.","Sheffield United")
    transfers["Team_to"] = transfers["Team_to"].str.replace("Swansea","Swansea City")
    transfers["Team_to"] = transfers["Team_to"].str.replace("West Brom","West Bromwich Albion")
    transfers["Team_to"] = transfers["Team_to"].str.replace("West Ham","West Ham United")
    transfers["Team_to"] = transfers["Team_to"].str.replace("Wigan","Wigan Athletic")
    transfers["Team_to"] = transfers["Team_to"].str.replace("Wolves","Wolverhampton Wanderers")
    return transfers

def GetChampionsLeagueResults():
    ChampionsLeague = pd.read_csv("ChampionsLeague.csv")
    return ChampionsLeague

def GetEnglandResults():
    England = pd.read_csv("England.csv")
    return England


def GetItalyResults():
    Italy = pd.read_csv("Italy.csv")
    return Italy

def GetGermanyResults():
    Germany = pd.read_csv("Germany.csv")
    return Germany

def GetSpainResults():
    Spain = pd.read_csv("Spain.csv")
    return Spain