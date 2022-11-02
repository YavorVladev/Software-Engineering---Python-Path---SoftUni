team_name = input()
season_games = int(input())
points = 0
W_count = 0
D_count = 0
L_count = 0

if season_games == 0:
    print(f"{team_name} hasn't played any games during this season.")
    quit()

for matches in range(season_games):
    outcome = input()

    if outcome == "W":
        points += 3
        W_count += 1

    elif outcome == "D":
        points += 1
        D_count += 1

    else:
        L_count += 1

win_rate = W_count / season_games * 100
print(f"{team_name} has won {points} points during this season.")
print("Total stats:")
print(f"## W: {W_count}")
print(f"## D: {D_count}")
print(f"## L: {L_count}")
print(f"Win rate: {win_rate:.2f}%")
