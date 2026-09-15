from numbers_data import numbers

def find_min(numbers):
    smallest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
    return smallest

def find_max(numbers):
    largest = numbers [0]
    for n in numbers:
        if n > largest:
            largest = n
    return largest

def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i

def bubble_sort(numbers):
    numbers = numbers.copy()
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
    return numbers

def show_menu():
    print("/n=== Number Cruncher ===")
    print("1. Find the minimum number")
    print("2. Find the maximum number")
    print("3. Search for a number ")
    print("4. Sort through the list") 
    print("5. Exit")
    return input("Choose an option (1-5): ")

def main():
    while True:
        choice = show_menu()
        if choice == "1":
            print(f"Minimum: {find_min(numbers)}")
        elif choice == "2":
            print(f"Maximum: {find_max(numbers)}")
        elif choice == "3":
            target = int(input("Enter a number to search for: "))
            index = search(numbers, target)
            print(f"Found {target} at {index}." if index != -1 else f"{target} was not found in the list.")
        elif choice == "4":
            print(f"Sorted list: {bubble_sort(numbers)}")
        elif choice == "5":
            print("Goodbye!")
            break
    else:
        print("Invalid choice. Please try again and choose a number between 1 and 5.")

