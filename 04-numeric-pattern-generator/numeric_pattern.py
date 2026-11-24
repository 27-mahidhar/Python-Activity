# Case Study 27: Advanced Numeric Pattern Generator
# Syllabus: Conditionals, Nested Loops, Pattern Generation, Strings, Lists

test_dimensions = [1, 12, 4, 5]

print("=== HOLLOW NUMERIC DIAMOND PATTERN GENERATOR ===")

for n in test_dimensions:
    print(f"\nInput Dimension: n = {n}")
    if n < 2 or n > 9:
        print("Error: Dimension must be an integer between 2 and 9 for proper alignment.")
        continue

    for i in range(1, n + 1):
        line = ""
        for s in range(n - i):
            line += " "
        line += str(i)
        if i > 1:
            for gap in range(2 * i - 3):
                line += " "
            line += str(i)
        print(line)

    for i in range(n - 1, 0, -1):
        line = ""
        for s in range(n - i):
            line += " "
        line += str(i)
        if i > 1:
            for gap in range(2 * i - 3):
                line += " "
            line += str(i)
        print(line)
