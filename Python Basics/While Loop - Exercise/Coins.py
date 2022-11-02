change = float(input())
change_coins = round(change * 100)
coins_returned = 0

while change_coins > 0:
    if change_coins >= 200:
        change_coins -= 200
        coins_returned += 1
    elif change_coins >= 100:
        change_coins -= 100
        coins_returned += 1
    elif change_coins >= 50:
        change_coins -= 50
        coins_returned += 1
    elif change_coins >= 20:
        change_coins -= 20
        coins_returned += 1
    elif change_coins >= 10:
        change_coins -= 10
        coins_returned += 1
    elif change_coins >= 5:
        change_coins -= 5
        coins_returned += 1
    elif change_coins >= 2:
        change_coins -= 2
        coins_returned += 1
    elif change_coins >= 1:
        change_coins -= 1
        coins_returned += 1

print(coins_returned)