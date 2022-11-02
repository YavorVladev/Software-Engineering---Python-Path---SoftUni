trip_money = float(input())
current_money = float(input())
days_spend = 0
days_passed = 0
total_money = current_money

while total_money < trip_money:
    if days_spend >= 5:
        break
    days_passed += 1
    action = input()
    amount = float(input())

    if action == "spend":
        days_spend += 1
        total_money -= amount
        if total_money < 0:
            total_money = 0
    elif action == "save":
        days_spend = 0
        total_money += amount
if days_spend >= 5:
    print("You can't save the money.")
    print(days_passed)
else:
    print(f"You saved the money for {days_passed} days.")