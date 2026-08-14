age = int(input("Enter your age: "))

if age >= 0 and age <= 12:
    category = "Child"
elif age >= 13 and age <= 17:
    category = "Teen"
elif age >= 18 and age <= 64:
    category = "Adult"
else:
    category = "Senior"

print(f"You are a {category}.")
