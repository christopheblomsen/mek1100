import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 50)
x, y = np.meshgrid(t, t, indexing="ij")

plt.contour(x, y, -np.cos(x)*np.cos(y), 4)
plt.quiver(x, y, np.cos(x)*np.sin(y), -np.sin(x)*np.cos(y), pivot="middle")

plt.savefig("3b.png")
plt.show()
