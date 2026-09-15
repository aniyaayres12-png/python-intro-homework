def is_valid_score(score):
    return isinstance(score, int) and 0 <= score <= 100

score = int(input("Enter a score: "))

if is_valid_score(score):
    print ("Valid score.")
else: 
    print("Invalid score. Please enter a integer that is between 0 and 100.")
    