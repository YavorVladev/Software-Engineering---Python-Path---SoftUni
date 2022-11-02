year = int(input())
next_happy_year = 0
end_loop = False
while not end_loop:
    year += 1
    find_happy_year = list(str(year))
    list_num = []
    for num in find_happy_year:
        if num not in list_num:
            list_num.append(num)
    if len(list_num) == len(find_happy_year):
        print("".join(find_happy_year))
        end_loop = True