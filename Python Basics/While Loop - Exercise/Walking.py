input_line = input()
overall_steps = 0
while input_line != "Going home":
    steps = int(input_line)
    overall_steps += steps

    if overall_steps >= 10000:
        break

    input_line = input()
if input_line == "Going home":
    steps_home = int(input())
    overall_steps += steps_home
diff = abs(overall_steps - 10000)
if overall_steps >= 10000:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")