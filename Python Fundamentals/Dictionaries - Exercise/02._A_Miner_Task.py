reses = {}
while True:
    material = input()
    if material == "stop":
        break
    amount = int(input())
    if material not in reses:
        reses[material] = 0
    reses[material] += amount
for key, value in reses.items():
    print(f"{key} -> {value}")