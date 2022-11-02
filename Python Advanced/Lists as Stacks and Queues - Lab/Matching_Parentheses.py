exp = input()
res = []

for idx in range(len(exp)):
    ch = exp[idx]
    if ch == "(":
        res.append(idx)
    elif ch == ")":
        opening_bracket_idx = res.pop()
        final_expression = exp[opening_bracket_idx:idx+1]
        print(final_expression)