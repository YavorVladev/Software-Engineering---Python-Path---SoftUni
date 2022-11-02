count_tabs = int(input())
salary = int(input())
copy_salary = salary
for i in range(1, count_tabs + 1):
    name_web = input()
    if name_web == "Facebook":
        copy_salary = copy_salary - 150
    elif name_web == "Instagram":
        copy_salary = copy_salary - 100
    elif name_web == "Reddit":
        copy_salary = copy_salary - 50
    if copy_salary <= 0:
        break
if copy_salary > 0:
    print(copy_salary)
else:
    print("You have lost your salary.")