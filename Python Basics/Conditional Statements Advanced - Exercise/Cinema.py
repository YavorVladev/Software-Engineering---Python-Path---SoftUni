projection = input()
broi_redove = int(input())
broi_koloni = int(input())
income = 0

kapacitet_kino = broi_koloni * broi_redove

if projection == "Premiere":
    income = kapacitet_kino * 12.00
elif projection == "Normal":
    income = kapacitet_kino * 7.50
elif projection == "Discount":
    income = kapacitet_kino * 5.00
print(f"{income:.2f} leva")