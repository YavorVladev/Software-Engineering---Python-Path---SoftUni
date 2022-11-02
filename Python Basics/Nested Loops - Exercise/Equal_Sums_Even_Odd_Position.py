n1 = int(input())
n2 = int(input())

for i in range(n1, n2 + 1):
    current_digit_str = str(i)
    even_counter = 0
    odd_counter = 0

    for j in range(0, len(current_digit_str)):
        digit = int(current_digit_str[j])
        if j % 2 == 0:
            even_counter += digit
        else:
            odd_counter += digit

    if even_counter == odd_counter:
        print(current_digit_str, end=" ")