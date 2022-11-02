from collections import deque

quantity_food_daily = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

for _ in range(len(orders)):
    current_order = orders[0]
    if quantity_food_daily >= current_order:
        orders.popleft()
        quantity_food_daily -= current_order
    else:
        break

if len(orders) > 0:
    print(f"Orders left:", *orders, sep= " ")
else:
    print('Orders complete')