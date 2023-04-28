import matplotlib.pyplot as plt
from control.matlab import *

from UI import mplwidget


def draw_weight(canvas: mplwidget, nm, dm):
    canvas.axes.cla()
    num = nm
    den = dm
    print(num)
    print(den)
    w = tf(num, den)

    y, x = impulse(w)
    canvas.axes.grid()
    canvas.axes.plot(x, y)
    canvas.draw()

if __name__ == "__main__":
    num = [1]
    den = [1,2,1]
    print(num)
    print(den)
    w = tf(num, den)

    y, x = impulse(w)
    plt.plot(x, y)
    plt.show()

