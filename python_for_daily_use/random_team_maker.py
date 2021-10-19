"""
This program was made to equally (if possible) distribute players randomly among any number of teams.
"""

import random

print('Enter names of players separating with space and press enter when finished: ')
players = input().split(" ")

# creating lists of teams
print('Enter team names separating with space and press enter when finished: ')
team_names = input().split(" ")

# creating a list having lists for different teams
teams = [[] for x in team_names]

# randomly allocating players to different teams
while len(players) >= 1:
    for x in teams:
        if len(players) < 1:
            break
        random_number = random.randint(0, len(players) - 1)
        player = players.pop(random_number)
        x.append(player)

# now players are allocated to two different teams
# now let's name both the teams randomly
for x in range(len(team_names)):
    random_team = team_names.pop(random.randint(0, len(team_names)-1))
    print("Team ", random_team, ":")
    for y in teams[x]:
        print(y)
    print("\n", end="")
