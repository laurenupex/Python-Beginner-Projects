import random
all_players = ["Harry", "Connor", "Amy", "Sally", "Tom", "Penny", "Leonard", "Bernadette", "Sheldon", "Howard"]
team1 = []
team2 = []
player_number = 0

for i in range(5):
    player_number = all_players[random.randrange(0, len(all_players))]
    team1.append(player_number)
    all_players.remove(player_number)
    player_number = all_players[random.randrange(0, len(all_players))]
    team2.append(player_number)
    all_players.remove(player_number)

print("Team 1 is:")
for i in range(len(team1)):
    print(team1[i])
print("")
print("Team 2 is:")
for i in range(len(team2)):
    print(team2[i])
