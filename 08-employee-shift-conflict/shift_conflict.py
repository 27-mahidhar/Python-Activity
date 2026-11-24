# Case Study 48: Tuple-Based Employee Shift Conflict Detection
# Syllabus: Tuples, Tuple Operations, Unpacking, Nested Loops, Conditionals

shifts = [
    ("E101", "Ravi", "Mon", 9, 13),
    ("E101", "Ravi", "Mon", 12, 16),
    ("E102", "Priya", "Mon", 9, 13),
    ("E102", "Priya", "Mon", 13, 17),
    ("E103", "Kiran", "Tue", 10, 15),
    ("E103", "Kiran", "Tue", 14, 18),
    ("E101", "Ravi", "Wed", 9, 17)
]

conflicts = []
conflicted_ids = []

for i in range(len(shifts)):
    id1, name1, day1, s1, e1 = shifts[i]
    for j in range(i + 1, len(shifts)):
        id2, name2, day2, s2, e2 = shifts[j]

        if id1 == id2 and day1 == day2:
            if s1 < e2 and s2 < e1:
                conflicts.append((id1, name1, day1, (s1, e1), (s2, e2)))
                if id1 not in conflicted_ids:
                    conflicted_ids.append(id1)

print("=== EMPLOYEE SHIFT CONFLICT REPORT ===")
if len(conflicts) == 0:
    print("No shift conflicts detected.")
else:
    for emp_id, name, day, slot1, slot2 in conflicts:
        print(f"CONFLICT: {emp_id} ({name}) on {day} -> {slot1[0]}:00-{slot1[1]}:00 overlaps {slot2[0]}:00-{slot2[1]}:00")

    print(f"\nTotal Conflicts Found      : {len(conflicts)}")
    print(f"Conflicted Employee IDs    : {tuple(conflicted_ids)}")
