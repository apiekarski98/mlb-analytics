import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
file = pd.read_csv("baseballdata.csv")

red_sox = file[file.Tm=='Boston Red Sox']

# Gather Red Sox wins each year
red_sox_wins = pd.DataFrame([red_sox.Year, red_sox.W])
red_sox_wins = red_sox_wins.transpose()

# Create a bar graph of the Red Sox data
red_sox_wins_plot = plt.bar(red_sox_wins.Year, red_sox_wins.W, width=.25)
plt.title("Red Sox Wins by Year")
plt.xlabel("Year")
plt.ylabel("Number of Wins")
plt.xlim(xmin=min(red_sox_wins.Year))
# plt.show()

# Plot teams by mean wins
unique_teams = file.Tm.unique()
mean_team_wins = pd.DataFrame()

for team in unique_teams:
    temp = file[file.Tm == team]
    mean_wins = temp['W'].mean()
    mean_team_wins[team] = [mean_wins]

mean_team_wins = mean_team_wins.transpose()
print(mean_team_wins.attribute)

# mean_wins_plot = plt.bar(mean_team_wins.index, mean_team_wins.mean_wins)
# plt.show()