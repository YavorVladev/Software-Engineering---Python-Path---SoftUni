chicken_menu = int(input())
fish_menu = int(input())
veg_menu = int(input())

chicken_price = chicken_menu * 10.35
fish_price = fish_menu * 12.40
veg_price = veg_menu * 8.15
full_price = chicken_price + fish_price + veg_price
desert_price = full_price * 0.2
dostavka = 2.50
obhsta_cena = full_price + desert_price + dostavka
print(obhsta_cena)