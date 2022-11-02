seq_strings = input().split()
result = [word * len(word) for word in seq_strings]
print(''.join(result))
