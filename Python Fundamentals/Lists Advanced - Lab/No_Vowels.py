text = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
final = [x for x in text if x not in vowels]
print(''.join(final))