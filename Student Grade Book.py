student = [
    ['Sean', 90, 100, 95],
    ['Zylk', 91, 80, 95],
    ['Jhaye', 95, 80, 95],
    ['Bench', 80, 100, 95]
]
print("\n****GradeBook****")
for student_list in student:
    print(student_list) 

print(f"\n2nd Student Quiz 2 Score: {student[1][2]}")

student[2][1] = 100
print("Updated", student[2][0],"Quiz 1:",student[2][1]) 

student.append(['Shish', 75, 99, 81])

print(f"\n****Updated Student GradeBook****")
for student_list in student:
    print(student_list)
