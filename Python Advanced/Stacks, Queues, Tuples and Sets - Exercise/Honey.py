from collections import deque
n_bees = deque(map(int, input().split()))
nectar_value = deque(map(int, input().split()))
symbols = deque(input().split())
honey_made = 0

while n_bees and nectar_value:
    first_bee = n_bees[0]
    current_nectar = nectar_value[-1]

    if current_nectar < first_bee:
        nectar_value.pop()
    elif current_nectar >= first_bee:
        operation = symbols.popleft()
        nectar_value.pop()
        n_bees.popleft()
        if operation == "+":
            result = first_bee + current_nectar
            honey_made += abs(result)
        elif operation == "-":
            result = first_bee - current_nectar
            honey_made += abs(result)
        elif operation == "*":
            result = first_bee * current_nectar
            honey_made += abs(result)
        elif operation == "/":
            if first_bee and current_nectar > 0:
                result = first_bee / current_nectar
                honey_made += abs(result)

print(f"Total honey made: {honey_made}")
if n_bees:
    print(f"Bees left: {', '.join(str(x) for x in n_bees)}")
elif nectar_value:
    print(f"Nectar left: {', '.join(str(x) for x in nectar_value)}")
