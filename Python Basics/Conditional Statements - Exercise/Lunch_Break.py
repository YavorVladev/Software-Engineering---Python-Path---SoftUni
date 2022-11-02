import math

ime_serial = input()
ep_length = int(input())
break_length = int(input())

breakfast_time = break_length * 0.125
chill_time = break_length * 0.25

free_time_left = break_length - breakfast_time - chill_time
finale = math.ceil(free_time_left - ep_length)
needed_time = math.ceil(ep_length - free_time_left)

if free_time_left >= ep_length:
    print(f"You have enough time to watch {ime_serial} and left with {finale} minutes free time.")
else:
    print(f"You don't have enough time to watch {ime_serial}, you need {needed_time} more minutes.")