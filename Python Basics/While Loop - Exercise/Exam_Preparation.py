fail_threshold = int(input())

sum_grades = 0
count_grades = 0
last_problem = ""
poor_grades = 0
take_break = False
input_line = input()
while input_line != "Enough":
    grade = int(input())
    if grade <= 4:
        poor_grades += 1
        if poor_grades >= fail_threshold:
            take_break = True
            break
    last_problem = input_line

    count_grades += 1
    sum_grades += grade

    input_line = input()

if take_break:
    print(f"You need a break, {poor_grades} poor grades.")
else:
 avg_grades = sum_grades / count_grades
 print(f"Average score: {avg_grades:.2f}")
 print(f"Number of problems: {count_grades}")
 print(f"Last problem: {last_problem}")