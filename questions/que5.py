# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s)
# having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
n = int(input('enter the number of students '))
students = []
for i in range(n):
    name = input('enter yuor name')
    grade = float(input('enter your grade'))
    students.append([name, grade])

grades = sorted(set([student[1] for student in students]))
second_lowest = grades[1]

result = [student[0] for student in students if student[1] == second_lowest]
for name in sorted(result):
    print(name)
