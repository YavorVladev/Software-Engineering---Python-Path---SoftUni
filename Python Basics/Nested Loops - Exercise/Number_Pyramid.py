n = int(input())
current_numb = 1
is_bigger = False
for rows in range(1, n+1):
    for col in range(1, rows+1):
        if current_numb > n:
            is_bigger = True
            break
        print(str(current_numb) + " ", end="")
        current_numb +=1
    if is_bigger:
        break
    print()