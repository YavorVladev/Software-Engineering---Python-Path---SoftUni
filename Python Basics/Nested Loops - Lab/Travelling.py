destination = input()
while destination != "End":
    needed_money = float(input())
    saved_money = 0
    while saved_money < needed_money:
        add_amount = float(input())
        saved_money += add_amount
    print(f"Going to {destination}!")
    destination = input()