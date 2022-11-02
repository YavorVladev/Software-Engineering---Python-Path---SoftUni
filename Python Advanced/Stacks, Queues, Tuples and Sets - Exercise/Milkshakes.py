from collections import deque

milkshakes = 0
chocolates = deque(map(int, input().split(", ")))
cup_milk = deque(map(int, input().split(", ")))

while chocolates and cup_milk and milkshakes < 5:
    last_chocolate = chocolates.pop()
    first_cup_milk = cup_milk.popleft()

    if last_chocolate <= 0 and first_cup_milk <= 0:
        continue

    if last_chocolate <= 0:
        cup_milk.appendleft(first_cup_milk)
        continue

    if first_cup_milk <= 0:
        chocolates.append(last_chocolate)
        continue

    if last_chocolate == first_cup_milk:
        milkshakes += 1
    else:
        chocolates.append(last_chocolate - 5)
        cup_milk.append(first_cup_milk)


if milkshakes >= 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
if chocolates:
    str_chocos = [str(x) for x in chocolates]
    print(f"Chocolate: {', '.join(str_chocos)}")
else:
    print("Chocolate: empty")
if cup_milk:
    str_milk = [str(x) for x in cup_milk]
    print(f"Milk: {', '.join(str_milk)}")
else:
    print("Milk: empty")

