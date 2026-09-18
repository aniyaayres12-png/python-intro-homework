with open("../data/notes.txt") as f:
    for i, line in enumerate(f, start=1):
        print(f"Line {i}: {line.strip()}")
        