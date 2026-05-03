import math


def analyseSeriesCircuit(R, L_mH, C_uF, V, f):
    """
    Analyse a Series R-L-C circuit.

    Arguments:
        R     -- Resistance in Ohms
        L_mH  -- Inductance in millihenries
        C_uF  -- Capacitance in microfarads
        V     -- Voltage amplitude in Volts
        f     -- Frequency in Hertz

    Returns:
        (Z_L, Z_C, Z_total, I, phi_deg)
        Z_L     -- Inductor impedance in Ohms
        Z_C     -- Capacitor impedance in Ohms
        Z_total -- Total impedance in Ohms
        I       -- Current in Amperes
        phi_deg -- Phase angle in degrees
    """
    L = L_mH * 1e-3          # millihenries -> henries
    C = C_uF * 1e-6          # microfarads  -> farads

    omega   = 2 * math.pi * f
    Z_L     = omega * L
    Z_C     = 1.0 / (omega * C)
    Z_total = math.sqrt(R**2 + (Z_L - Z_C)**2)
    I       = V / Z_total
    phi_deg = math.degrees(math.atan((Z_L - Z_C) / R))

    return Z_L, Z_C, Z_total, I, phi_deg


def analyseParallelCircuit(R, L_mH, C_uF, V, f):
    """
    Analyse a Parallel R-L-C circuit.

    Arguments:
        R     -- Resistance in Ohms
        L_mH  -- Inductance in millihenries
        C_uF  -- Capacitance in microfarads
        V     -- Voltage amplitude in Volts
        f     -- Frequency in Hertz

    Returns:
        (Z_L, Z_C, Z_total, I, phi_deg)
        Z_L     -- Inductor impedance in Ohms
        Z_C     -- Capacitor impedance in Ohms
        Z_total -- Total impedance in Ohms
        I       -- Current in Amperes
        phi_deg -- Phase angle in degrees
    """
    L = L_mH * 1e-3          # millihenries -> henries
    C = C_uF * 1e-6          # microfarads  -> farads

    omega   = 2 * math.pi * f
    Z_L     = omega * L
    Z_C     = 1.0 / (omega * C)
    Z_total = 1.0 / math.sqrt((1.0 / R)**2 + (1.0 / Z_L - 1.0 / Z_C)**2)
    I       = V / Z_total
    phi_deg = math.degrees(math.atan((1.0 / Z_L - 1.0 / Z_C) * R))

    return Z_L, Z_C, Z_total, I, phi_deg


def main():
    # ------------------------------------------------------------------ #
    # Input and output filenames are fixed                                #
    # ------------------------------------------------------------------ #
    input_filename  = "input.txt"
    output_filename = "result.txt"

    # ------------------------------------------------------------------ #
    # Read each line and call the appropriate function                    #
    # ------------------------------------------------------------------ #
    output_lines = []

    with open(input_filename, "r") as input_file:
        for line in input_file:
            line = line.strip()
            if not line:                    # skip blank lines
                continue

            parts        = line.split()
            circuit_type = parts[0].lower()
            R            = float(parts[1])
            L_mH         = float(parts[2])
            C_uF         = float(parts[3])
            V            = float(parts[4])
            f            = float(parts[5])

            if circuit_type == "series":
                Z_L, Z_C, Z_total, I, phi_deg = analyseSeriesCircuit(R, L_mH, C_uF, V, f)
            else:                           # parallel
                Z_L, Z_C, Z_total, I, phi_deg = analyseParallelCircuit(R, L_mH, C_uF, V, f)

            result_line = (f"{round(Z_L, 1)} {round(Z_C, 1)} "
                           f"{round(Z_total, 1)} {round(I, 1)} {round(phi_deg, 1)}")
            output_lines.append(result_line)

    # ------------------------------------------------------------------ #
    # Write results to result.txt                                         #
    # ------------------------------------------------------------------ #
    with open(output_filename, "w") as output_file:
        output_file.write("\n".join(output_lines) + "\n")

    print(f"Results written to {output_filename}")


main()