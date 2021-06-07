'''
Given the names and grades for each student in a class of N students, store them in a nested list and
print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically
and print each name on a new line.
'''

d = {} # empty dictionary
for _ in range(int(raw_input())): # range for number of students
    name = raw_input() # accepting name of the student
    grade = float(raw_input()) # accepting the grade of the student
    d[name] = grade # assigning name as key and grade as value for the dictionary

v = d.values() # obtaining the values of dictionary (all grades of students)
second = sorted(list(set(v)))[1] # removing duplicate grades by using set data type, changing it to list, sorting in ascending order and taking the second lowest grade
second_lowest = [] # declaring an empty list for storing the name of the students who got the second lowest grade
for key, value in d.items(): # going through the name and grade of each students by using items() method of dictionary
    if value == second: # checking whether the grade is equal to the second lowest grade
        second.lowest.append(key) # if yes, append it to the second_lowest list
second_lowest.sort() # sorting the name of students in ascending order
for name in second_lowest: # going through the name of each students who got the second lowest grade
    print (name) # printing each name of students in separate line