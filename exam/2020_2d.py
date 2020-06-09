import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

u, v = psi = sp.symbols("u, v", real=True)
r = (sp.cosh(u)*sp.cos(v), sp.sinh(u)*sp.sin(v))

def basisvektor(psi, r):
    b = np.zeros((len(psi), len(r)), dtype=object)
    for i, ui, in enumerate(psi):
        for j, rj in enumerate(r):
            b[i, j] = sp.simplify(rj.diff(ui, 1))
    return b

def skaleringsfaktor(b):
    h = np.zeros(b.shape[0], dtype=object)
    for i, s in enumerate(np.sum(b**2, axis=1)):
        h[i] = sp.simplify(sp.sqrt(s))
    return h

def enhetsvektor(psi, r):
    b = basisvektor(psi, r)
    hi = skaleringsfaktor(b)
    return b/ hi[None, :], hi

e, h = enhetsvektor(psi, r)

f = (1 - u**2)*sp.cos(2*v)

N = 20
ui = np.broadcast_to(np.linspace(0, 1, N)[:, None], (N, N))
vi = np.broadcast_to(np.linspace(-1, 1, N)[None, :], (N, N))
fj = sp.lambdify((u, v), f)(ui, vi)

mesh = []
for rj in r:
    mesh.append(sp.lambdify((u, v), rj)(ui, vi))
x, y = mesh

plt.contourf(x, y, fj)

df = np.array((1/h[0]*f.diff(u, 1), 1/h[1]*f.diff(v, 1)))

gradf = e[0]*df[0] + e[1]*df[1]

dfdxi = sp.lambdify((u, v), gradf[0])(ui, vi)
dfdyi = sp.lambdify((u, v), gradf[1])(ui, vi)
plt.contourf(x, y, fj)
plt.quiver(x[::10], y[::10], dfdxi[::10], dfdyi[::10], scale=10)

plt.show()
