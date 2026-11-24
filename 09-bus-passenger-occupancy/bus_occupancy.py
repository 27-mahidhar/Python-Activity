# Case Study 51: Bus Passenger Occupancy Simulation
# Syllabus: Lists, Tuples, Unpacking, Loops, Conditionals

max_capacity = 45
current_passengers = 0
peak_occupancy = 0
peak_stop = ""
overloaded_stops = []

route_stops = [
    ("Central Station", 0, 22),
    ("City Market", 5, 18),
    ("Tech Park", 8, 25),
    ("University Gate", 20, 12),
    ("Main Square", 15, 4),
    ("Terminal", 33, 0)
]

print("=== BUS PASSENGER OCCUPANCY SIMULATION ===")
print(f"Bus Max Capacity: {max_capacity}\n")
print(f"{'Stop Name':<18}{'Off':>5}{'On':>5}{'Occupancy':>11}  {'Status'}")
print("-" * 55)

for stop_name, alighting, boarding in route_stops:
    if alighting > current_passengers:
        print(f"  [Warning] {stop_name}: Alighting ({alighting}) > Onboard ({current_passengers}). Adjusted.")
        alighting = current_passengers

    current_passengers = current_passengers - alighting + boarding

    if current_passengers > peak_occupancy:
        peak_occupancy = current_passengers
        peak_stop = stop_name

    if current_passengers > max_capacity:
        excess = current_passengers - max_capacity
        status = f"OVERLOAD (+{excess})"
        overloaded_stops.append((stop_name, current_passengers, excess))
    else:
        status = "Normal"

    print(f"{stop_name:<18}{alighting:>5}{boarding:>5}{current_passengers:>11}  {status}")

print("-" * 55)
print(f"Peak Occupancy  : {peak_occupancy} passengers at {peak_stop}")
print(f"Final Onboard   : {current_passengers} passengers")
print(f"Overloaded Stops: {len(overloaded_stops)}")
