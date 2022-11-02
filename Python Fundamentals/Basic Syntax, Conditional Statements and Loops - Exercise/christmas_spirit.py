quantity = int(input())
days = int(input())
budget = 0
total_spirit = 0
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
for curr_day in range(1, days + 1):
    if curr_day % 11 == 0:
        quantity += 2
    if curr_day % 2 == 0:
        budget += ornament_set * quantity
        total_spirit += 5
    if curr_day % 3 == 0:
        budget += (tree_skirt + tree_garland) * quantity
        total_spirit += 13
    if curr_day % 5 == 0:
        budget += tree_lights * quantity
        total_spirit += 17
        if curr_day % 3 == 0:
            total_spirit += 30
    if curr_day % 10 == 0:
        total_spirit -= 20
        budget += tree_skirt + tree_garland + tree_lights
if days % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")
