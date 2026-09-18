import os

print(os.getcwd())

if os.path.exists("../data/expenses.csv"):
    print("expenses.csv is found.")
else: 
    print("expenses.csv is not found.")

path = os.path.join("..", "data", "expenses.csv")
print(path)
