def calculation(product,quantity):
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "coke":
        price = 1.40
    elif product == "water":
        price = 1.00
    elif product == "snacks":
        price = 2.00

    final_sum = price * quantity
    return f"{final_sum:.2f}"


product = input()
quantity = int(input())
print(calculation(product, quantity))
