from PySide6.QtCore import QIODeviceBase, Slot, QByteArray, QTimer, QThread, QObject, Signal
from PySide6.QtWidgets import QLabel, QMainWindow, QMessageBox, QGraphicsView, QLineEdit, QWidget, QCheckBox, QComboBox, QRadioButton
from PySide6.QtSerialPort import QSerialPort
from PySide6.QtGui import QShortcut

from plot import CustomViewBox
from ui_mainwindow import Ui_MainWindow
from settingsdialog import SettingsDialog
import pyqtgraph as pg
import numpy as np
import array
import json
import plot as plt
import time

BUFFER_SIZE = 1000

def to_b16t(i):
    r = bytearray()
    for e in i:
        r += e.to_bytes(2,'little',signed=True)
    return r

def description(s):
    return (f"Connected to {s.name} : {s.string_baud_rate}, "
            f"{s.string_data_bits}, {s.string_parity}, {s.string_stop_bits}, "
            f"{s.string_flow_control}")

class SerialWorker(QObject):
    data_ready = Signal(bytes)

    def __init__(self):
        super().__init__()
        self.serial = QSerialPort()
        self.serial.readyRead.connect(self.handle_ready_read)
        self.packets = 0
        self.bad_packets = 0

    def handle_ready_read(self):
        data = self.serial.readAll()
        # buffer_temp = np.array(array.array('h', bytes(data)))
        # self.packets += 1
        # if len(buffer_temp) > 7:
        #     self.bad_packets +=1
        # print(1- (self.bad_packets/self.packets))
        self.data_ready.emit(data)

