import sys
n_snowballs = int(input())
highest_value = -sys.maxsize
sn_weight = 0
sn_time = 0
sn_quality = 0
for i in range(1,n_snowballs + 1):
    weight = int(input())
    fly_time = int(input())
    quality = int(input())
    value = (weight // fly_time) ** quality
    if value > highest_value:
        highest_value = value
        sn_weight = weight
        sn_time = fly_time
        sn_quality = quality
print(f"{sn_weight} : {sn_time} = {highest_value} ({sn_quality})")
