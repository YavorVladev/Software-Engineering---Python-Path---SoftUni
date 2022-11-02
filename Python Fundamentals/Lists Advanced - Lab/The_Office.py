happiness = list(map(int, input().split()))
factor = int(input())
multi = [x * factor for x in happiness]
filtered = list(filter(lambda x: x >= sum(multi) / len(multi), multi))
if len(filtered) >= len(multi) / 2:
    print(f"Score: {len(filtered)}/{len(multi)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(multi)}. Employees are not happy!")





