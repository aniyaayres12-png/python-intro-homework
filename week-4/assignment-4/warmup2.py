student = {
    "name": "Aniya",
    "grade": 12,
    "subjects": ["Comp Sci", "Science", "Math"],
}

for key, value in student.items():
    print(f"{key}: {value}")

student["graduated"] = False
print(student)
