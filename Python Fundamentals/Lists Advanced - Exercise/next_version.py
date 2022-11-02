current_version = [int(s) for s in input().split(".")]
current_version[-1] += 1
print(len(current_version))
for index in range(len(current_version) - 1, -1, -1):
    if current_version[index] > 9:
        current_version[index] = 0
        if index - 1 >= 0:
            current_version[index-1] += 1
print(".".join(str(s) for s in current_version))
