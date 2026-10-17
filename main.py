import pandas as pd
import matplotlib.pyplot as plt

#pip install pandas openpyxl

# Data Collection
df = pd.read_csv("circ_dataset.csv")

# Data Cleaning
df =df.drop_duplicates()

player_name= df["player_name"].count()

group=df.groupby("role")
player_role=group["role"].count()


max_player = df.loc[df["total_runs"].idxmax()]
min_player = df.loc[df["total_runs"].idxmin()]

strike_rate_max_player = df.loc[df["strike_rate"].idxmax()]
strike_rate_min_player = df.loc[df["strike_rate"].idxmin()]

total_balls_faced_max = df.loc[df["total_balls_faced"].idxmax()]
total_balls_faced_min = df.loc[df["total_balls_faced"].idxmin()]

total_wickets_taken_max = df.loc[df["total_wickets_taken"].idxmax()]
total_wickets_taken_min = df.loc[df["total_wickets_taken"].idxmin()]

total_runs_conceded_max = df.loc[df["total_runs_conceded"].idxmax()]
total_runs_conceded_min = df.loc[df["total_runs_conceded"].idxmin()]

total_overs_bowled_max = df.loc[df["total_overs_bowled"].idxmax()]
total_overs_bowled_min = df.loc[df["total_overs_bowled"].idxmin()]

total_matches_played_max = df.loc[df["total_matches_played"].idxmax()]
total_matches_played_min = df.loc[df["total_matches_played"].idxmin()]

matches_played_as_batter_max = df.loc[df["matches_played_as_batter"].idxmax()]
matches_played_as_batter_min = df.loc[df["matches_played_as_batter"].idxmin()]

matches_played_as_bowler_max = df.loc[df["matches_played_as_bowler"].idxmax()]
matches_played_as_bowler_min = df.loc[df["matches_played_as_bowler"].idxmin()]

matches_won_max=df.loc[df["matches_won"].idxmax()]
matches_won_min=df.loc[df["matches_won"].idxmin()]

matches_lost_max=df.loc[df["matches_lost"].idxmax()]
matches_lost_min=df.loc[df["matches_lost"].idxmin()]

player_of_match_awards_max=df.loc[df["player_of_match_awards"].idxmax()]
player_of_match_awards_min=df.loc[df["player_of_match_awards"].idxmin()]

average_max=df.loc[df["average"].idxmax()]
average_min=df.loc[df["average"].idxmin()]

percentage_max=df.loc[df["percentage"].idxmax()]
percentage_min=df.loc[df["percentage"].idxmin()]



print("Player name count:",player_name)
print("Player role count:",player_role)
print("PlayerName:", max_player["player_name"],"Max Runs:", max_player["total_runs"])
print("PlayerName:", min_player["player_name"],"Min Runs:", min_player["total_runs"])

print("PlayerName :", strike_rate_max_player["player_name"],"StrikeRate :", strike_rate_max_player["strike_rate"])
print("PlayerName :", strike_rate_min_player["player_name"],"StrikeRate :", strike_rate_min_player["strike_rate"])

print("PlayerName :", total_balls_faced_max["player_name"],"total_balls_faced_max :", total_balls_faced_max["total_balls_faced"])
print("PlayerName :", total_balls_faced_min["player_name"],"total_balls_faced_min :", total_balls_faced_min["total_balls_faced"])

print("PlayerName :", total_wickets_taken_max["player_name"],"total_wickets_taken_max :", total_wickets_taken_max["total_wickets_taken"])
print("PlayerName :", total_wickets_taken_min["player_name"],"total_balls_faced_min :", total_wickets_taken_min["total_wickets_taken"])

print("PlayerName :", total_runs_conceded_max["player_name"],"total_runs_conceded_max :", total_runs_conceded_max["total_runs_conceded"])
print("PlayerName :", total_runs_conceded_min["player_name"],"total_runs_conceded_min :", total_runs_conceded_min["total_runs_conceded"])

print("PlayerName :", total_overs_bowled_max["player_name"],"total_overs_bowled_max:", total_overs_bowled_max["total_overs_bowled"])
print("PlayerName :", total_overs_bowled_min["player_name"],"total_overs_bowled_min :", total_overs_bowled_min["total_overs_bowled"])

# Total Matches Played
print("PlayerName :", total_matches_played_max["player_name"],"Total Matches Played Max :", total_matches_played_max["total_matches_played"])

