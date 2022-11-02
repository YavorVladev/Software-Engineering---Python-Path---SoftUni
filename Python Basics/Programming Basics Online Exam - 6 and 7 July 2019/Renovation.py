import math

wall_height = int(input())
wall_width = int(input())
percent_not_painted = int(input())

total_surface = wall_height * wall_width * 4
total_surface = math.ceil(total_surface - (total_surface / 100 * percent_not_painted))


input_command = input()
while input_command != "Tired!":
    total_surface -= int(input_command)

    if total_surface <= 0:
        break
    input_command = input()


if total_surface > 0:
    print(f"{total_surface} quadratic m left.")
elif total_surface == 0:
    print(f"All walls are painted! Great job, Pesho!")
else:
    print(f"All walls are painted and you have {abs(total_surface)} l paint left!")