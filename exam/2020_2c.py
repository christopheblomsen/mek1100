import numpy as np
import matplotlib.pyplot as plt

N = 100
u = np.linspace(-3, 3, N)
v = np.linspace(0, 2*np.pi, N)

for i in range(1, 4):
    x = np.cosh(i)*np.cos(v)
    y = np.sinh(i)*np.sin(v)
    plt.plot(x, y, label=f"$\cosh({i}) \cdot \sinh(v)$")

for i in range(1, 7):
    x = np.cosh(u)*np.cos(i)
    y = np.sinh(u)*np.sin(i)
    plt.plot(x, y, label=f"$\cosh(u) \cdot \sinh({i})$")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig("2c.png")
plt.show()
