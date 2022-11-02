budget = float(input())
price_per_kg_flour = float(input())
total_eggs = 0
total_loaves = 0
one_pack_eggs = price_per_kg_flour * 0.75
liter_milk = price_per_kg_flour * 1.25
milk = liter_milk / 4
loave_price = one_pack_eggs + price_per_kg_flour + milk
while budget >= loave_price:
    total_eggs += 3
    total_loaves += 1
    budget -= loave_price
    if total_loaves % 3 == 0:
        total_eggs -= total_loaves - 2
print(f"You made {total_loaves} loaves of Easter bread! Now you have {total_eggs} eggs and {budget:.2f}BGN left.")

