import math
import matplotlib.pyplot as plt
import csv


def radians(deg):
    """Input angle in degrees and returns radians"""
    return deg * math.pi / 180


def degrees(radian):
    """Input angle in radians and returns degrees"""
    return radian * 180 / math.pi


# Take index number as input
index = input("Enter Index Number: ")
filename = input("Enter CSV filename: ")

# Check if the index number is in correct format
if (len(index) != 6 and len(index) != 7) or not index[:6].isnumeric():
    print("Invalid Index Number")
    exit()

# Assign Lengths according to the index number
try:
    AB = 10
    BC = 40 + int(index[3])
    CD = 30 + int(index[4])
    AD = 30 + int(index[5])
    THETA = radians(int(index[4:6]))
    OMEGA = 0.1 + int(index[5]) * 0.1

    print("AB = ", AB)
    print("BC = ", BC)
    print("CD = ", CD)
    print("AD = ", AD)
    print("Angle = ", round(degrees(THETA)))
    print("Angular Velocity = ", OMEGA)

except ValueError:
    exit()


def get_velocity(Theta, initial=False):
    # Solving the diagram to find the unknown angles using sin and cosine rules

    BD = (AB ** 2 + AD ** 2 - 2 * AB * AD * math.cos(Theta)) ** 0.5

    BDA = math.asin(10 * math.sin(Theta) / BD)
    BDC = math.acos((BD ** 2 + CD ** 2 - BC ** 2) / (2 * BD * CD))
    BCD = math.acos((BC ** 2 + CD ** 2 - BD ** 2) / (2 * BC * CD))
    CBX = math.pi - BDA - BDC - BCD

    # Finding the initial velocity at B
    Vb = OMEGA * AB

    # Solving the relative velocity diagram using the sin and cosine rules
    bac = (math.pi * 0.5) - Theta
    cax = BDA + BDC - (math.pi * 0.5)
    acb = (math.pi * 0.5) + CBX + cax

    bc = Vb * math.sin(bac - cax) / math.sin(acb)
    ec = bc / 2
    ac = 4 * math.sin((math.pi * 0.5) - CBX - bac) / math.sin(acb)
    ae = (ac ** 2 + ec ** 2 - 2 * ac * ec * math.cos(acb)) ** 0.5

    # Check whether the initial condition is given
    if initial:
        return ae
    else:
        return abs(ac)


print("Velocity at mid-point of BC", round(get_velocity(THETA, initial=True), 2))

angles = list(range(361))
velocities = []

# Open csv to write
file = open(filename, "w")
writer = csv.writer(file)
writer.writerow(["Theta", "Vc (cm/s)"])

# Iterate through each angle and get the Vc value to plot graph
for angle in range(361):
    rad = radians(angle)
    Vc = get_velocity(rad)
    velocities.append(Vc)

# Iterate by 18 degrees and get the Vc value and write to CSV
for angle in range(0, 361, 18):
    rad = radians(angle)
    Vc = get_velocity(rad)
    row = [str(angle), str(round(Vc, 2))]
    writer.writerow(row)

file.close()

plt.title("Angle(\u03B8) vs Velocity of Point C")
plt.xlabel("Theta(\u03B8)")
plt.ylabel("Velocity of point C (w.r.t point A)")
plt.plot(angles, velocities)
labels=list(range(0, 361, 45))
plt.xticks(labels)
plt.grid(True)
plt.show()
