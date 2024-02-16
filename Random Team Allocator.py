import random
all_players = ["Harry", "Connor", "Amy", "Sally", "Tom", "Penny", "Leonard", "Bernadette", "Sheldon", "Howard"]  # list to be assigned to 2 teams
team1 = []
team2 = []
player_number = 0

for i in range(5):  # to ensure there are equal numbers of players in each team
    player_number = all_players[random.randrange(0, len(all_players))]  # picks random player
    team1.append(player_number)  #  assigns to team 1
    all_players.remove(player_number)  # removes from selection list
    player_number = all_players[random.randrange(0, len(all_players))]  # picks another player
    team2.append(player_number)  # assigns to team 2
    all_players.remove(player_number)  # removes from selection list

print("Team 1 is:")
for i in range(len(team1)):  # prints teams without list format
    print(team1[i])
print("")
print("Team 2 is:")
for i in range(len(team2)):
    print(team2[i])
