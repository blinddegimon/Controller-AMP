from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from mainwindow import MainWindow

import pyqtgraph as pg

"""PySide6 Controller for AMP v0.1"""


if __name__ == "__main__":
    #pg.setConfigOptions(useOpenGL = True, antialias = True)
    a = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(a.exec())