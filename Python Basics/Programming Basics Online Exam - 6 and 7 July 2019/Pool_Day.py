import math

amount_people = int(input())
enter_tax = float(input())
one_bench_price = float(input())
one_umbr_price = float(input())

tax_sum = amount_people * enter_tax
all_benches = math.ceil(amount_people * 0.75)
price_all_benches = all_benches * one_bench_price
all_umbr = math.ceil(amount_people / 2)
all_umbr_price = all_umbr * one_umbr_price

result = tax_sum + price_all_benches + all_umbr_price
print(f"{result:.2f} lv.")