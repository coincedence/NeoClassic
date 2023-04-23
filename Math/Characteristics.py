from control import *
import matplotlib.pyplot as plt
from numpy import rad2deg

from UI import mplwidget


def draw_characteristics(mag_canvas: mplwidget, phase_canvas: mplwidget, nm, dm):
    mag_canvas.axes.cla()
    phase_canvas.axes.cla()
    mag_canvas.axes.grid()
    phase_canvas.axes.grid()

    w = tf(nm, dm)
    mag, phase, omega = bode(w, dB=True)
    for i in range(len(phase)):
        phase[i] = rad2deg(phase[i])

    mag_canvas.axes.set_xscale('log')
    mag_canvas.axes.plot(omega, mag2db(mag))

    phase_canvas.axes.set_xscale('log')
    phase_canvas.axes.plot(omega, phase)

    plt.plot()
    plt.show()

    mag_canvas.draw()
    phase_canvas.draw()


if __name__ == "__main__":
    num = [1.]
    den = [1., 1.]
    w = tf(num, den)
    mag, phase, omega = bode_plot(w, dB=True)
    plt.plot()
    plt.show()
