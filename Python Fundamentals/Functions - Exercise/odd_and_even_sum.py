def summed(number):
    even_digits = 0
    odd_digits = 0
    string_to_int = []
    for string in number:
        string_to_int.append(int(string))
    for num in string_to_int:
        if num % 2 == 0:
            even_digits += num
        elif num % 2 != 0:
            odd_digits += num
    return f"Odd sum = {odd_digits}, Even sum = {even_digits}"


number = input()
print(summed(number))
