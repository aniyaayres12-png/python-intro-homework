#replace this with a list from week-5/data/numbers.py
numbers = [5, 3, 8, 1, 5, 7, 9, 2]

def find_minimum(nums):
    smallest = nums[0]
    for n in nums:
        if n < smallest:
            smallest = n
        return smallest

def find_maximum(nums):
    largest = nums [0]
    for n in nums:
        if n > largest:
            largest = n
        return largest

def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

def bubble_sort(nums):
    nums = nums.copy()
    swapped = True
    while swapped:
        swapped = False 
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return nums

while True:
    print("\n=== Number Cruncher ===")
    print("1. Find the minimum")
    print("2. Find the maximum")
    print("3. Search for a number")
    print("4. Sort through the list")
    print("5. Quit")

    choice = input("Choose an option (1 through 5):")

    if choice == "1":
        print(f"Minimum: {find_minimum(numbers)}")
    elif choice == "2":
        print(f"Maximum: {find_maximum(numbers)}")
    elif choice == "3":
        target = int(input("Enter a number to search for: "))
        index = linear_search(numbers, target)
        if index != -1:
            print(f"Found {target} at {index}.")
        else:
            print(f"{target} was not found in the list.")
    elif choice == "4":
        print(f"Sorted list: {bubble_sort(numbers)}")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again and choose a number 1 through 5.")


    

        