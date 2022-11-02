wanted_winnings = float(input())
total_price = 0
money = 0


input_command = input()
while input_command != "Party!":
    drink = input_command
    amount_of_drinks = int(input())
    price = len(drink)
    total_price = price * amount_of_drinks
    if total_price % 2 != 0:
        total_price *= 0.75

    money += total_price
    if money >= wanted_winnings:
        print(f"Target acquired.")
        break
    input_command = input()

if input_command == "Party!":
    diff = wanted_winnings - money
    print(f"We need {diff:.2f} leva more.")
print(f"Club income - {money:.2f} leva.")