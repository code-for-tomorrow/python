# Warning: can be challenging
#
# A teacher is given a list of students.The number of occurences of a student's
# name in the list is the number of times the student participated this week.
# If a student has 8 or more participations, they get an A. If a student has
# between 4 and 7 participations, they get a B. If a student has more than
# 0 but less than 4, the student gets a C.
#
# Make a dictionary with the keys as the students' name and the values as the
# corresponding student's letter grade. Print the dictionary
#
# Write your code below


participation_occurences = [
    "Sam",
    "Dan",
    "Bob",
    "Dan",
    "Sam",
    "Sam",
    "Bob",
    "Dan",
    "Dan",
    "Ivan",
    "Ivan",
    "Ray",
    "Sam",
    "Sam",
    "Dan",
    "Ivan",
    "Ivan",
    "Ray",
    "Dan",
    "Ivan",
    "Ivan",
    "Sam",
    "Dan",
    "Ray",
    "Sam",
    "Dan",
    "Bob",
    "Dan",
    "Sam",
    "Sam",
    "Dan",
    "Bob",
    "Dan",
    "Sam",
    "Sam",
]

grade_dict = {}
for student in participation_occurences:
    if student not in grade_dict:
        grade_dict[student] = 1
    else:
        grade_dict[student] += 1

for student in grade_dict.keys():
    if grade_dict[student] > 7:
        grade_dict[student] = "A"
    elif grade_dict[student] > 3:
        grade_dict[student] = "B"
    else:
        grade_dict[student] = "C"

print(grade_dict)
