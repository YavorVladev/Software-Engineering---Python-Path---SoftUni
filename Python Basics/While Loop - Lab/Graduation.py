name = input()
current_class = 1
bad_tries = 0
is_out = False
main_grade = 0

while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        bad_tries += 1
        if bad_tries > 1:
            is_out = True
            break
        continue
    current_class += 1
    main_grade += current_grade
if is_out:
    print(f"{name} has been excluded at {current_class} grade")
else:
    average_grade = main_grade / 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")