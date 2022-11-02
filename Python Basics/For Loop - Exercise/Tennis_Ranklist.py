import math
tournament_count = int(input())
init_points = int(input())
sum_points = 0
win_count = 0
for i in range(1, tournament_count + 1):
    level = input()
    if level == "W":
        win_count = win_count + 1
        sum_points = sum_points + 2000
    elif level == "F":
        sum_points = sum_points + 1200
    elif level == "SF":
        sum_points = sum_points + 720
total_points = sum_points + init_points
print(f"Final points: {total_points}")
avg_points = math.floor(sum_points / tournament_count)
print(f"Average points: {avg_points}")
percent_win = win_count / tournament_count * 100
print(f"{percent_win:.2f}%")