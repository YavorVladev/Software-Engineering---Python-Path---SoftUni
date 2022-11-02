from collections import deque
string = input().split()
numbers = deque()
for el in string:
    if el not in "+-*/":
        numbers.append(int(el))
    else:
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            result = 0

            if el == "+":
                result = first_num + second_num
            elif el == "-":
                result = first_num - second_num
            elif el == "*":
                result = first_num * second_num
            elif el == "/":
                result = first_num // second_num

            numbers.appendleft(result)

print(numbers.popleft())