# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowJJPnME.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QStatusBar, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(828, 690)
        self.actionConnect = QAction(MainWindow)
        self.actionConnect.setObjectName(u"actionConnect")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaylistShuffle))
        self.actionConnect.setIcon(icon)
        self.actionDisconnect = QAction(MainWindow)
        self.actionDisconnect.setObjectName(u"actionDisconnect")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemLogOut))
        self.actionDisconnect.setIcon(icon1)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionConfigure = QAction(MainWindow)
        self.actionConfigure.setObjectName(u"actionConfigure")
        self.actionClear = QAction(MainWindow)
        self.actionClear.setObjectName(u"actionClear")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.actionClear.setIcon(icon2)
        self.actionClear.setMenuRole(QAction.MenuRole.NoRole)
        self.actionPause = QAction(MainWindow)
        self.actionPause.setObjectName(u"actionPause")
        self.actionPause.setCheckable(True)
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackPause))
        self.actionPause.setIcon(icon3)
        self.actionPause.setMenuRole(QAction.MenuRole.NoRole)
        self.actionStop = QAction(MainWindow)
        self.actionStop.setObjectName(u"actionStop")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStop))
        self.actionStop.setIcon(icon4)
        self.actionStop.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_5.addWidget(self.lineEdit, 4, 0, 1, 2)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_5.addWidget(self.lineEdit_2, 0, 0, 1, 2)

        self.radioButton_5 = QRadioButton(self.centralwidget)
        self.bg_plots = QButtonGroup(MainWindow)
        self.bg_plots.setObjectName(u"bg_plots")
        self.bg_plots.setExclusive(False)
        self.bg_plots.addButton(self.radioButton_5)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setChecked(False)
        self.radioButton_5.setAutoExclusive(False)

        self.gridLayout_5.addWidget(self.radioButton_5, 11, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_5.addWidget(self.lineEdit_4, 8, 0, 1, 2)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_5.addWidget(self.lineEdit_3, 6, 0, 1, 2)

        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.bg_plots.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setAutoExclusive(False)

        self.gridLayout_5.addWidget(self.radioButton_2, 5, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_5.addWidget(self.lineEdit_5, 10, 0, 1, 2)

        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.bg_plots.addButton(self.radioButton_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setAutoExclusive(False)

        self.gridLayout_5.addWidget(self.radioButton_3, 7, 0, 1, 1)

        self.radioButton = QRadioButton(self.centralwidget)
        self.bg_plots.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)
        self.radioButton.setAutoExclusive(False)

        self.gridLayout_5.addWidget(self.radioButton, 2, 0, 1, 1)

        self.radioButton_4 = QRadioButton(self.centralwidget)
        self.bg_plots.addButton(self.radioButton_4)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setAutoExclusive(False)

        self.gridLayout_5.addWidget(self.radioButton_4, 9, 0, 1, 1)

        self.pb_clrPlot_1 = QPushButton(self.centralwidget)
        self.bg_clrPlots = QButtonGroup(MainWindow)
        self.bg_clrPlots.setObjectName(u"bg_clrPlots")
        self.bg_clrPlots.setExclusive(False)
        self.bg_clrPlots.addButton(self.pb_clrPlot_1)
        self.pb_clrPlot_1.setObjectName(u"pb_clrPlot_1")
        self.pb_clrPlot_1.setAutoFillBackground(True)

        self.gridLayout_5.addWidget(self.pb_clrPlot_1, 2, 1, 1, 1)

        self.pb_clrPlot_2 = QPushButton(self.centralwidget)
        self.bg_clrPlots.addButton(self.pb_clrPlot_2)
        self.pb_clrPlot_2.setObjectName(u"pb_clrPlot_2")

        self.gridLayout_5.addWidget(self.pb_clrPlot_2, 5, 1, 1, 1)

        self.pb_clrPlot_3 = QPushButton(self.centralwidget)
        self.bg_clrPlots.addButton(self.pb_clrPlot_3)
        self.pb_clrPlot_3.setObjectName(u"pb_clrPlot_3")

        self.gridLayout_5.addWidget(self.pb_clrPlot_3, 7, 1, 1, 1)

        self.pb_clrPlot_4 = QPushButton(self.centralwidget)
        self.bg_clrPlots.addButton(self.pb_clrPlot_4)
        self.pb_clrPlot_4.setObjectName(u"pb_clrPlot_4")

        self.gridLayout_5.addWidget(self.pb_clrPlot_4, 9, 1, 1, 1)

        self.pb_clrPlot_5 = QPushButton(self.centralwidget)
        self.bg_clrPlots.addButton(self.pb_clrPlot_5)
        self.pb_clrPlot_5.setObjectName(u"pb_clrPlot_5")

        self.gridLayout_5.addWidget(self.pb_clrPlot_5, 11, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_5)

        self.vl_plot = QVBoxLayout()
        self.vl_plot.setObjectName(u"vl_plot")

        self.horizontalLayout.addLayout(self.vl_plot)

        self.horizontalLayout.setStretch(1, 1500)

        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_setPos1 = QPushButton(self.centralwidget)
        self.bg_send = QButtonGroup(MainWindow)
        self.bg_send.setObjectName(u"bg_send")
        self.bg_send.addButton(self.pb_setPos1)
        self.pb_setPos1.setObjectName(u"pb_setPos1")

        self.gridLayout.addWidget(self.pb_setPos1, 3, 2, 1, 1)

        self.pb_send = QPushButton(self.centralwidget)
        self.bg_send.addButton(self.pb_send)
        self.pb_send.setObjectName(u"pb_send")

        self.gridLayout.addWidget(self.pb_send, 6, 0, 1, 2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.le_setPos3 = QLineEdit(self.centralwidget)
        self.le_setPos3.setObjectName(u"le_setPos3")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.le_setPos3.setFont(font1)

        self.gridLayout.addWidget(self.le_setPos3, 5, 3, 1, 1)

        self.cb_mode = QCheckBox(self.centralwidget)
        self.cb_mode.setObjectName(u"cb_mode")

        self.gridLayout.addWidget(self.cb_mode, 4, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setKerning(True)
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 4)

        self.le_setPos = QLineEdit(self.centralwidget)
        self.le_setPos.setObjectName(u"le_setPos")
        self.le_setPos.setFont(font1)

        self.gridLayout.addWidget(self.le_setPos, 5, 1, 1, 1)

        self.cb_enable = QCheckBox(self.centralwidget)
        self.cb_enable.setObjectName(u"cb_enable")

        self.gridLayout.addWidget(self.cb_enable, 3, 1, 1, 1)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.gridLayout.addWidget(self.label_14, 0, 2, 1, 1)

        self.pb_setPos3 = QPushButton(self.centralwidget)
        self.bg_send.addButton(self.pb_setPos3)
        self.pb_setPos3.setObjectName(u"pb_setPos3")

        self.gridLayout.addWidget(self.pb_setPos3, 5, 2, 1, 1)

        self.le_setPos1 = QLineEdit(self.centralwidget)
        self.le_setPos1.setObjectName(u"le_setPos1")
        self.le_setPos1.setFont(font1)

        self.gridLayout.addWidget(self.le_setPos1, 3, 3, 1, 1)

        self.le_setPos2 = QLineEdit(self.centralwidget)
        self.le_setPos2.setObjectName(u"le_setPos2")
        self.le_setPos2.setFont(font1)

        self.gridLayout.addWidget(self.le_setPos2, 4, 3, 1, 1)

        self.l_pps = QLabel(self.centralwidget)
        self.l_pps.setObjectName(u"l_pps")

        self.gridLayout.addWidget(self.l_pps, 6, 3, 1, 1)

        self.pb_setPos2 = QPushButton(self.centralwidget)
        self.bg_send.addButton(self.pb_setPos2)
        self.pb_setPos2.setObjectName(u"pb_setPos2")

        self.gridLayout.addWidget(self.pb_setPos2, 4, 2, 1, 1)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)

        self.cb_degrees = QCheckBox(self.centralwidget)
        self.cb_degrees.setObjectName(u"cb_degrees")

        self.gridLayout.addWidget(self.cb_degrees, 0, 3, 1, 1)

        self.lr_angle = QLineEdit(self.centralwidget)
        self.lr_angle.setObjectName(u"lr_angle")
        self.lr_angle.setFont(font1)
        self.lr_angle.setReadOnly(True)

        self.gridLayout.addWidget(self.lr_angle, 0, 1, 1, 1)

        self.pb_gen = QPushButton(self.centralwidget)
        self.pb_gen.setObjectName(u"pb_gen")
        self.pb_gen.setCheckable(True)

        self.gridLayout.addWidget(self.pb_gen, 1, 0, 1, 1)

        self.sb_genFreq = QSpinBox(self.centralwidget)
        self.sb_genFreq.setObjectName(u"sb_genFreq")
        self.sb_genFreq.setWrapping(False)
        self.sb_genFreq.setMinimum(1)

        self.gridLayout.addWidget(self.sb_genFreq, 1, 1, 1, 1)

        self.sb_genAmpl = QSpinBox(self.centralwidget)
        self.sb_genAmpl.setObjectName(u"sb_genAmpl")
        self.sb_genAmpl.setMinimum(1)

        self.gridLayout.addWidget(self.sb_genAmpl, 1, 2, 1, 1)

        self.gridLayout.setColumnStretch(0, 50)
        self.gridLayout.setColumnStretch(1, 50)
        self.gridLayout.setColumnStretch(2, 50)
        self.gridLayout.setColumnStretch(3, 50)

        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lr_zeroShift = QLineEdit(self.centralwidget)
        self.lr_zeroShift.setObjectName(u"lr_zeroShift")
        self.lr_zeroShift.setFont(font1)
        self.lr_zeroShift.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lr_zeroShift, 5, 1, 1, 2)

        self.pb_saveConf = QPushButton(self.centralwidget)
        self.pb_saveConf.setObjectName(u"pb_saveConf")

        self.gridLayout_2.addWidget(self.pb_saveConf, 7, 4, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.le_zeroShift = QLineEdit(self.centralwidget)
        self.le_zeroShift.setObjectName(u"le_zeroShift")
        self.le_zeroShift.setFont(font1)

        self.gridLayout_2.addWidget(self.le_zeroShift, 5, 3, 1, 2)

        self.pb_updateConf = QPushButton(self.centralwidget)
        self.pb_updateConf.setObjectName(u"pb_updateConf")

        self.gridLayout_2.addWidget(self.pb_updateConf, 7, 3, 1, 1)

        self.le_paD = QLineEdit(self.centralwidget)
        self.le_paD.setObjectName(u"le_paD")
        self.le_paD.setFont(font1)

        self.gridLayout_2.addWidget(self.le_paD, 4, 3, 1, 2)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 1, 1, 1, 2)

        self.pb_readConf = QPushButton(self.centralwidget)
        self.pb_readConf.setObjectName(u"pb_readConf")

        self.gridLayout_2.addWidget(self.pb_readConf, 7, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.lr_paD = QLineEdit(self.centralwidget)
        self.lr_paD.setObjectName(u"lr_paD")
        self.lr_paD.setFont(font1)
        self.lr_paD.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lr_paD, 4, 1, 1, 2)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 5)

        self.le_paP = QLineEdit(self.centralwidget)
        self.le_paP.setObjectName(u"le_paP")
        self.le_paP.setFont(font1)

        self.gridLayout_2.addWidget(self.le_paP, 3, 3, 1, 2)

        self.lr_pwm = QLineEdit(self.centralwidget)
        self.lr_pwm.setObjectName(u"lr_pwm")
        self.lr_pwm.setFont(font1)
        self.lr_pwm.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lr_pwm, 2, 1, 1, 2)

        self.pb_readMem = QPushButton(self.centralwidget)
        self.pb_readMem.setObjectName(u"pb_readMem")

        self.gridLayout_2.addWidget(self.pb_readMem, 7, 2, 1, 1)

        self.le_pwm = QLineEdit(self.centralwidget)
        self.le_pwm.setObjectName(u"le_pwm")
        self.le_pwm.setFont(font1)

        self.gridLayout_2.addWidget(self.le_pwm, 2, 3, 1, 2)

        self.lr_paP = QLineEdit(self.centralwidget)
        self.lr_paP.setObjectName(u"lr_paP")
        self.lr_paP.setFont(font1)
        self.lr_paP.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lr_paP, 3, 1, 1, 2)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_9, 1, 3, 1, 2)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout_2.addWidget(self.label_12, 6, 0, 1, 1)

        self.lr_speed = QLineEdit(self.centralwidget)
        self.lr_speed.setObjectName(u"lr_speed")
        self.lr_speed.setFont(font1)
        self.lr_speed.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lr_speed, 6, 1, 1, 2)

        self.le_speed = QLineEdit(self.centralwidget)
        self.le_speed.setObjectName(u"le_speed")
        self.le_speed.setFont(font1)

        self.gridLayout_2.addWidget(self.le_speed, 6, 3, 1, 2)

        self.gridLayout_2.setColumnStretch(0, 50)
        self.gridLayout_2.setColumnStretch(1, 50)
        self.gridLayout_2.setColumnStretch(2, 50)
        self.gridLayout_2.setColumnStretch(3, 50)
        self.gridLayout_2.setColumnStretch(4, 50)

        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 1, 1, 1)

        self.gridLayout_3.setRowStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 828, 33))
        self.menuCalls = QMenu(self.menubar)
        self.menuCalls.setObjectName(u"menuCalls")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuCalls.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menuCalls.addAction(self.actionConnect)
        self.menuCalls.addAction(self.actionDisconnect)
        self.menuTools.addAction(self.actionConfigure)
        self.toolBar.addAction(self.actionConnect)
        self.toolBar.addAction(self.actionDisconnect)
        self.toolBar.addAction(self.actionClear)
        self.toolBar.addAction(self.actionPause)
        self.toolBar.addAction(self.actionStop)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionConnect.setText(QCoreApplication.translate("MainWindow", u"Conncect", None))
        self.actionDisconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionConfigure.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionClear.setText(QCoreApplication.translate("MainWindow", u"clear", None))
