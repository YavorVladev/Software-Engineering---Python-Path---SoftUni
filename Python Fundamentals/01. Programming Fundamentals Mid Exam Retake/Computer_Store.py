part_price = input()
total_price_before_tax = 0
taxes = 0
price_after_tax = 0
while part_price != "special" and part_price != "regular":
    part_price = float(part_price)
    if part_price < 0:
        print("Invalid price!")
        part_price = float(part_price)
    if part_price > 0:
        total_price_before_tax += part_price
        taxes += part_price * 0.20
    part_price = input()

if part_price == "special":
    if total_price_before_tax + taxes <= 0:
        print(f"Invalid order!")
        quit()
    price_after_tax = total_price_before_tax + taxes
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_before_tax:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {price_after_tax * 0.90:.2f}$")
elif part_price == "regular":
    if total_price_before_tax + taxes <= 0:
        print(f"Invalid order!")
        quit()
    price_after_tax = total_price_before_tax + taxes
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_before_tax:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {price_after_tax:.2f}$")