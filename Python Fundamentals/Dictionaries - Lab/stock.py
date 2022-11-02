available_products = input().split(" ")
wanted_products = input().split(" ")
my_dict = {available_products[i]: int(available_products[i + 1]) for i in range(0, len(available_products), 2)}
for product in wanted_products:
    if product not in my_dict:
        print(f"Sorry, we don't have {product}")
    else:
        print(f"We have {my_dict[product]} of {product} left")
