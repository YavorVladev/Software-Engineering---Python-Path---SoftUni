games_sold = int(input())
hearthstone = 0
fornite = 0
overwatch = 0
others = 0
for game in range(games_sold):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone += 1
    elif game_name == "Fornite":
        fornite += 1
    elif game_name == "Overwatch":
        overwatch += 1
    else:
        others += 1

hearthstone_per = hearthstone / games_sold * 100
fornite_per = fornite / games_sold * 100
overwatch_per = overwatch / games_sold * 100
others_per = others / games_sold * 100

print(f"Hearthstone - {hearthstone_per:.2f}%")
print(f"Fornite - {fornite_per:.2f}%")
print(f"Overwatch - {overwatch_per:.2f}%")
print(f"Others - {others_per:.2f}%")