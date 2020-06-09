import sympy as sp
import matplotlib.pyplot as plt

a, b, t, v = sp.symbols("a, b, t, v")

x = sp.cos(a)*sp.sin(b)*sp.exp(-2*v*t)
y = -sp.sin(a)*sp.cos(b)*sp.exp(-2vt)
N = 100
t = np.linspace(- np.pi, np.pi, N)

