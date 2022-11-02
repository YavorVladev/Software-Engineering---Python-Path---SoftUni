side_a = int(input())
side_b = int(input())
side_c = int(input())
free_space_available = side_a * side_b * side_c
free_space_wanted = 0

input_command = input()

while input_command != "Done":
    boxes = int(input_command)
    free_space_wanted += boxes

    if free_space_wanted > free_space_available:
        break

    input_command = input()

diff = abs(free_space_wanted - free_space_available)

if free_space_wanted > free_space_available:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")