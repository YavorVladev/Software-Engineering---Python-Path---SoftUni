def sum_numbers(n1, n2):
    return n1 + n2


def subtract_num(summed, third):
    return summed - third


def add_and_subtract(n1, n2, n3):
    sum_first_and_second = sum_numbers(n1, n2)
    result = subtract_num(sum_first_and_second, n3)
    return result


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(add_and_subtract(num1, num2, num3))
