from MainWindow import Ui_MainWindow
import sys
from PyQt6.QtWidgets import *

from Math.Roots import draw_root_picture


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showFullScreen()
        self.menuBar()
        self.ui.exit.aboutToShow.connect(lambda: exit())
        self.ui.calculateButton.clicked.connect(self.calculate)

    def calculate(self):
        upCoef1 = self.ui.upCoef1.toMarkdown().title()
        upCoef2 = self.ui.upCoef2.toMarkdown().title()
        upCoef3 = self.ui.upCoef3.toMarkdown().title()
        upCoef4 = self.ui.upCoef4.toMarkdown().title()
        downCoef1 = self.ui.downCoef1.toMarkdown().title()
        downCoef2 = self.ui.downCoef2.toMarkdown().title()
        downCoef3 = self.ui.downCoef3.toMarkdown().title()
        downCoef4 = self.ui.downCoef4.toMarkdown().title()
        print(upCoef1 + " " + upCoef2 + " " + upCoef3 + " " + upCoef4)
        print(downCoef1 + " " + downCoef2 + " " + downCoef3 + " " + downCoef4)
        draw_root_picture([upCoef1, upCoef2, upCoef3, upCoef4], [downCoef1, downCoef2, downCoef3, downCoef4])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
