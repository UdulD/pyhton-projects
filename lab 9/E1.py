import matplotlib.pyplot as plt

# ── Part 1: Read input ──────────────────────────────────────────────────────
with open("input.txt", "r") as f:
    line1 = f.readline().strip()
    line2 = f.readline().strip()

Vin, Vout_desired, tolerance = line1.split(",")
Vin = int(Vin.strip())
Vout_desired = int(Vout_desired.strip())
tolerance = float(tolerance.strip())

resistors = [int(r.strip()) for r in line2.split(",")]

# ── Part 1: Find best resistor pair ────────────────────────────────────────
best_pair = None
best_power = float("inf")

for i in range(len(resistors)):
    for j in range(len(resistors)):
        if i == j:
            continue
        R1 = resistors[i]
        R2 = resistors[j]
        Vout_calc = Vin * R2 / (R1 + R2)
        if abs(Vout_calc - Vout_desired) <= tolerance:
            P = (Vin ** 2) / (R1 + R2)
            if P < best_power:
                best_power = P
                best_pair = (R1, R2)

if best_pair is None:
    print("No valid resistor pair found within the given tolerance.")
else:
    R1, R2 = best_pair

    # ── Part 1: Write output ────────────────────────────────────────────────
    with open("output.txt", "w") as f:
        f.write(f"{R1}, {R2}")

    print(f"Best pair: R1 = {R1}, R2 = {R2}")
    print(f"Vout = {Vin * R2 / (R1 + R2):.6f} V")
    print(f"Power = {best_power:.6f} W")

    # ── Part 2: Plot Vnew vs RL ─────────────────────────────────────────────
    RL_values = range(10, 1010, 10)
    Vnew_values = []

    for RL in RL_values:
        R2_parallel_RL = (R2 * RL) / (R2 + RL)
        Vnew = Vin * R2_parallel_RL / (R1 + R2_parallel_RL)
        Vnew_values.append(Vnew)

    plt.figure(figsize=(8, 5))
    plt.plot(list(RL_values), Vnew_values)
    plt.title("Voltage vs Resistance")
    plt.xlabel("Resistance (ohms)")
    plt.ylabel("Voltage (V)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("voltage_vs_resistance.png")
    plt.show()
    print("Plot saved as voltage_vs_resistance.png")