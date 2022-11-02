n = float(input())

if n == 0:
    print(f"zero")
elif n > 0:
    if n < 1:
        print(f"small positive")
    elif n > 1000000:
        print(f"large positive")
    else:
        print(f"positive")
else:
    if abs(n) < 1:
        print(f"small negative")
    elif abs(n) > 1000000:
        print(f'large negative')
    else:
        print(f"negative")
