# Case Study 13: ATM Transaction Sequence Simulation
# Syllabus: Variables, Conditionals, Loops, Lists, Tuples, Unpacking

balance = 10000.0
min_balance = 500.0
single_limit = 5000.0
daily_limit = 8000.0
daily_withdrawn = 0.0

transactions = [
    ("D", 2500),
    ("W", 3000),
    ("W", 5500),
    ("W", 4550),
    ("W", 4500),
    ("W", 1000),
    ("D", -200),
    ("X", 500)
]

accepted_count = 0
rejected_count = 0

print("=== ATM TRANSACTION SIMULATION LOG ===")
print(f"Initial Balance: Rs. {balance:.2f}\n")

for idx in range(len(transactions)):
    t_type, amount = transactions[idx]
    step = idx + 1

    if amount <= 0:
        rejected_count += 1
        print(f"Txn {step} ({t_type}, {amount}): REJECTED - Amount must be positive.")
    elif t_type == "D":
        balance += amount
        accepted_count += 1
        print(f"Txn {step} (D, {amount}): ACCEPTED - New Balance: Rs. {balance:.2f}")
    elif t_type == "W":
        if amount % 100 != 0:
            rejected_count += 1
            print(f"Txn {step} (W, {amount}): REJECTED - Must be a multiple of Rs. 100.")
        elif amount > single_limit:
            rejected_count += 1
            print(f"Txn {step} (W, {amount}): REJECTED - Exceeds single limit (Rs. {single_limit:.0f}).")
        elif daily_withdrawn + amount > daily_limit:
            rejected_count += 1
            print(f"Txn {step} (W, {amount}): REJECTED - Exceeds daily limit (Rs. {daily_limit:.0f}).")
        elif balance - amount < min_balance:
            rejected_count += 1
            print(f"Txn {step} (W, {amount}): REJECTED - Minimum balance Rs. {min_balance:.0f} required.")
        else:
            balance -= amount
            daily_withdrawn += amount
            accepted_count += 1
            print(f"Txn {step} (W, {amount}): ACCEPTED - New Balance: Rs. {balance:.2f}")
    else:
        rejected_count += 1
        print(f"Txn {step} ({t_type}, {amount}): REJECTED - Unknown transaction type.")

print("\n=== SUMMARY ===")
print(f"Accepted Transactions: {accepted_count}")
print(f"Rejected Transactions: {rejected_count}")
print(f"Total Withdrawn Today: Rs. {daily_withdrawn:.2f}")
print(f"Closing Balance      : Rs. {balance:.2f}")
