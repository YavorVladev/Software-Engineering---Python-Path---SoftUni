budget = float(input())
nights_staying = int(input())
price_per_night = float(input())
percent_bonus_spend = int(input())
price = 0

if nights_staying > 7:
    price_per_night *= 0.95
    price = nights_staying * price_per_night
elif nights_staying <= 7:
    price = nights_staying * price_per_night

expenses = (budget * percent_bonus_spend / 100)
final_sum = price + expenses
money_left = budget - final_sum
if budget >= final_sum:
    print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")
else:
    print(f"{abs(money_left):.2f} leva needed.")