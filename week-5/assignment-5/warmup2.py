while True: 
    user_input = input("Enter a positive number: ")
    if user_input.isdigit() and int(user_input) > 0:
     break
else: 
    print("This is not a positive number. Please try again.")
    
    