def game(text):
    total = 0
    for word in text:
        num = int(word[1:-1])
        result = 0
        first_sym_num = ord(word[0].lower()) - 96
        last_sym_num = ord(word[-1].lower()) - 96
        if word[0].isupper():
            result = num / first_sym_num
        elif word[0].islower():
            result = num * first_sym_num
        if word[-1].isupper():
            result -= last_sym_num
        elif word[-1].islower():
            result += last_sym_num
        total += result

    return f'{total:.2f}'


text = input().split()
print(game(text))
