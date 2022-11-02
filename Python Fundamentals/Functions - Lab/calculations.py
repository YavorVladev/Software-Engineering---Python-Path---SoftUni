def calculation(x,y,operator):
    if operator == "multiply":
        return x * y
    elif operator == "divide":
        return int(x/y)
    elif operator == "add":
        return x + y
    elif operator == "subtract":
        return x - y


operation = input()
first_number = int(input())
second_number = int(input())
print(calculation(first_number, second_number, operation))
