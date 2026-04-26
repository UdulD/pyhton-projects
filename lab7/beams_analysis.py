def read_beam_data(filename):
    beams = []
    with open(filename, 'r') as f:
        for line in f:
            L, E_GPa, I, P_kN = map(float, line.split())
            beams.append((L, E_GPa, I, P_kN))
    return beams


def calculate_beam_properties(L, E_GPa, I, P_kN):
    E = E_GPa * 1e9
    P = P_kN  * 1e3
    Dmax = (P * L**3) / (48 * E * I)
    Smax = (P * L)    / (4  * I)
    return Dmax, Smax


def main():
    beams = read_beam_data("beam_data.txt")
    for i, (L, E_GPa, I, P_kN) in enumerate(beams, start=1):
        Dmax, Smax = calculate_beam_properties(L, E_GPa, I, P_kN)
        print(f"Beam {i}: Length: {L} m, Max Deflection: {Dmax:.6f} m, "
              f"Max Bending Stress: {Smax:.2f} Pa")

main()
