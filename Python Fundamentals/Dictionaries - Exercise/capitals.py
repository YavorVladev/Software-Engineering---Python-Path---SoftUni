country_names = input().split(", ")
capital_names = input().split(", ")
result = {country_names[index]: capital_names[index] for index in range(len(country_names))}
for k, v in result.items():
    print(f"{k} -> {v}")
