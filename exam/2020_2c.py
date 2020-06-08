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

e, hi = enhetsvektor(psi, r)

print(e)