#QLineEdit, QCheckBox, QComboBox
class AppConfig:
    def __init__(self):
        self.widgets = {}
        self.widget_dict = {}

    def add_widget(self, widget):
        self.widgets[widget.objectName()] = widget

    def save_widgets(self):
        for name, widget in self.widgets.items():
            match = self.match_widget(widget)
            self.widget_dict[match[0]] = match[1]

        with open('config_widgets.json', 'w', encoding='utf-8') as f:
            json.dump(self.widget_dict, f, ensure_ascii=False, indent=4)

    def load_widgets(self):
        with open('config_widgets.json', 'r+', encoding='utf-8') as f:
            self.widget_dict = json.load(f)

        for name, value in self.widget_dict.items():
            self.write_widget(self.widgets[name], value)

    @staticmethod
    def match_widget(widget):
        key = ""
        value = ""
        key = widget.objectName()
        match widget:
            case QLineEdit():
                value = widget.text()
                #print("QLineEdit")
            case QCheckBox() | QRadioButton():
                value = widget.isChecked()
                #print("QCheckBox")
            case QComboBox():
                value = widget.currentIndex()
                #print("QComboBox")
            case _:
                print("something went wrong")

        return key, value

    @staticmethod
    def write_widget(widget, value):

        match widget:
            case QLineEdit():
                widget.setText(value)
                #print("QLineEdit: ", value)
            case QCheckBox() | QRadioButton():
                widget.setChecked(value)
                #print("QCheckBox")
            case QComboBox():
                widget.setCurrentIndex(value)
                #print("QComboBox")
            case _:
                print("something went wrong")

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.timer = QTimer()
        self.timer_plot = QTimer()
        self.timer_gen = QTimer()
        self.m_ui = Ui_MainWindow()
        self.m_settings = SettingsDialog(self)
        self.m_status = QLabel()
        self.m_serial = QSerialPort(self)
        # self.serial_worker = SerialWorker()
        # self.m_serial = self.serial_worker.serial
        # self.serial_thread = QThread()
        self.m_ui.setupUi(self)
        self.config_settings = AppConfig()


        self.prev_time = time.time()

        self.buffer_speed = np.zeros(BUFFER_SIZE)

        self.pos = 0
        self.prev_pos = 0

        self.gen_start_pos = 0
        self.gen_pos = 0
        self.gen_sign = True

        self.packets = 0
        self.bad_packets = 0

        self.shortcut_update = QShortcut(self)
        self.shortcut_update.setKey('q')

        self.shortcut_auto_range = QShortcut(self)
        self.shortcut_auto_range.setKey('r')

        self.config_settings.add_widget(self.m_ui.cb_enable)
        self.config_settings.add_widget(self.m_ui.cb_mode)
        self.config_settings.add_widget(self.m_ui.le_setPos)
        self.config_settings.add_widget(self.m_ui.le_setPos1)
        self.config_settings.add_widget(self.m_ui.le_setPos2)
        self.config_settings.add_widget(self.m_ui.le_setPos3)

        self.config_settings.add_widget(self.m_ui.le_pwm)
        self.config_settings.add_widget(self.m_ui.le_paP)
        self.config_settings.add_widget(self.m_ui.le_paD)
        self.config_settings.add_widget(self.m_ui.le_zeroShift)
        self.config_settings.add_widget(self.m_ui.le_speed)


        self.config_settings.add_widget(self.m_ui.radioButton)
        self.config_settings.add_widget(self.m_ui.lineEdit)

        self.config_settings.add_widget(self.m_ui.radioButton_2)
        self.config_settings.add_widget(self.m_ui.lineEdit_2)

        self.config_settings.add_widget(self.m_ui.radioButton_3)
        self.config_settings.add_widget(self.m_ui.lineEdit_3)

        self.config_settings.add_widget(self.m_ui.radioButton_4)
        self.config_settings.add_widget(self.m_ui.lineEdit_4)

        self.config_settings.add_widget(self.m_ui.radioButton_5)
        self.config_settings.add_widget(self.m_ui.lineEdit_5)


        #self.config_settings.load_widgets()
        try:
            self.config_settings.load_widgets()
        except:
            pass

        self.m_ui.bg_send.setId(self.m_ui.pb_send, 0)
        self.m_ui.bg_send.setId(self.m_ui.pb_setPos1, 1)
        self.m_ui.bg_send.setId(self.m_ui.pb_setPos2, 2)
        self.m_ui.bg_send.setId(self.m_ui.pb_setPos3, 3)

        self.m_ui.bg_plots.setId(self.m_ui.radioButton, 0)
        self.m_ui.bg_plots.setId(self.m_ui.radioButton_2, 1)
        self.m_ui.bg_plots.setId(self.m_ui.radioButton_3, 2)
        self.m_ui.bg_plots.setId(self.m_ui.radioButton_4, 3)
        self.m_ui.bg_plots.setId(self.m_ui.radioButton_5, 4)

        self.timer.start(1000)
        self.timer_plot.start(33)
        self.pps = 0
        self.prev_pps = 0

        self.le_list = (self.m_ui.le_setPos, self.m_ui.le_setPos1, self.m_ui.le_setPos2, self.m_ui.le_setPos3)

        self.send_buffer = [0 for _ in range(64)]

        self.plot = plt.Plot(self.m_ui.bg_plots)
        #self.plot.setMenuEnabled(False)
        self.m_ui.vl_plot.addWidget(self.plot)

        for i, b in enumerate(self.m_ui.bg_clrPlots.buttons()):
            b.setStyleSheet("background-color:rgb" + str(self.plot.color_list[i]) + ";")


        self.m_ui.statusbar.addWidget(self.m_status)

        self.m_ui.actionConnect.triggered.connect(self.open_serial_port)
        self.m_ui.actionDisconnect.triggered.connect(self.close_serial_port)
        self.m_ui.bg_send.idClicked.connect(self.send_data)
        self.m_ui.pb_updateConf.clicked.connect(self.send_config)
        self.m_ui.pb_readMem.clicked.connect(self.send_read_mem)
        self.m_ui.pb_readConf.clicked.connect(self.send_read_config)
        self.m_ui.pb_saveConf.clicked.connect(self.send_config_save)
        self.m_ui.actionConfigure.triggered.connect(self.m_settings.show)
        self.m_ui.actionStop.triggered.connect(self.send_disable)

        self.m_ui.pb_gen.clicked.connect(self.timer_gen_start)



        self.m_ui.actionPause.triggered.connect(self.plot.update_pause)
        self.m_ui.actionClear.triggered.connect(self.plot.clear_plot)
        self.m_ui.bg_plots.idClicked.connect(self.plot.update_plot_list)
        self.shortcut_update.activated.connect(self.m_ui.pb_updateConf.click)
        self.shortcut_auto_range.activated.connect(self.auto_range)

        self.m_ui.actionConnect.setEnabled(True)
        self.m_ui.actionDisconnect.setEnabled(False)


        # self.serial_worker.moveToThread(self.serial_thread)
        # self.serial_worker.data_ready.connect(self.read_data)
        # self.serial_thread.start()
        self.m_serial.errorOccurred.connect(self.handle_error)
        self.m_serial.readyRead.connect(self.read_data)

        self.timer.timeout.connect(self.update_timer)
        self.timer_plot.timeout.connect(self.plot.update_plot)
        self.timer_gen.timeout.connect(self.update_gen)

    @Slot()
    def timer_gen_start(self, btn):
        self.gen_start_pos = self.pos
        print(btn)

        if btn:
            self.timer_gen.start(1000/self.m_ui.sb_genFreq.value())
        else:
            self.timer_gen.stop()

    @Slot()
    def update_gen(self):

        sign = 1 if self.gen_sign else -1
        self.gen_sign = True if not self.gen_sign else False

        self.gen_pos = self.gen_start_pos + sign*(self.m_ui.sb_genAmpl.value()*91)

        self.send_buffer[0] = 0x6788
        self.send_buffer[1] = self.m_ui.cb_enable.isChecked()
        self.send_buffer[2] = 1
        self.send_buffer[3] = int(self.gen_pos)

        buffer = QByteArray(to_b16t(self.send_buffer))
        self.m_serial.write(buffer)


    @Slot()
    def update_timer(self):
        #print("packets per second", self.pps)
        self.m_ui.l_pps.setText(str(self.pps)+"sps")
        self.prev_pps = self.pps
        self.pps = 0

    @Slot()
    def open_serial_port(self):
        s = self.m_settings.settings()
        self.m_serial.setPortName(s.name)
        self.m_serial.setBaudRate(s.baud_rate)
        self.m_serial.setDataBits(s.data_bits)
        self.m_serial.setParity(s.parity)
        self.m_serial.setStopBits(s.stop_bits)
        self.m_serial.setFlowControl(s.flow_control)
        self.m_serial.setReadBufferSize(12)
        if self.m_serial.open(QIODeviceBase.OpenModeFlag.ReadWrite):
            #self.m_console.setEnabled(True)
            #self.m_console.set_local_echo_enabled(s.local_echo_enabled)
            self.m_ui.actionConnect.setEnabled(False)
            self.m_ui.actionDisconnect.setEnabled(True)
            self.m_ui.actionConfigure.setEnabled(False)
            self.show_status_message(description(s))
        else:
            QMessageBox.critical(self, "Error", self.m_serial.errorString())
            self.show_status_message("Open error")


    @Slot()
    def close_serial_port(self):
        if self.m_serial.isOpen():
            self.m_serial.close()
        self.m_ui.actionConnect.setEnabled(True)
        self.m_ui.actionDisconnect.setEnabled(False)
        self.m_ui.actionConfigure.setEnabled(True)
        self.show_status_message("Disconnected")

    @Slot(str)
    def show_status_message(self, message):
        self.m_status.setText(message)

    @Slot()
    def handle_data(self, data):
        self.m_ui.lr_angle.setText(str(f'{(1 - data): .2f}'))

    @Slot()
    def read_data(self):
        self.pps += 1
        buffer_temp = np.array(array.array('h', bytes(self.m_serial.readAll())))
        #buffer_temp = np.array(array.array('h', bytes(data)))

        self.packets += 1
        if len(buffer_temp) > 7:
            self.bad_packets +=1

        self.buffer_speed = np.roll(self.buffer_speed, shift=-1)
        #self.buffer_speed[BUFFER_SIZE - 1] = (abs(self.prev_pos - self.pos) / (time.time() - self.prev_time))/91
        elapsed_time = time.time() - self.prev_time
        distance = abs(self.prev_pos - self.pos)
        speed = distance * self.prev_pps

        self.prev_time = time.time()

        buffer_temp = buffer_temp[0:6]
        match buffer_temp[0]:
            case 0x6777 | 0x6782:
                self.update_config(buffer_temp)
            case 0x6700:
                buffer_temp = np.append(buffer_temp, speed/91)
                self.plot.update_buffer_y(buffer_temp[1:])

                self.prev_pos = self.pos
                self.pos = buffer_temp[4]

                angle = buffer_temp[4]
                if self.m_ui.cb_degrees.isChecked():
                    angle /= 91


                self.m_ui.lr_angle.setText(str(f'{angle: .2f}'))





    @Slot(int)
    def send_data(self, btn_id: int):
        self.send_buffer[0] = 0x6788
        self.send_buffer[1] = self.m_ui.cb_enable.isChecked()
        self.send_buffer[2] = self.m_ui.cb_mode.isChecked()
        self.send_buffer[3] = int(self.le_list[btn_id].text())

        buffer = QByteArray(to_b16t(self.send_buffer))
        self.m_serial.write(buffer)

    @Slot()
    def send_disable(self):
        self.send_buffer[0] = 0x6788
        self.send_buffer[1] = 0

        buffer = QByteArray(to_b16t(self.send_buffer))
        self.m_serial.write(buffer)

    @Slot()
    def send_read_mem(self):
        self.send_buffer[0] = 0x6777

        buffer = QByteArray(to_b16t(self.send_buffer))
        self.m_serial.write(buffer)

    @Slot()
    def send_read_config(self):
        self.send_buffer[0] = 0x6782

        buffer = QByteArray(to_b16t(self.send_buffer))
        self.m_serial.write(buffer)

    @Slot()
    def send_config_save(self):
        self.send_buffer[0] = 0x6783

        buffer = QByteArray(to_b16t(self.send_buffer))
        self.m_serial.write(buffer)

    @Slot()
    def send_config(self):
        print("update")
        self.send_buffer[0] = 0x6770
        self.send_buffer[1] = int(self.m_ui.le_pwm.text())
        self.send_buffer[2] = int(float(self.m_ui.le_paP.text()) * 1000)
        self.send_buffer[3] = int(float(self.m_ui.le_paD.text()) * 1000)
        self.send_buffer[4] = int(self.m_ui.le_zeroShift.text())
        self.send_buffer[5] = int(self.m_ui.le_speed.text())

        buffer = QByteArray(to_b16t(self.send_buffer))
        self.m_serial.write(buffer)

    @Slot(QSerialPort.SerialPortError)
    def handle_error(self, error):
        if error == QSerialPort.SerialPortError.ResourceError:
            QMessageBox.critical(self, "Critical Error",
                                 self.m_serial.errorString())
            self.close_serial_port()

    @Slot()
    def auto_range(self):
        #self.plot.getViewBox().autoRange()
        self.plot.getViewBox().enableAutoRange()

    def update_config(self, data):
        self.m_ui.lr_pwm.setText(str(data[1]))
        self.m_ui.lr_paP.setText(str(data[2]/1000))
        self.m_ui.lr_paD.setText(str(data[3]/1000))
        self.m_ui.lr_zeroShift.setText(str(data[4]))
        self.m_ui.lr_speed.setText(str(data[5]))

    def closeEvent(self, event):
        self.config_settings.save_widgets()

