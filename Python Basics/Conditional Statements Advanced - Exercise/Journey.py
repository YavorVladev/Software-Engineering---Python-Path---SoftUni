budget = float(input())
season = input()
total = 0
destination = ""
place = ""

if budget <= 100:
    if season == "summer":
        total = budget - (budget * 0.30)
        place = "Camp"
    elif season == "winter":
        total = budget - (budget * 0.70)
        place = "Hotel"
elif budget <= 1000:
    if season == "summer":
        total = budget - (budget * 0.40)
        place = "Camp"
    elif season == "winter":
        total = budget - (budget * 0.80)
        place = "Hotel"
elif budget > 1000:
    total = budget - (budget * 0.90)
    place = "Hotel"

if budget <= 100:
    destination = "Bulgaria"
elif budget <= 1000:
    destination = "Balkans"
elif budget > 1000:
    destination = "Europe"

print(f"Somewhere in {destination}")
print(f"{place} - {budget - total:.2f}")