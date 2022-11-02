judges = int(input())
grade_counter = 0
all_grade_sum = 0


input_command = input()
while input_command != "Finish":
    projects = input_command
    sum = 0

    for i in range(1, judges + 1):
        grade = float(input())
        grade_counter += 1
        all_grade_sum += grade
        sum += grade

    avg_grade = sum / judges
    print(f"{projects} - {avg_grade:.2f}.")

    input_command = input()

final_grade = all_grade_sum / grade_counter
print(f"Student's final assessment is {final_grade:.2f}.")