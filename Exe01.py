import pandas as pd

players_df = pd.read_csv(r"C:\pythonProjects\Pandas\players.csv")
teams_df = pd.read_csv(r"C:\pythonProjects\Pandas\teams.csv")

for index, linha in players_df.iterrows():
    team_id = linha["TEAM_ID"]
    player_name = linha["PLAYER_NAME"]
    season = linha["SEASON"]

    #print(f"{index} - {team_id} - {player_name} - {season}")

jogador = players_df[ (players_df['PLAYER_NAME'] == "Zach LaVine") & (players_df["SEASON"] == 2015) ]
team_id = jogador["TEAM_ID"].values[0]

time = teams_df[ teams_df["TEAM_ID"] == team_id ]
print(time["NICKNAME"].values[0])