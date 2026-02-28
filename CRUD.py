student = ['Em-jhaye', 'Sean', 'Gnani', 'Drin', 'Bench']

# two more students
student.append("Judie")
print(student)
student.insert(1, "Lance")
print(student)

student[3] = "Zylk"
print(student)

student.remove("Drin")
print(student)

student.pop(-1)
print(student)

print(f"Final List: {student}")

list_length = len(student)
print(f"List_Length: {list_length}")
