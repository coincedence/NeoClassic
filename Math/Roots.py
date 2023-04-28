import numpy as np
import matplotlib.pyplot as plt
from UI import mplwidget


def draw_root_picture(canvas:mplwidget, coeffsNM, coeffsDN):
    canvas.axes.cla()
    canvas.axes.grid()
    draw_roots(canvas, coeffsNM, 'o')
    draw_roots(canvas, coeffsDN, 'x')

    canvas.draw()
    plt.grid()
    plt.show()


def draw_roots(canvas:mplwidget, coeffs, marker):
    tolerance = 0.000000001
    roots = np.roots(coeffs)
    no_imag = True
    no_real = True
    for i in range(len(roots)):
            if abs(roots[i].imag) > tolerance:
                no_imag = False
            if abs(roots[i].real) > tolerance:
                no_real = False
    print(no_imag)
    print(no_real)
    if len(roots) != 0:
        if no_real:
            canvas.axes.set_xlim([-1, 1])
        if no_imag:
            canvas.axes.set_ylim([-1, 1])

    x = [ele.real for ele in roots]
    y = [ele.imag for ele in roots]
    canvas.axes.scatter(x, y, marker=marker)
    canvas.axes.axhline()
    canvas.axes.axvline()
    plt.grid()
    plt.axhline()
    plt.axvline()
    plt.scatter(x, y, marker=marker)
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
