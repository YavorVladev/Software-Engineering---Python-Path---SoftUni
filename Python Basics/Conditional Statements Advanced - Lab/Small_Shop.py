product_name = input()
city = input()
amount = float(input())

if city == "Sofia":
    if product_name == "coffee":
        coffee_price = round(amount * 0.50, 2)
        print(coffee_price)
    elif product_name == "water":
        water_price = round(amount * 0.80, 2)
        print(water_price)
    elif product_name == "beer":
        beer_price = round(amount * 1.20, 2)
        print(beer_price)
    elif product_name == "sweets":
        sweets_price = amount * 1.45
        print(sweets_price)
    elif product_name == "peanuts":
        peanuts_price = round(amount * 1.60, 2)
        print(peanuts_price)

elif city == "Plovdiv":
    if product_name == "coffee":
        coffee_price = round(amount * 0.40, 2)
        print(coffee_price)
    elif product_name == "water":
        water_price = round(amount * 0.70, 2)
        print(water_price)
    elif product_name == "beer":
        beer_price = round(amount * 1.15, 2)
        print(beer_price)
    elif product_name == "sweets":
        sweets_price = amount * 1.30
        print(sweets_price)
    elif product_name == "peanuts":
        peanuts_price = round(amount * 1.50, 2)
        print(peanuts_price)

elif city == "Varna":
    if product_name == "coffee":
        coffee_price = round(amount * 0.45, 2)
        print(coffee_price)
    elif product_name == "water":
        water_price = round(amount * 0.70, 2)
        print(water_price)
    elif product_name == "beer":
        beer_price = round(amount * 1.10, 2)
        print(beer_price)
    elif product_name == "sweets":
        sweets_price = amount * 1.35
        print(sweets_price)
    elif product_name == "peanuts":
        peanuts_price = round(amount * 1.55, 2)
        print(peanuts_price)