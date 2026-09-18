import csv

with open("../data/students.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']} is {row['score']}")
        
    
