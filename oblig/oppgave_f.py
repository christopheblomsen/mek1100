import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt

data = sio.loadmat('data.mat')
x = data.get('x')
y = data.get('y')
u = data.get('u')
v = data.get('v')
xit = data.get('xit')
yit = data.get('yit')

"""
oppgave c
"""


def rectangle(x1, x2, y1, y2):
    position1 = (x[x2, x1], y[x2, y1])
    position2 = (x[y2, y1], y[y2, y1])

    # Bottom
    plt.plot([position1[0], position2[0]], [position1[1], position1[1]], "r")

    # Righ
    plt.plot([position2[0], position2[0]], [position1[1], position2[1]], "g")

    # Top
    plt.plot([position1[0], position2[0]], [position2[1], position2[1]], "b")

    # Left
    plt.plot([position1[0], position1[0]], [position1[1], position2[1]], "k")


"""
f
"""


def draw_rectangles():
    rectangle1_values = [34, 159, 69, 169]
    rectangle(rectangle1_values[0], rectangle1_values[1],
              rectangle1_values[2], rectangle1_values[3])

    rectangle2_values = [34, 84, 69, 99]
    rectangle(rectangle2_values[0], rectangle2_values[1],
              rectangle2_values[2], rectangle2_values[3])

    rectangle3_values = [34, 49, 69, 59]
    rectangle(rectangle3_values[0], rectangle3_values[1],
              rectangle3_values[2], rectangle3_values[3])


dudy = np.gradient(u, 0.5, axis=0)
dvdx = np.gradient(v, 0.5, axis=1)

curl_v = dvdx - dudy


def line_integral(x1, y1, x2, y2):
    side1 = 0
    side2 = 0
    side3 = 0
    side4 = 0
    dx = 0.5
    dy = 0.5

    for k in u[y1, x1:x2+1]:
        side1 += k*dx

    for k in v[x2, y1:y2+1]:
        side2 += k*dy

    for k in u[y2, x1:x2+1]:
        side3 -= k*dx

    for k in v[x1, y1:y2+1]:
        side4 -= k*dy

    sumation = side1 + side2 + side3 + side4
    return sumation, side1, side2, side3, side4


def surface_integral(x1, y1, x2, y2):
    integral = 0
    dx = 0.5
    dy = 0.5
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            integral += curl_v[j, i]*dx*dy

    return integral


line_integral_1, side1_1, side2_1, side3_1, side4_1 = line_integral(34, 159, 69, 169)
line_integral_2, side1_2, side2_2, side3_2, side4_2 = line_integral(34, 84, 69, 99)
line_integral_3, side1_3, side2_3, side3_3, side4_3 = line_integral(34, 49, 69, 59)

integral_1 = surface_integral(34, 159, 69, 169)
integral_2 = surface_integral(34, 84, 69, 99)
integral_3 = surface_integral(34, 49, 69, 159)

print(f"Sirkulasjonen til rektangel 1 ble {line_integral_1}")
print(f"Sirkulasjonen til rektangel 2 ble {line_integral_2}")
print(f"Sirkulasjonen til rektangel 3 ble {line_integral_3}")

print(f"""Rektangel 1 har side verdier: Side 1={side1_1},
      Side 2={side2_1}, Side 3={side3_1}, Side 4={side4_1}""")
print(f"""Rektangel 2 har side verdier: Side 1={side1_2},
      Side 2={side2_2}, Side 3={side3_2}, Side 4={side4_2}""")
print(f"""Rektangel 3 har side verdier: Side 1={side1_3},
      Side 2={side2_3}, Side 3={side3_3}, Side 4={side4_3}""")
"""
Sirkulasjonen til rektangel 1 ble 1796.013421486005
Sirkulasjonen til rektangel 2 ble -60206.56400779366
Sirkulasjonen til rektangel 3 ble -143.18708039114364
Rektangel 1 har side verdier: Side 1=70100.52387861427,
      Side 2=-100.99982042140701, Side 3=-68332.85609978675, Side 4=129.34546307988458
Rektangel 2 har side verdier: Side 1=198.47559740489203,
      Side 2=919.0821556116496, Side 3=-61243.46477849595, Side 4=-80.65698231424645
Rektangel 3 har side verdier: Side 1=5133.347850903836,
      Side 2=175.1650519009061, Side 3=-5410.039721925995, Side 4=-41.660261269891
"""
"""
g
"""


def gauss(x1, y1, x2, y2):
    side1 = 0
    side2 = 0
    side3 = 0
    side4 = 0
    dx = 0.5
    dy = 0.5

    for k in v[y1, x1:x2+1]:
        side1 -= k*dx

    for k in u[y1:y2+1, x2]:
        side2 += k*dy

    for k in v[y2, x1:x2+1]:
        side3 += k*dx

    for k in u[y1:y2+1, x1]:
        side4 -= k*dy

    sumation = side1 + side2 + side3 + side4
    return sumation, side1, side2, side3, side4


gauss_1, gauss_side1_1, gauss_side2_1, gauss_side3_1, gauss_side4_1 = gauss(34, 159, 69, 169)
gauss_2, gauss_side1_2, gauss_side2_2, gauss_side3_2, gauss_side4_2 = gauss(34, 84, 69, 99)
gauss_3, gauss_side1_3, gauss_side2_3, gauss_side3_3, gauss_side4_3 = gauss(34, 49, 69, 59)

print(f"Fluksen til kurveintegral 1 ble {gauss_1}")
print(f"Fluksen til kurveintegral 2 ble {gauss_2}")
print(f"Fluksen til kurveintegral 3 ble {gauss_3}")

print(f"""Rektangel 1 har side verdier: Side 1={gauss_side1_1},
      Side 2={gauss_side2_1}, Side 3={gauss_side3_1}, Side 4={gauss_side4_1}""")
print(f"""Rektangel 2 har side verdier: Side 1={gauss_side1_2},
      Side 2={gauss_side2_2}, Side 3={gauss_side3_2}, Side 4={gauss_side4_2}""")
print(f"""Rektangel 3 har side verdier: Side 1={gauss_side1_3},
      Side 2={gauss_side2_3}, Side 3={gauss_side3_3}, Side 4={gauss_side4_3}""")

"""
Fluksen til kurveintegral 1 ble 104.8526049082102
Fluksen til kurveintegral 2 ble -6476.93918209796
Fluksen til kurveintegral 3 ble -124.56866604496236
Rektangel 1 har side verdier: Side 1=1556.8679439413959,
      Side 2=21664.567474322168, Side 3=-2059.6771847938708, Side 4=-21056.905628561482
Rektangel 2 har side verdier: Side 1=-5187.564033067891,
      Side 2=14782.532896182345, Side 3=-4074.0522144394345, Side 4=-11997.85583077298
Rektangel 3 har side verdier: Side 1=-195.5701479258336,
      Side 2=1536.8217966413547, Side 3=284.9436464350764, Side 4=-1750.7639611955597
"""
