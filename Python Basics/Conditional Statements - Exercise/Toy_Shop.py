ekskurziq = float(input())
puzeli = int(input())
kukli = int(input())
mecheta = int(input())
minion = int(input())
kamion = int(input())

pechalba = puzeli * 2.60 + kukli * 3 + mecheta * 4.10 + minion * 8.20 + kamion * 2
broi_igrachki = puzeli + kukli + mecheta + minion + kamion
if broi_igrachki >= 50:
    realna_suma = pechalba - pechalba * 0.25
else:
    realna_suma = pechalba

rent = 0.10 * realna_suma
ultimate_sum = realna_suma - rent

if ultimate_sum >= ekskurziq:
    print(f"Yes! {ultimate_sum - ekskurziq:.2f} lv left.")
else:
    print(f"Not enough money! {ekskurziq - ultimate_sum:.2f} lv needed.")