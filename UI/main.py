from MainWindow import Ui_MainWindow
import sys
from PyQt6.QtWidgets import *
from pyqtgraph import PlotWidget, plot

from Math.Characteristics import draw_characteristics
from Math.Roots import draw_root_picture
from Math.TransferProcess import draw_transfer_process


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showFullScreen()
        self.menuBar()
        self.ui.exit.aboutToShow.connect(lambda: exit())

        self.ui.calculateButton.clicked.connect(self.update_graphs)

    def update_graphs(self):
        upCoef1 = float(self.ui.upCoef1.toMarkdown().title())
        upCoef2 = float(self.ui.upCoef2.toMarkdown().title())
        upCoef3 = float(self.ui.upCoef3.toMarkdown().title())
        upCoef4 = float(self.ui.upCoef4.toMarkdown().title())
        downCoef1 = float(self.ui.downCoef1.toMarkdown().title())
        downCoef2 = float(self.ui.downCoef2.toMarkdown().title())
        downCoef3 = float(self.ui.downCoef3.toMarkdown().title())
        downCoef4 = float(self.ui.downCoef4.toMarkdown().title())

        nm = [upCoef1, upCoef2, upCoef3, upCoef4]
        dm = [downCoef1, downCoef2, downCoef3, downCoef4]

        draw_root_picture(self.ui.root_picture.canvas, nm, dm)
        draw_transfer_process(self.ui.h_from_t.canvas, nm, dm)
        draw_characteristics(self.ui.magnitude_graph.canvas, self.ui.phase_graph.canvas, nm, dm)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
