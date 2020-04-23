import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
"""
oppgave a)
"""

data = sio.loadmat('data.mat')
x = data.get('x')
y = data.get('y')
u = data.get('u')
v = data.get('v')
xit = data.get('xit')
yit = data.get('yit')

print(f"x shape is {np.shape(x)}")
print(f"y shape is {np.shape(y)}")
print(f"u shape is {np.shape(u)}")
print(f"v shape is {np.shape(v)}")
print(f"xit shape is {np.shape(xit)}")
print(f"yit shape is {np.shape(yit)}")

print(x)
print(y)

"""
oppgave b)
"""


velocity = np.sqrt(u**2 + v**2)

plt.subplot(2, 1, 1)
plt.plot(xit, yit, "k*")
water_bender = plt.contourf(x, y, velocity, np.linspace(0, 500, 100))
plt.colorbar(water_bender)

plt.subplot(2, 1, 2)
plt.plot(xit, yit, "k*")
air_bender = plt.contourf(x, y, velocity, np.linspace(1000, 5000, 100))
plt.colorbar(air_bender)

plt.savefig("oppgave_b.png")
plt.show()
