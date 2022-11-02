string = list(map(int, input().split(", ")))
indexs = [i for i in range(len(string)) if string[i] % 2 == 0]
print(indexs)