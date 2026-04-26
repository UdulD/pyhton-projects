"""
Beam Analysis Program
=====================
Reads beam data from beam_data.txt and calculates:
  1. Maximum deflection at the center of the beam  : Dmax = P*L^3 / (48*E*I)
  2. Maximum bending stress at the center of the beam: Smax = P*L  / (4*I)

Input file format (beam_data.txt):
    Length(m)  YoungsModulus(GPa)  MomentOfInertia(m^4)  Load(kN)
"""


def read_beam_data(filename):
    """Read beam data from file and return a list of (L, E, I, P) tuples."""
    beams = []
    try:
        with open(filename, 'r') as f:
            for line_num, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue  # Skip empty lines
                parts = line.split()
                if len(parts) != 4:
                    print(f"[Warning] Line {line_num} skipped "
                          f"(expected 4 values, got {len(parts)}): '{line}'")
                    continue
                try:
                    L, E_GPa, I, P_kN = map(float, parts)
                    beams.append((L, E_GPa, I, P_kN))
                except ValueError:
                    print(f"[Warning] Line {line_num} skipped (non-numeric data): '{line}'")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        print("Please make sure 'beam_data.txt' is in the same directory as this script.")
    return beams


def calculate_beam_properties(L, E_GPa, I, P_kN):
    """
    Calculate maximum deflection and maximum bending stress.

    Parameters:
        L     : Length of beam (m)
        E_GPa : Young's modulus (GPa)
        I     : Moment of inertia (m^4)
        P_kN  : Central point load (kN)

    Returns:
        Dmax  : Maximum deflection (m)      = P*L^3 / (48*E*I)
        Smax  : Maximum bending stress (Pa) = P*L   / (4*I)
    """
    E = E_GPa * 1e9   # GPa → Pa
    P = P_kN  * 1e3   # kN  → N

    Dmax = (P * L**3) / (48 * E * I)   # metres
    Smax = (P * L)    / (4  * I)       # Pa

    return Dmax, Smax


def main():
    filename = "beam_data.txt"
    beams = read_beam_data(filename)

    if not beams:
        print("No valid beam data found. Exiting.")
        return

    for i, (L, E_GPa, I, P_kN) in enumerate(beams, start=1):
        Dmax, Smax = calculate_beam_properties(L, E_GPa, I, P_kN)
        print(f"Beam {i}: Length: {L} m, Max Deflection: {Dmax:.6f} m, "
              f"Max Bending Stress: {Smax:.2f} Pa")


if __name__ == "__main__":
    main()