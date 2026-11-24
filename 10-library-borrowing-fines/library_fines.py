# Case Study 58: Library Borrowing and Fine Reconciliation
# Syllabus: Tuples, Unpacking, Lists, Loops, Conditionals

borrowing_records = [
    ("B101", "Python Basics", 14, 12, True),
    ("B102", "Data Structures", 14, 21, True),
    ("B103", "Discrete Math", 14, 18, False),
    ("B104", "Digital Logic", 7, 7, True),
    ("B105", "C Programming", 14, 25, False)
]

total_fines = 0.0
returned_books = 0
unreturned_books = 0
overdue_count = 0

print("=== LIBRARY BORROWING & FINE RECONCILIATION ===")
print(f"{'ID':<7}{'Book Title':<18}{'Allowed':>8}{'Held':>6}{'Overdue':>9}{'Fine(Rs)':>10}  {'Status'}")
print("-" * 72)

for book_id, title, allowed_days, days_held, is_returned in borrowing_records:
    overdue_days = days_held - allowed_days if days_held > allowed_days else 0

    if overdue_days == 0:
        fine = 0.0
    elif overdue_days <= 5:
        fine = overdue_days * 5.0
    else:
        fine = (5 * 5.0) + (overdue_days - 5) * 10.0

    if overdue_days > 0:
        overdue_count += 1

    total_fines += fine

    if is_returned:
        returned_books += 1
        status = "Returned"
    else:
        unreturned_books += 1
        status = "Pending Return"

    print(f"{book_id:<7}{title:<18}{allowed_days:>8}{days_held:>6}{overdue_days:>9}{fine:>10.2f}  {status}")

print("-" * 72)
print(f"Total Books Tracked : {len(borrowing_records)}")
print(f"Available in Library: {returned_books}")
print(f"Currently Issued Out: {unreturned_books}")
print(f"Overdue Records     : {overdue_count}")
print(f"Total Fines Assessed: Rs. {total_fines:.2f}")
