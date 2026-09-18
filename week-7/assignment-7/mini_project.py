import csv
import os
from datetime import datetime

def generate_report(rows, category, filename):
    """Filter the rows by category, total the amount, and then write an report file."""
    filtered = [row for row in rows if row.get("category") == category]
    total = sum(row["amount"] for row in filtered)
    today_str = datetime.now().strftime("%B %d, %Y")

    with open(filename, "w") as f:
        f.write(f"Report for {category} - {today_str}\n\n")
        for row in filtered:
            f.write(f"{row['date']}: ${row['amount']:.2f}\n")
        f.write(f"\nTotal: ${total:.2f}\n")

def main():
    path = os.path.join("..", "data", "expenses.csv")

    if not os.path.exists(path): 
        print("Error: expenses.csv is not found.")
        return
    with open(path) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # this is the amount that comes back as a string from DictReader, which will then convert before any math
    for row in rows:
        row["amount"] = float(row["amount"])

    generate_report(rows, "Food", "food_report.txt")
    print("Report generated: food_report.txt")

    # same function
    generate_report(rows, "Transport", "transport_report.txt")
    print("Report generated: transport_report.txt")

main()


