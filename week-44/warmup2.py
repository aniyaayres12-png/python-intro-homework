student = {
    "name": "Niya",
    "grade": 11, 
    "subjects": ["Python", "Science", "Math"]
}

for key, value in student.items():
    print(f"{key}: {value}")

student["graduated"] = False

print(student)
