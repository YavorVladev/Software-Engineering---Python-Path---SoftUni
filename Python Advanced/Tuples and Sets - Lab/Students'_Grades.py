students = int(input())

student_grade_book = {}
for student in range(students):
    name, grade = input().split()
    if name not in student_grade_book:
        student_grade_book[name] = []
    student_grade_book[name].append(float(grade))

for student, grades in student_grade_book.items():
    grade_list = " ".join(str(f"{grade:.2f}") for grade in grades)
    average = sum(grades) / len(grades)
    print(f"{student} -> {grade_list} (avg: {average:.2f})")
