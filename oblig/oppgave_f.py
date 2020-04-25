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


def kurveintegral(x1, y1, x2, y2):
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
    return sumation


def flateintegral(x1, y1, x2, y2):
    integral = 0
    dx = 0.5
    dy = 0.5
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            integral += curl_v[j, i]*dx*dy

    return integral


print(kurveintegral(34, 159, 69, 169), kurveintegral(34, 84, 69, 99),
      kurveintegral(34, 49, 69, 59))
print(flateintegral(34, 159, 69, 169), flateintegral(34, 84, 69, 99),
      flateintegral(34, 49, 69, 59))


def gaus(x1, y1, x2, y2):
    side1 = 0
    side2 = 0
    side3 = 0
    side4 = 0
    dx = 0.5
    dy = 0.5
    dz = 1

    for k in v[y1, x1:x2+1]:
        side1 -= k*dx*dz

    for k in u[x2, y1:y2+1]:
        side2 += k*dy*dz

    for k in v[y2, x1:x2+1]:
        side3 += k*dx*dz

    for k in u[x1, y1:y2+1]:
        side4 -= k*dy*dz

    sumation = side1 + side2 + side3 + side4
    return sumation

