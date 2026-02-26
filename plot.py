from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPen, QColor
from pyqtgraph import PlotWidget, mkColor, mkPen

import pyqtgraph as pg
import numpy as np
import array

BUFFER_SIZE = 2000

def to_b16t(i):
    r = bytearray()
    for e in i:
        r += e.to_bytes(2,'little',signed=True)
    return r

class CustomViewBox(pg.ViewBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMouseMode(pg.ViewBox.RectMode)

    def mouseClickEvent(self, ev):
        if ev.button() == Qt.MouseButton.MiddleButton:
            self.show_custom_menu(ev)
            ev.accept()
        elif ev.button() == Qt.MouseButton.RightButton:
            self.enableAutoRange()
            ev.accept()
        else:
            super().mouseClickEvent(ev)

    def show_custom_menu(self, ev):
        menu = self.getMenu(ev)  # default pyqtgraph menu
        menu.popup(ev.screenPos().toPoint())

class Plot(PlotWidget):

    def __init__(self, bg_plots, parent=None):
        super().__init__(parent, background=(250,250,250), viewBox = CustomViewBox())

        #self.showGrid(x=True, y=True, alpha=0.3)

        self.getAxis('bottom').setStyle(maxTickLevel = 0)
        self.getAxis('left').setStyle(maxTickLevel = 0)

        self.getViewBox().setLimits(xMin = 0, xMax = BUFFER_SIZE)
        #self.getViewBox().enableAutoRange()

        self.curves_amount = 6

        self.bg_plots = bg_plots
        self.plot_list = [True for _ in range(self.curves_amount)]
        self.curve_list = [None for _ in range(self.curves_amount)]
        self.color_list = ((7,41,84), (224,43,51), (240,197,113), (89,168,155), (166,89,169), (0,250,0))
        for i in range(0,self.curves_amount):
            self.curve_list[i] = self.plot(pen = mkPen(self.color_list[i], width=1))





        self.buffer_x = np.linspace(0, BUFFER_SIZE, BUFFER_SIZE)
        self.buffer_y = np.zeros((self.curves_amount, BUFFER_SIZE))
        self.buffer_y_pointer = 0
        self.pause = False

        self.update_plot_list(0)

        self.setRange(xRange=[0, BUFFER_SIZE])
        self.showGrid(x=True, y=True)

    def update_buffer_y(self, data):
        buffer_temp = data
        if not self.pause:
            for i, val in enumerate(self.plot_list):
                if val:
                    self.buffer_y[i] = np.roll(self.buffer_y[i], shift=-1)
                    self.buffer_y[i][BUFFER_SIZE - 1] = buffer_temp[i]


                #self.curve_list[i].setData(self.buffer_y[i])
                #self.curve1.setData(self.buffer_y[0])

    @Slot()
    def update_plot(self):
        if not self.pause:
            for i, val in enumerate(self.plot_list):
                if val:
                    self.curve_list[i].setData(self.buffer_y[i])

    def update_pl(self):
        for i, val in enumerate(self.plot_list):
            if val:
                self.curve_list[i].setData(self.buffer_y[i])

    @Slot(int)
    def update_plot_list(self, btn_id: int):

        for i in range(0,5):
            self.plot_list[i] = self.bg_plots.button(i).isChecked()

        self.update_pl()

        if not self.bg_plots.button(btn_id).isChecked() :
            self.curve_list[btn_id].setData(np.zeros(BUFFER_SIZE))

    @Slot()
    def update_pause(self):
        if self.pause:
            self.pause = False
        else:
            self.pause = True

    @Slot()
    def clear_plot(self):
        for i, val in enumerate(self.plot_list):
            self.buffer_y[i] = np.zeros(BUFFER_SIZE)
            self.curve_list[i].setData(self.buffer_y[i])