print("PlayerName :", total_matches_played_min["player_name"],"Total Matches Played Min :", total_matches_played_min["total_matches_played"])

# Matches Played as Batter
print("PlayerName :", matches_played_as_batter_max["player_name"],"Batter Matches Max :", matches_played_as_batter_max["matches_played_as_batter"])

print("PlayerName :", matches_played_as_batter_min["player_name"],"Batter Matches Min :", matches_played_as_batter_min["matches_played_as_batter"])

# Matches Played as Bowler
print("PlayerName :", matches_played_as_bowler_max["player_name"],"Bowler Matches Max :", matches_played_as_bowler_max["matches_played_as_bowler"])

print("PlayerName :", matches_played_as_bowler_min["player_name"],"Bowler Matches Min :", matches_played_as_bowler_min["matches_played_as_bowler"])

# Matches Won
print("PlayerName :", matches_won_max["player_name"],"Matches Won Max :", matches_won_max["matches_won"])

print("PlayerName :", matches_won_min["player_name"],"Matches Won Min :", matches_won_min["matches_won"])

# Matches Lost
print("PlayerName :", matches_lost_max["player_name"],"Matches Lost Max :", matches_lost_max["matches_lost"])

print("PlayerName :", matches_lost_min["player_name"],"Matches Lost Min :", matches_lost_min["matches_lost"])

# Player of the Match Awards
print("PlayerName :", player_of_match_awards_max["player_name"],"POM Awards Max :", player_of_match_awards_max["player_of_match_awards"])

print("PlayerName :", player_of_match_awards_min["player_name"],"POM Awards Min :", player_of_match_awards_min["player_of_match_awards"])

print("Batting Average")
print("PlayerName :", average_max["player_name"],"Average Max :", average_max["average"])
print("PlayerName :", average_min["player_name"],"Average Min :", average_min["average"])

# Winning Percentage
print("PlayerName :", percentage_max["player_name"],"Winning Percentage Max :", percentage_max["percentage"])
print("PlayerName :", percentage_min["player_name"],"Winning Percentage Min :", percentage_min["percentage"])


matches_won_top = df.sort_values("matches_won").head(10)

plt.figure(figsize=(12, 6))
plt.plot(matches_won_top["player_name"],matches_won_top["matches_won"],marker="o",linewidth=2)
plt.title("Top 10 players Won Match")
plt.xlabel("Player Name")
plt.ylabel("Matches Won")

plt.tight_layout()
plt.show()

matches_lost_top=df.sort_values("matches_lost").head(10)
plt.figure(figsize=(12,6))
plt.plot(matches_lost_top["player_name"],matches_lost_top["matches_lost"],marker="o",linewidth=2)
plt.title("Top 10 players Lost Match")
plt.xlabel("Player Name")
plt.ylabel("Matches Lost")

plt.tight_layout()
plt.show()



total_runs_top=df.sort_values("total_runs").head(10)

plt.figure(figsize=(12,6))

bar=plt.bar(total_runs_top["player_name"],total_runs_top["total_runs"],linewidth=2)
plt.bar_label(bar, padding=3, fontsize=9)

plt.title("top 10 players Total Runs")
plt.xlabel("Player Name")
plt.ylabel("Total runs")

plt.tight_layout()
plt.show()

total_balls_faced_top=df.sort_values("total_balls_faced").head(10)

plt.figure(figsize=(12,6))

bar_total_balls_faced=plt.bar(total_balls_faced_top["player_name"],total_balls_faced_top["total_balls_faced"],linewidth=2)
plt.bar_label(bar_total_balls_faced, padding=3, fontsize=9)

plt.title("top 10 players Total Balls Faced")
plt.xlabel("Player Name")
plt.ylabel("Total balls Faced")

plt.tight_layout()
plt.show()


strike_rate_top=df.sort_values("strike_rate").head(10)
plt.figure(figsize=(16,8))

plt.scatter(strike_rate_top["total_runs"], strike_rate_top["strike_rate"])
plt.xlabel("Total Runs")
plt.ylabel("Strike Rate")
plt.show()


top10 = (df.sort_values("strike_rate").head(10))
plt.figure(figsize=(18,9))

plt.hist(top10["strike_rate"],edgecolor="black")

plt.title("Strike Rate Distribution (Top 10 Players)")
plt.xlabel("Strike Rate")
plt.ylabel("Number of Players")

plt.tight_layout()
plt.show()