days = int(input()) - 1
room = input()
review = input()
price = 0

if room == "room for one person":
   price = 18

elif room == "apartment":
   price = 25
   if days > 15:
      price *= 0.50
   elif 10 <= days <= 15:
      price *= 0.65
   else:
      price *= 0.70

elif room == "president apartment":
   price = 35
   if days > 15:
      price *= 0.80
   elif 10 <= days <= 15:
      price *= 0.85
   else:
      price *= 0.90

if review == "positive":
   price *= 1.25
elif review == "negative":
   price *= 0.90

total = days * price
print(f"{total:.2f}")