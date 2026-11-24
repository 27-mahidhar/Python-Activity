# Case Study 6: Railway Fare and Reservation Calculator
# Syllabus: Variables, Conditionals, Loops, Lists, Tuples, Unpacking

passengers = [
    ("Aarav", 28, 350, "3AC", False),
    ("Meera", 64, 350, "SL", False),
    ("Rohan", 9, 250, "2AC", False),
    ("Kavya", 35, 480, "3AC", True)
]

total_collected = 0.0

print("=== RAILWAY FARE & RESERVATION SUMMARY ===")
print(f"{'Name':<10}{'Age':>4}{'Dist':>6}{'Class':>7}{'Status':>11}{'Net Fare':>11}{'Refund':>10}")
print("-" * 59)

for name, age, dist, travel_class, is_cancelled in passengers:
    if dist <= 100:
        dist_fare = dist * 1.5
    elif dist <= 300:
        dist_fare = (100 * 1.5) + (dist - 100) * 1.2
    else:
        dist_fare = (100 * 1.5) + (200 * 1.2) + (dist - 300) * 1.0

    if travel_class == "SL":
        multiplier = 1.0
        res_fee = 40.0
    elif travel_class == "3AC":
        multiplier = 2.2
        res_fee = 60.0
    else:
        multiplier = 3.0
        res_fee = 60.0

    class_fare = dist_fare * multiplier

    if age < 12:
        concession = 0.50 * class_fare
    elif age >= 60:
        concession = 0.40 * class_fare
    else:
        concession = 0.0

    net_ticket = (class_fare - concession) + res_fee

    if is_cancelled:
        penalty = 0.25 * (class_fare - concession) + res_fee
        refund = net_ticket - penalty
        retained = penalty
        status = "Cancelled"
    else:
        refund = 0.0
        retained = net_ticket
        status = "Confirmed"

    total_collected += retained
    print(f"{name:<10}{age:>4}{dist:>6}{travel_class:>7}{status:>11}{net_ticket:>11.2f}{refund:>10.2f}")

print("-" * 59)
print(f"Total Net Revenue Retained: Rs. {total_collected:.2f}")
