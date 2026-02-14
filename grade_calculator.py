user_score = int(input("score here (0-100): "))
if user_score < 0 or user_score > 100:
    print("Invalid Scores: Enter a value between 0 and 100.")

elif user_score <= 100 and user_score >= 99:
    grade = "A+"
    message = "Exceptional"
elif user_score <= 98 and user_score >= 96:
    grade = "A"
    message = "Outstanding"
elif user_score <= 95 and user_score >= 93:
    grade = "A-"
    message = "Excellent"
elif user_score <= 92 and user_score >= 90:
    grade = "B+"
    message = "Very Good"
elif user_score <= 89 and user_score >= 87:
    grade = "B"
    message = "Good"
elif user_score <= 86 and user_score >= 84:
    grade = "B-"
    message = "Solid"
elif user_score <= 83 and user_score >= 81:
    grade = "C+"
    message = "Solid"
elif user_score <= 80 and user_score >= 78:
    grade = "C"
    message = "Passed"
elif user_score <= 77 and user_score >= 70:
    grade = "C-"
    message = "Passed"
elif user_score <= 69:
    grade = "F"
    message = "Failed"
else:
    print()
# print("Score:",user_score, "Grade:",grade, "-",message)
print(f"Score: {user_score} Grade: {grade} - {message}")

#grade base system
#https://share.google/0fGMKYaOgIC2HAtDB
#https://web.uvic.ca/~kumara/econ329/grading_scale.pdf
#ZYLK MANDOLADO 
