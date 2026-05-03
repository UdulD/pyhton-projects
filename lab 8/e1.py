import math

def analyseSeriesCircuit(R, L_mH, C_uF, V, f):
    L = L_mH * 1e-3
    C = C_uF * 1e-6
    w = 2 * math.pi * f
    zl = w * L
    zc = 1.0 / (w * C)
    zt = math.sqrt(R**2 + (zl - zc)**2)
    current = V / zt
    angle = math.degrees(math.atan((zl - zc) / R))
    return zl, zc, zt, current, angle

def analyseParallelCircuit(R, L_mH, C_uF, V, f):
    L = L_mH * 1e-3
    C = C_uF * 1e-6
    w = 2 * math.pi * f
    zl = w * L
    zc = 1.0 / (w * C)
    zt = 1.0 / math.sqrt((1.0/R)**2 + (1.0/zl - 1.0/zc)**2)
    current = V / zt
    angle = math.degrees(math.atan((1.0/zl - 1.0/zc) * R))
    return zl, zc, zt, current, angle

def main():
    fname = input()
    results = []

    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) != 6:
                continue
            ctype = parts[0].lower()
            R = float(parts[1])
            L = float(parts[2])
            C = float(parts[3])
            V = float(parts[4])
            freq = float(parts[5])

            if ctype == "series":
                zl, zc, zt, current, angle = analyseSeriesCircuit(R, L, C, V, freq)
            else:
                zl, zc, zt, current, angle = analyseParallelCircuit(R, L, C, V, freq)

            results.append(f"{round(zl, 1)} {round(zc, 1)} {round(zt, 1)} {round(current, 1)} {round(angle, 1)}")

    with open("result.txt", "w") as f:
        f.write("\n".join(results) + "\n")

main()
