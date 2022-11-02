def way1(n):
    balanced = 0
    for i in range(n):
        string = input()
        if string == "(":
            balanced += 1
            if balanced > 1:
                print("UNBALANCED")
                exit()
        elif string == ")":
            balanced -= 1
    if balanced == 0:
        print("BALANCED")
    else:
        print("UNBALANCED")


def way2(n):
    is_balanced = True
    last_bracket = ''
    for _ in range(n):
        current = input()
        if current not in ['(', ')']:
            continue

        if last_bracket == '' and current == ')' or last_bracket == current:
            is_balanced = False
            break

        last_bracket = current

    if is_balanced:
        print('BALANCED')
    else:
        print('UNBALANCED')


def way3(n):
    is_balanced = True
    has_open_bracket = False

    for _ in range(n):
        line = input()
        if line != '(' and line != ')':
            continue

        is_open_bracket = line == '('
        if has_open_bracket == is_open_bracket:
            is_balanced = False
            break

        has_open_bracket = is_open_bracket

    if is_balanced:
        print('BALANCED')
    else:
        print('UNBALANCED')


n_lines = int(input())
way1(n_lines)
