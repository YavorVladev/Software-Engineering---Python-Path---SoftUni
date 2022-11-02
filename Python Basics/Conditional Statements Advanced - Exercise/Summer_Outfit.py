temp = int(input())
time_of_day = input()

if 10 <= temp <= 18 and time_of_day == "Morning":
    outfit = "Sweatshirt"
    shoes = "Sneakers"
elif 10 <= temp <= 18 and time_of_day == "Afternoon":
    outfit = "Shirt"
    shoes = "Moccasins"
elif 10 <= temp <= 18 and time_of_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"

if 18 < temp <= 24 and time_of_day == "Morning":
    outfit = "Shirt"
    shoes = "Moccasins"
elif 18 < temp <= 24 and time_of_day == "Afternoon":
    outfit = "T-Shirt"
    shoes = "Sandals"
elif 18 < temp <= 24 and time_of_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"

if temp >= 25 and time_of_day == "Morning":
    outfit = "T-Shirt"
    shoes = "Sandals"
elif temp >= 25 and time_of_day == "Afternoon":
    outfit = "Swim Suit"
    shoes = "Barefoot"
elif temp >= 25 and time_of_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"

print(f"It's {temp} degrees, get your {outfit} and {shoes}.")