import pandas as pd
import numpy as np

matches = pd.read_csv("C:/Users/prash/CrickTalkz/DataSet/matches.csv")

# print(matches.head(5))

def teamsApi():
    teams = list(set(matches['team1'].unique()))
    teams_dict = {
        "teams":teams
    }

    return teams_dict

def teamVteamAPI(team1,team2):
    temp = matches[((matches['team1'] == team1) & (matches['team2'] == team2)) | ((matches['team1'] == team2) & (matches['team2'] == team1))]
    total_matches = temp.shape[0]

    matches_won_team1 = temp["winner"].value_counts()[team1]
    matches_won_team2 = temp["winner"].value_counts()[team2]

    comparison = {
            "total match":total_matches,
            "match_won_team1":int(matches_won_team1),
            "match_won_team2":int(matches_won_team2)
        }
    return comparison