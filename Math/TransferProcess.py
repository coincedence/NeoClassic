from control import *
import matplotlib.pyplot as plt
from control.matlab import step

from UI import mplwidget


def draw_transfer_process(canvas: mplwidget, nm, dm):
    canvas.axes.cla()
    num = nm
    den = dm
    print(num)
    print(den)
    w = tf(num, den)


    x, y = step_response(w)
    plt.plot(x,y)
    plt.show()
    canvas.axes.grid()
    canvas.axes.plot(x, y)
    canvas.draw()


if __name__ == "__main__":
    num = [1.]
    den = [1., 1.]
    w = tf(num, den)
    y, x = step(w)
    plt.plot(x, y, "b")
    plt.title('Step Responsse ')
    plt.ylabel('Amplitude')
    plt.xlabel('Time(sec)')
    plt.grid(True)
    plt.show()
