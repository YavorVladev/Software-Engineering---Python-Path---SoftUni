from collections import deque

MILIGRAMS = deque([int(x) for x in input().split(', ')])  # miligrams
ENERGY_DRINKS = deque([int(x) for x in input().split(', ')])  # drinks
coffee_drank = 0

while MILIGRAMS and ENERGY_DRINKS:
    last_miligram = MILIGRAMS.pop()
    first_drink = ENERGY_DRINKS.popleft()

    total_miligrams = last_miligram * first_drink

    if total_miligrams + coffee_drank > 300:
        ENERGY_DRINKS.append(first_drink)
        if coffee_drank - 30 >= 0:
            coffee_drank -= 30
            continue
        else:
            coffee_drank = 0
            continue

    if total_miligrams <= 300:
        coffee_drank += total_miligrams

if ENERGY_DRINKS:
    print(f"Drinks left: {', '.join([str(x) for x in ENERGY_DRINKS])}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {coffee_drank} mg caffeine.")
