import pandas as pd

df1 = pd.read_csv("players.csv")
df2 = pd.read_csv("teams.csv")
df3 = pd.merge(df1, df2, left_on='TEAM_ID', right_on="TEAM_ID")

df3 = pd.DataFrame(df3)

nome_do_time = input("Digite o nome do time: \n")

temporada = int(input("Digite a temporada: \n"))

time = df3.query("`NICKNAME` == @nome_do_time and `SEASON` == @temporada")

print(time)
