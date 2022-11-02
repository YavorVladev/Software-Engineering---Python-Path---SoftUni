side_a = int(input())
side_b = int(input())
full_cake = side_a * side_b

input_command = input()
while input_command != "STOP":
    curr_slices = int(input_command)
    full_cake -= curr_slices
    if full_cake <= 0:
        break
    input_command = input()

if full_cake > 0:
    print(f"{full_cake} pieces are left.")
else:
    print(f"No more cake left! You need {abs(full_cake)} pieces more.")