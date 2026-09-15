students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

top_name = ""
top_score = 0

for student in students:
    if student["score"] > top_score:
        top_score = student["score"]
        top_name = student["name"]

total = 0
for student in students:
    total += student["score"]
average_score = total / len(students)

subject =set()
for student in students:
    subject.add(student["subject"])

high_scorers = []   
for students in students:
    if students["score"] > 79:
        high_scorers.append(students["name"])

print(f"Top scorer: {top_name} has a score of {top_score}")
print(f"Class average score: {average_score}")
print(f"Subjects offered: {subject}")
print(f"High Scorers: {high_scorers}")
