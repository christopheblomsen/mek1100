import numpy as np

t = np.linspace(0, 2*np.pi, 1000)

dx = -np.sin(t)
dy = np.cos(t)
dz = np.cos(np.cos(t))*np.sin(np.cos(t))*np.sin(t) - np.cos(np.cos(t))*np.sin(np.sin(t))*np.cos(t)

L = np.trapz(np.sqrt(dx**2 + dy**2 + dz**2), t)

print(L)
