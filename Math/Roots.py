import numpy as np
import matplotlib.pyplot as plt


def draw_root_picture(coeffsNM, coeffsDN):
    draw_roots(coeffsNM, 'o')
    draw_roots(coeffsDN, 'x')
    plt.grid()
    plt.show()
def draw_roots(coeffs, marker):
    roots = np.roots(coeffs)

    x = [ele.real for ele in roots]
    y = [ele.imag for ele in roots]

    plt.grid()
    plt.axhline()
    plt.axvline()
    plt.scatter(x, y, marker=marker)
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
