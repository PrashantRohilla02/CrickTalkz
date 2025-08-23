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
    if team1 in list(set(matches['team1'].unique())) and team2 in list(set(matches['team1'].unique())):
        temp = matches[((matches['team1'] == team1) & (matches['team2'] == team2)) | ((matches['team1'] == team2) & (matches['team2'] == team1))]
        total_matches = temp.shape[0]

        matches_won_team1 = temp[temp["winner"] == team1].shape[0]
        matches_won_team2 = temp[temp["winner"]== team1].shape[0]

        comparison = {
                "total match":total_matches,
                "match_won_team1":int(matches_won_team1),
                "match_won_team2":int(matches_won_team2)
            }
        return comparison
    else:
        return {
            "error":"Team name dosen't exist"   
        }
    
def teamRecord(team):
    if team in list(set(matches['team1'].unique())):
        total_matches = matches[(matches["team1"] == team) | (matches["team2"] == team)]
        matches_won = (total_matches["winner"] == team).sum()
        max_runs_scored = total_matches["target_runs"].max()
        lowest_runs_scored = total_matches["target_runs"].min()

        AllTeams = matches['team1'].unique()

        against = {team2 : teamVteamAPI(team,team2) for team2 in AllTeams if team2 != team}

        record = {
                    "total_matches":int(total_matches.shape[0]),
                    "matches_won":int(matches_won),
                    "matches_lost":int(total_matches.shape[0] - matches_won),
                    "max_runs_scored":int(max_runs_scored),
                    "lowest_runs_scored":int(lowest_runs_scored),
                    "average_runs_scored":int(total_matches["target_runs"].mean())
                    
            }
        
        data = {
            team:{ 
                "Overall":record,
                "Against":against
                }
        }
        return data
    
    else:
        return {
            "error":"Team name dosen't exist"
        }