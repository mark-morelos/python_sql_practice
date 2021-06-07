'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for
a list of students. Print the average of the marks array for the student name provided, showing
2 places after the decimal.
'''

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

for key, value in student_marks.items():
    if query_name == key:
        sum = 0
        count = 0
        for i in value:
            sum += i
            count += 1
        average = sum/count
        print("{:.2f}".format(average))

