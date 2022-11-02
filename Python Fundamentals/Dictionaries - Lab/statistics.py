products_inventory = {}

while True:
    command = input()
    if command == "statistics":
        break

    command = command.split(": ")
    item = command[0]
    quantity = int(command[1])

    if item not in products_inventory:
        products_inventory[item] = quantity
    else:
        products_inventory[item] += quantity
print("Products in stock:")
for (item, quantity) in products_inventory.items():
    print(f"- {item}: {quantity}")
print(f"Total Products: {len(products_inventory.keys())}")
print(f"Total Quantity: {sum(products_inventory.values())}")
