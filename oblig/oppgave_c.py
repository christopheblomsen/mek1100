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

    # Right
    plt.plot([position2[0], position2[0]], [position1[1], position2[1]], "g")

    # Top
    plt.plot([position1[0], position2[0]], [position2[1], position2[1]], "b")

    # Left
    plt.plot([position1[0], position1[0]], [position1[1], position2[1]], "k")


def draw_rectangles():
    rectangle1_values = [35, 160, 70, 170]
    rectangle(rectangle1_values[0], rectangle1_values[1],
              rectangle1_values[2], rectangle1_values[3])

    rectangle2_values = [35, 85, 70, 100]
    rectangle(rectangle2_values[0], rectangle2_values[1],
              rectangle2_values[2], rectangle2_values[3])

    rectangle3_values = [35, 50, 70, 60]
    rectangle(rectangle3_values[0], rectangle3_values[1],
              rectangle3_values[2], rectangle3_values[3])


plt.plot(xit, yit, "k*")
num_skip = 5
plt.quiver(x[::num_skip, ::num_skip], y[::num_skip, ::num_skip],
           u[::num_skip, ::num_skip], v[::num_skip, ::num_skip])

plt.title("Oppgave c)")
plt.xlabel("x")
plt.ylabel("y")

plt.savefig("oppgave_c.png")

"""
oppgave d
"""

dudx = np.gradient(u, axis=0)
dvdy = np.gradient(v, axis=1)

divergence = dudx + dvdy
print(f"The divergence is {divergence}")

plt.contourf(x, y, divergence)
plt.colorbar()
plt.title("Oppgave d)")
plt.savefig("oppgave_d.png")
plt.close()

"""
oppgave e
Had to redraw a lot so first couple of lines are just that
"""
draw_rectangles()
plt.plot(xit, yit, "k*")
num_skip = 5
plt.quiver(x[::num_skip, ::num_skip], y[::num_skip, ::num_skip],
           u[::num_skip, ::num_skip], v[::num_skip, ::num_skip])
plt.plot(xit, yit, "k*")
"""
New stuff
"""

dudy = np.gradient(u, axis=1)
dvdx = np.gradient(v, axis=0)

curl_v = dvdx - dudy

curl_plot = plt.contourf(x, y, curl_v)
plt.colorbar()

plt.title("Oppgave e)")

plt.savefig("oppgave_e.png")
plt.show()
