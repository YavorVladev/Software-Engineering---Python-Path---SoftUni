player_name = input()
points = 0
max_points = 0
winner = ""

while player_name != "Stop":
    points = 0
    for letter in player_name:
        digit = int(input())
        price = ord(letter)
        if digit == price:
            points += 10
        else:
            points += 2
    if points > max_points:
        max_points = points
        winner = player_name
    elif points == max_points:
        max_points = points
        winner = player_name

    player_name = input()

print(f"The winner is {winner} with {max_points} points!")