# Case Study 29: Password Policy Validation Engine
# Syllabus: Strings, Loops, Conditionals, Lists

sample_passwords = [
    "Campus@2026",
    "abc12",
    "Admin@1234",
    "Strong###9",
    "NriuCse!26"
]

special_chars = "@#$%&*!"
prohibited = ["password", "admin", "1234", "qwerty"]

print("=== PASSWORD POLICY VALIDATION REPORT ===")

for pwd in sample_passwords:
    failures = []

    if len(pwd) < 8:
        failures.append("Minimum length of 8 characters not met")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    has_repeat = False

    for i in range(len(pwd)):
        ch = pwd[i]
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True

        if i >= 2 and pwd[i] == pwd[i - 1] and pwd[i] == pwd[i - 2]:
            has_repeat = True

    if not has_upper:
        failures.append("Missing uppercase letter")
    if not has_lower:
        failures.append("Missing lowercase letter")
    if not has_digit:
        failures.append("Missing numeric digit")
    if not has_special:
        failures.append("Missing special character (@#$%&*!)")
    if has_repeat:
        failures.append("Contains 3+ consecutive repeated characters")

    low_pwd = pwd.lower()
    for bad in prohibited:
        if bad in low_pwd:
            failures.append(f"Contains prohibited substring '{bad}'")

    if len(failures) == 0:
        print(f"\nPassword: {pwd} -> VALID")
    else:
        print(f"\nPassword: {pwd} -> INVALID")
        for reason in failures:
            print(f"  - {reason}")
