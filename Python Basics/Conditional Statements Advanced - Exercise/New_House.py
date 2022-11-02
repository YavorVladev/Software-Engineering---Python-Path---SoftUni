type_flower = input()
amount_flowers = int(input())
budget = float(input())
total = 0

if type_flower == "Roses":
    if amount_flowers > 80:
        total = (amount_flowers * 5) * 0.90
    else:
        total = amount_flowers * 5
if type_flower == "Dahlias":
    if amount_flowers > 90:
        total = (amount_flowers * 3.80) * 0.85
    else:
        total = amount_flowers * 3.80
if type_flower == "Tulips":
    if amount_flowers > 80:
        total = (amount_flowers * 2.80) * 0.85
    else:
        total = amount_flowers * 2.80
if type_flower == "Narcissus":
    if amount_flowers < 120:
        total = amount_flowers * 3 + (amount_flowers * 3) * 0.15
    else:
        total = amount_flowers * 3
if type_flower == "Gladiolus":
    if amount_flowers < 80:
        total = amount_flowers * 2.50 + (amount_flowers * 2.50) * 0.20
    else:
        total = amount_flowers * 2.50

if budget >= total:
    print(f"Hey, you have a great garden with {amount_flowers} {type_flower} and {(budget - total):.2f} leva left.")
elif budget < total:
    print(f"Not enough money, you need {abs(budget - total):.2f} leva more.")