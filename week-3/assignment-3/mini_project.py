day = input("What day is it? ").strip().lower()
time = input("What time is it? ").strip().lower()

suggestion = {
    ("monday", "morning"): "Morning Python class - great time to focus!",
    ("monday", "afternoon"): "Review notes from previous class.",
    ("monday", "evening"): "Relax and prep for the upcoming week.",
    ("tuesday", "morning"): "Complete the hardest task first!",
    ("tuesday", "afternoon"): "Work on your project or assignments.",
    ("tuesday", "evening"): "Take a break and recharge.",
    ("saturaday", "morning"): "Week check-in: review your progress.",
    ("saturday", "afternoon"): "Catch up on personal errands",
    ("saturday", "evening"): "Enjoy and have a perfect night",
}

valid_days = "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday"

if (day, time) in suggestion:
    print(f"Suggestion for: {suggestion[(day, time)]}")
elif day not in ["morning", "afternoon", "evening"]:
    print(f"Sorry, I don't recognize that day. Please enter a valid day. Try: {valid_days}..")
elif time not in ["morning", "afternoon", "evening"]:
    print(f"Sorry, I don't recognize that time. Please enter a valid time (morning, afternoon, evening).")
else: 
    print("Suggestion: Take a break and enjoy your day!")