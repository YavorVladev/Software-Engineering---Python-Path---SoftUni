number_a = int(input())
number_b = int(input())
number_c = int(input())
counter = 0
is_found = False


if number_a < number_b:
    for x1 in range(number_a, number_b + 1):
        for x2 in range(number_a, number_b + 1):
            counter += 1

            if x1 + x2 == number_c:
                print(f"Combination N:{counter} ({x1} + {x2} = {number_c})")
                is_found = True
                break
        if is_found:
            break
    if not is_found:
        print(f"{counter} combinations - neither equals {number_c}")