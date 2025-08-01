from flask import Flask,jsonify,request
import ipl

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

@app.route("/api/teams")
def teams():
    teams = ipl.teamsApi()
    return jsonify(teams)

@app.route("/api/team_vs_team")
def team_vs_team():
    team1 = request.args.get("team1")
    team2 = request.args.get("team2")
    responce = ipl.teamVteamAPI(team1,team2)
    return jsonify(responce)

if __name__ == "__main__":
    app.run(debug=True)