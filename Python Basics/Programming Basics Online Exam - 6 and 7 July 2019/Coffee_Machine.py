type_coffee = input()
sugar_or_no = input()
amount_purchased = int(input())
total_price = 0

if type_coffee == "Espresso":
    if sugar_or_no == "Without":
        total_price += amount_purchased * 0.90
        total_price = total_price - total_price * 0.35
    elif sugar_or_no == "Normal":
        total_price += amount_purchased * 1
    elif sugar_or_no == "Extra":
        total_price += amount_purchased * 1.20
elif type_coffee == "Cappuccino":
    if sugar_or_no == "Without":
        total_price += amount_purchased * 1
        total_price = total_price - total_price * 0.35
    elif sugar_or_no == "Normal":
        total_price += amount_purchased * 1.20
    elif sugar_or_no == "Extra":
        total_price += amount_purchased * 1.60
elif type_coffee == "Tea":
    if sugar_or_no == "Without":
        total_price += amount_purchased * 0.50
        total_price = total_price - total_price * 0.35
    elif sugar_or_no == "Normal":
        total_price += amount_purchased * 0.60
    elif sugar_or_no == "Extra":
        total_price += amount_purchased * 0.70

if type_coffee == "Espresso" and amount_purchased >= 5:
    total_price -= total_price * 0.25
if total_price > 15:
    total_price -= total_price * 0.20

print(f"You bought {amount_purchased} cups of {type_coffee} for {total_price:.2f} lv.")