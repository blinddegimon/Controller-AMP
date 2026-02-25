from PySide6.QtCore import Slot
from PySide6.QtGui import QPen, QColor
from pyqtgraph import PlotWidget, mkColor, mkPen

import pyqtgraph as pg
import numpy as np
import array

BUFFER_SIZE = 1000

def to_b16t(i):
    r = bytearray()
    for e in i:
        r += e.to_bytes(2,'little',signed=True)
    return r

class Plot(PlotWidget):

    def __init__(self, bg_plots, parent=None):
        super().__init__(parent, background=(250,250,250))


        self.bg_plots = bg_plots
        self.plot_list = [0 for _ in range(5)]
        self.curve_list = [None for _ in range(5)]
        self.color_list = ((7,41,84), (224,43,51), (240,197,113), (89,168,155), (166,89,169), (206,206,206))
        for i in range(0,5):
            self.curve_list[i] = self.plot(pen = mkPen(self.color_list[i], width=1.5))


        self.update_plot_list(0)

        self.buffer_x = np.linspace(0, BUFFER_SIZE, BUFFER_SIZE)
        self.buffer_y = np.zeros((5, BUFFER_SIZE))
        self.buffer_y_pointer = 0
        self.pause = False

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

    @Slot(int)
    def update_plot_list(self, btn_id: int):
        for i in range(0,5):
            self.plot_list[i] = self.bg_plots.button(i).isChecked()

        if not self.bg_plots.button(btn_id).isChecked() :
            self.curve_list[btn_id].setData(np.zeros(BUFFER_SIZE))

        #print(self.plot_list)

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