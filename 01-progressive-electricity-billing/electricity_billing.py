# Case Study 2: Progressive Electricity Billing
# Syllabus: Variables, Operators, Conditionals, Loops, Lists, Tuples, Unpacking

monthly_readings = [
    ("Jan", 95),
    ("Feb", 150),
    ("Mar", 280),
    ("Apr", 420),
    ("May", 390),
    ("Jun", 180)
]

fixed_charge = 75.0
bill_records = []
unusual_months = []

print("=== PROGRESSIVE ELECTRICITY BILLING REPORT ===")
print(f"{'Month':<8}{'Units':>8}{'Energy(Rs)':>13}{'Surcharge':>12}{'Rebate':>10}{'Total(Rs)':>12}")
print("-" * 63)

for month, units in monthly_readings:
    if units <= 100:
        energy_charge = units * 3.0
    elif units <= 200:
        energy_charge = (100 * 3.0) + (units - 100) * 4.5
    elif units <= 400:
        energy_charge = (100 * 3.0) + (100 * 4.5) + (units - 200) * 6.0
    else:
        energy_charge = (100 * 3.0) + (100 * 4.5) + (200 * 6.0) + (units - 400) * 7.5

    surcharge = 0.05 * energy_charge if units > 300 else 0.0
    rebate = 50.0 if units <= 100 else 0.0
    total_bill = energy_charge + fixed_charge + surcharge - rebate

    bill_records.append((month, units, total_bill))
    print(f"{month:<8}{units:>8}{energy_charge:>13.2f}{surcharge:>12.2f}{rebate:>10.2f}{total_bill:>12.2f}")

total_amount = 0.0
for i in range(len(bill_records)):
    month, units, bill = bill_records[i]
    total_amount += bill
    if i > 0:
        prev_month, prev_units, prev_bill = bill_records[i - 1]
        pct_change = ((bill - prev_bill) / prev_bill) * 100.0
        if pct_change > 40.0:
            unusual_months.append((month, prev_month, pct_change))

avg_bill = total_amount / len(bill_records)
print("-" * 63)
print(f"Total 6-Month Bill  : Rs. {total_amount:.2f}")
print(f"Average Monthly Bill: Rs. {avg_bill:.2f}")

if len(unusual_months) > 0:
    print("\nUnusual Bill Increases (>40% vs previous month):")
    for cur_m, prev_m, pct in unusual_months:
        print(f"  - {cur_m} increased by {pct:.1f}% compared to {prev_m}")
else:
    print("\nNo unusual bill increases detected.")
