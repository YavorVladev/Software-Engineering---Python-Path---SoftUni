n = int(input())
total_price = 0
for i in range(n):
    p_per_cap = float(input())
    days = int(input())
    cap_per_day = int(input())
    if p_per_cap < 0.01 or p_per_cap > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif cap_per_day < 1 or cap_per_day > 2000:
        continue
    curr_price = p_per_cap * cap_per_day * days
    total_price += curr_price
    print(f"The price for the coffee is: ${curr_price:.2f}")
print(f"Total: ${total_price:.2f}")
