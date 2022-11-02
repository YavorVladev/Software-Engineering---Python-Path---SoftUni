budget = int(input())
input_command = input()
while input_command != "End":
    price = int(input_command)
    budget -= price
    if budget < 0:
        print(f"You went in overdraft!")
        break
    input_command = input()
else:
    print(f"You bought everything needed.")
