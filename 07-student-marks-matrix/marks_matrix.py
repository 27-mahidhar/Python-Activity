# Case Study 42: Student Marks Matrix Analysis
# Syllabus: Nested Lists, Loops, Conditionals, Operators

students = ["Ananya", "Vikram", "Divya", "Karthik", "Sneha"]
subjects = ["Math", "Python", "Physics", "English"]

marks_matrix = [
    [88, 92, 68, 85],
    [72, 65, 48, 70],
    [95, 96, 62, 90],
    [60, 58, 45, 66],
    [81, 84, 55, 78]
]

top_student = ""
top_total = -1

print("=== STUDENT-WISE PERFORMANCE ===")
print(f"{'Student':<12}{'Total':>8}{'Average':>10}{'Grade':>8}")
print("-" * 38)

for i in range(len(marks_matrix)):
    row = marks_matrix[i]
    row_total = 0
    for score in row:
        row_total += score
    row_avg = row_total / len(row)

    if row_avg >= 85:
        grade = "A+"
    elif row_avg >= 75:
        grade = "A"
    elif row_avg >= 60:
        grade = "B"
    else:
        grade = "C"

    if row_total > top_total:
        top_total = row_total
        top_student = students[i]

    print(f"{students[i]:<12}{row_total:>8}{row_avg:>10.2f}{grade:>8}")

print(f"\nTop Performer: {top_student} ({top_total}/400)")

print("\n=== SUBJECT-WISE ANALYSIS ===")
weak_subjects = []
num_students = len(marks_matrix)

for col in range(len(subjects)):
    col_total = 0
    for row_idx in range(num_students):
        col_total += marks_matrix[row_idx][col]
    col_avg = col_total / num_students
    status = "LOW AVG (<60)" if col_avg < 60.0 else "Satisfactory"
    if col_avg < 60.0:
        weak_subjects.append(subjects[col])
    print(f"  {subjects[col]:<10}: Avg = {col_avg:.2f}% [{status}]")

if len(weak_subjects) > 0:
    print(f"\nSubjects needing attention: {', '.join(weak_subjects)}")
