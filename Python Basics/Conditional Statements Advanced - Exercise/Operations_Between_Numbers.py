nmb_1 = int(input())
nmb_2 = int(input())
operator = input()
final_nmb = 0
even_odd = ""
error = ""

if operator == "+":
    final_nmb = nmb_1 + nmb_2
    if final_nmb % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{nmb_1} {operator} {nmb_2} = {final_nmb} - {even_odd}")
elif operator == "-":
    final_nmb = nmb_1 - nmb_2
    if final_nmb % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{nmb_1} {operator} {nmb_2} = {final_nmb} - {even_odd}")
elif operator == "*":
    final_nmb = nmb_1 * nmb_2
    if final_nmb % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{nmb_1} {operator} {nmb_2} = {final_nmb} - {even_odd}")

if operator == "/":
    if nmb_1 == 0 or nmb_2 == 0:
        print(f"Cannot divide {nmb_1} by zero")
    elif operator == "/":
        final_nmb = nmb_1 / nmb_2
        print(f"{nmb_1} {operator} {nmb_2} = {final_nmb:.2f}")

if operator == "%":
    if nmb_1 == 0 or nmb_2 == 0:
        print(f"Cannot divide {nmb_1} by zero")
    elif operator == "%":
        final_nmb = nmb_1 % nmb_2
        print(f"{nmb_1} {operator} {nmb_2} = {final_nmb}")