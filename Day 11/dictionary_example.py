student_info = {
    "name" : "John",
    "age" : 18,
    "grade" : 85,
    "subjects" : ["Math", "Science", "English"]
}

# Accessing values
print("Name:", student_info["name"])
print("Age:", student_info["age"])
print("Grade:", student_info["grade"])
print("Subjects:", student_info["subjects"])
print("Subjects:", student_info["subjects"][1])

# Updating values
student_info["age"] = 21
print("age:", student_info["age"])
