import time

import sympy as sp
import matplotlib.pyplot as plt
from sympy.abc import s, t


def draw_transfer_process(nm, dm, tk):
    fp = ((nm[0] + nm[1] * s + nm[2] * (s ** 2)) / (dm[0] + dm[1] * s + dm[2] * (s ** 2))) / s
    ht = sp.inverse_laplace_transform(fp, s, t)
    f = sp.lambdify(t, ht, modules=['numpy', 'sympy'])
    dt = 0.01
    n = int(tk/dt)
    k = 1
    t0 = 0
    x = [0] * n
    y = [0] * n

    if str(f(0)).__contains__("DiracDelta(0)"):
        t0 += dt
        k += 1
        if f(1) == 0:
            arr_len = 1
        else:
            arr_len = float(f(1))
        plt.arrow(0, 0, 0, arr_len, length_includes_head=True, width=5 * dt, head_width=arr_len * 0.1,
                  head_length=arr_len * 0.05, edgecolor='none')
    else:
        x[0] = 0
        y[0] = 0
    for i in range(k, n):
        x[i] = t0
        y[i] = f(x[i])
        # k += 1
        t0 += dt
    plt.plot(x, y)
    plt.show()