#if QT_CONFIG(tooltip)
        self.actionClear.setToolTip(QCoreApplication.translate("MainWindow", u"Clear plot ", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionClear.setShortcut(QCoreApplication.translate("MainWindow", u"C", None))
#endif // QT_CONFIG(shortcut)
        self.actionPause.setText(QCoreApplication.translate("MainWindow", u"pause", None))
#if QT_CONFIG(tooltip)
        self.actionPause.setToolTip(QCoreApplication.translate("MainWindow", u"Pause plotting", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionPause.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.actionStop.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
#if QT_CONFIG(tooltip)
        self.actionStop.setToolTip(QCoreApplication.translate("MainWindow", u"Disable of drivers", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionStop.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Plot 2", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Plot 1", None))
        self.radioButton_5.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Plot 4", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Plot 3", None))
        self.radioButton_2.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Plot 5", None))
        self.radioButton_3.setText("")
        self.radioButton.setText("")
        self.radioButton_4.setText("")
        self.pb_clrPlot_1.setText("")
        self.pb_clrPlot_2.setText("")
        self.pb_clrPlot_3.setText("")
        self.pb_clrPlot_4.setText("")
        self.pb_clrPlot_5.setText("")
        self.pb_setPos1.setText(QCoreApplication.translate("MainWindow", u"SetPos 1", None))
        self.pb_send.setText(QCoreApplication.translate("MainWindow", u"SEND", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enable:", None))
        self.cb_mode.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Set Pos:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Mode:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CONTROL", None))
        self.cb_enable.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Degrees:", None))
        self.pb_setPos3.setText(QCoreApplication.translate("MainWindow", u"SetPos 3", None))
        self.l_pps.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pb_setPos2.setText(QCoreApplication.translate("MainWindow", u"SetPos 2", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Angle:", None))
        self.cb_degrees.setText("")
        self.pb_gen.setText(QCoreApplication.translate("MainWindow", u"GEN", None))
        self.sb_genFreq.setSuffix(QCoreApplication.translate("MainWindow", u" Hz", None))
        self.sb_genAmpl.setSuffix(QCoreApplication.translate("MainWindow", u" \u00b0", None))
        self.pb_saveConf.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PWM", None))
        self.pb_updateConf.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Read", None))
        self.pb_readConf.setText(QCoreApplication.translate("MainWindow", u"READ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PA P", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"CONFIG", None))
        self.pb_readMem.setText(QCoreApplication.translate("MainWindow", u"READ mem", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"PA D", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Zero Shift", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.menuCalls.setTitle(QCoreApplication.translate("MainWindow", u"Calls", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

