# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowVeuHFi.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QStatusBar, QToolBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1699, 812)
        MainWindow.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
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
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pb_mReadMem = QPushButton(self.frame)
        self.bg_readM = QButtonGroup(MainWindow)
        self.bg_readM.setObjectName(u"bg_readM")
        self.bg_readM.addButton(self.pb_mReadMem)
        self.pb_mReadMem.setObjectName(u"pb_mReadMem")

        self.gridLayout_2.addWidget(self.pb_mReadMem, 9, 2, 1, 1)

        self.pb_mSaveConf = QPushButton(self.frame)
        self.bg_save = QButtonGroup(MainWindow)
        self.bg_save.setObjectName(u"bg_save")
        self.bg_save.addButton(self.pb_mSaveConf)
        self.pb_mSaveConf.setObjectName(u"pb_mSaveConf")

        self.gridLayout_2.addWidget(self.pb_mSaveConf, 9, 4, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)

        self.le_phStep = QLineEdit(self.frame)
        self.le_phStep.setObjectName(u"le_phStep")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.le_phStep.setFont(font1)

        self.gridLayout_2.addWidget(self.le_phStep, 6, 3, 1, 2)

        self.le_Q = QLineEdit(self.frame)
        self.le_Q.setObjectName(u"le_Q")
        self.le_Q.setFont(font1)

        self.gridLayout_2.addWidget(self.le_Q, 3, 3, 1, 2)

        self.lr_D = QLineEdit(self.frame)
        self.lr_D.setObjectName(u"lr_D")
        self.lr_D.setFont(font1)
        self.lr_D.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lr_D, 4, 1, 1, 2)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_9, 1, 3, 1, 2)

        self.le_elZeroShift = QLineEdit(self.frame)
        self.le_elZeroShift.setObjectName(u"le_elZeroShift")
        self.le_elZeroShift.setFont(font1)

        self.gridLayout_2.addWidget(self.le_elZeroShift, 5, 3, 1, 2)

        self.lr_elZeroShift = QLineEdit(self.frame)
        self.lr_elZeroShift.setObjectName(u"lr_elZeroShift")
        self.lr_elZeroShift.setFont(font1)
        self.lr_elZeroShift.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lr_elZeroShift, 5, 1, 1, 2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.gridLayout_2.addWidget(self.label_15, 7, 0, 1, 1)

        self.lr_phStep = QLineEdit(self.frame)
        self.lr_phStep.setObjectName(u"lr_phStep")
        self.lr_phStep.setFont(font1)
        self.lr_phStep.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lr_phStep, 6, 1, 1, 2)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout_2.addWidget(self.label_12, 6, 0, 1, 1)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setKerning(True)
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 5)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 1, 1, 1, 2)

        self.le_D = QLineEdit(self.frame)
        self.le_D.setObjectName(u"le_D")
        self.le_D.setFont(font1)

        self.gridLayout_2.addWidget(self.le_D, 4, 3, 1, 2)

        self.lr_mtMode = QLineEdit(self.frame)
        self.lr_mtMode.setObjectName(u"lr_mtMode")
        self.lr_mtMode.setFont(font1)
        self.lr_mtMode.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lr_mtMode, 8, 1, 1, 2)

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.gridLayout_2.addWidget(self.label_16, 8, 0, 1, 1)

        self.le_phAcc = QLineEdit(self.frame)
        self.le_phAcc.setObjectName(u"le_phAcc")
        self.le_phAcc.setFont(font1)

        self.gridLayout_2.addWidget(self.le_phAcc, 7, 3, 1, 2)

        self.pb_mUpdateConf = QPushButton(self.frame)
        self.bg_update = QButtonGroup(MainWindow)
        self.bg_update.setObjectName(u"bg_update")
        self.bg_update.addButton(self.pb_mUpdateConf)
        self.pb_mUpdateConf.setObjectName(u"pb_mUpdateConf")

        self.gridLayout_2.addWidget(self.pb_mUpdateConf, 9, 3, 1, 1)

        self.lr_Q = QLineEdit(self.frame)
        self.lr_Q.setObjectName(u"lr_Q")
        self.lr_Q.setFont(font1)
        self.lr_Q.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lr_Q, 3, 1, 1, 2)

        self.pb_mReadConf = QPushButton(self.frame)
        self.bg_read = QButtonGroup(MainWindow)
        self.bg_read.setObjectName(u"bg_read")
        self.bg_read.addButton(self.pb_mReadConf)
        self.pb_mReadConf.setObjectName(u"pb_mReadConf")

        self.gridLayout_2.addWidget(self.pb_mReadConf, 9, 1, 1, 1)

        self.le_pwm = QLineEdit(self.frame)
        self.le_pwm.setObjectName(u"le_pwm")
        self.le_pwm.setFont(font1)
        self.le_pwm.setInputMethodHints(Qt.InputMethodHint.ImhNone)

        self.gridLayout_2.addWidget(self.le_pwm, 2, 3, 1, 2)

        self.lr_pwm = QLineEdit(self.frame)
        self.lr_pwm.setObjectName(u"lr_pwm")
        self.lr_pwm.setFont(font1)
        self.lr_pwm.setFrame(True)
        self.lr_pwm.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lr_pwm, 2, 1, 1, 2)

        self.lr_phAcc = QLineEdit(self.frame)
        self.lr_phAcc.setObjectName(u"lr_phAcc")
        self.lr_phAcc.setFont(font1)
        self.lr_phAcc.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lr_phAcc, 7, 1, 1, 2)

        self.cb_ampSelect = QComboBox(self.frame)
        self.cb_ampSelect.addItem("")
        self.cb_ampSelect.addItem("")
        self.cb_ampSelect.addItem("")
        self.cb_ampSelect.addItem("")
        self.cb_ampSelect.addItem("")
        self.cb_ampSelect.setObjectName(u"cb_ampSelect")

        self.gridLayout_2.addWidget(self.cb_ampSelect, 1, 0, 1, 1)

        self.cb_mtMode = QComboBox(self.frame)
        self.cb_mtMode.addItem("")
        self.cb_mtMode.addItem("")
        self.cb_mtMode.addItem("")
        self.cb_mtMode.setObjectName(u"cb_mtMode")

        self.gridLayout_2.addWidget(self.cb_mtMode, 8, 3, 1, 2)


        self.horizontalLayout_2.addLayout(self.gridLayout_2)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pb_pidUpdateConf = QPushButton(self.frame)
        self.bg_update.addButton(self.pb_pidUpdateConf)
        self.pb_pidUpdateConf.setObjectName(u"pb_pidUpdateConf")

        self.gridLayout_6.addWidget(self.pb_pidUpdateConf, 9, 3, 1, 1)

        self.lr_res = QLineEdit(self.frame)
        self.lr_res.setObjectName(u"lr_res")
        self.lr_res.setFont(font1)
        self.lr_res.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lr_res, 8, 1, 1, 2)

        self.le_spP = QLineEdit(self.frame)
        self.le_spP.setObjectName(u"le_spP")
        self.le_spP.setFont(font1)

        self.gridLayout_6.addWidget(self.le_spP, 5, 3, 1, 2)

        self.lr_spP = QLineEdit(self.frame)
        self.lr_spP.setObjectName(u"lr_spP")
        self.lr_spP.setFont(font1)
        self.lr_spP.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lr_spP, 5, 1, 1, 2)

        self.le_posD = QLineEdit(self.frame)
        self.le_posD.setObjectName(u"le_posD")
        self.le_posD.setFont(font1)

        self.gridLayout_6.addWidget(self.le_posD, 3, 3, 1, 2)

        self.pb_pidSaveConf = QPushButton(self.frame)
        self.bg_save.addButton(self.pb_pidSaveConf)
        self.pb_pidSaveConf.setObjectName(u"pb_pidSaveConf")

        self.gridLayout_6.addWidget(self.pb_pidSaveConf, 9, 4, 1, 1)

        self.pb_pidReadMem = QPushButton(self.frame)
        self.bg_readM.addButton(self.pb_pidReadMem)
        self.pb_pidReadMem.setObjectName(u"pb_pidReadMem")

        self.gridLayout_6.addWidget(self.pb_pidReadMem, 9, 2, 1, 1)

        self.label_27 = QLabel(self.frame)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font)

        self.gridLayout_6.addWidget(self.label_27, 3, 0, 1, 1)

        self.label_34 = QLabel(self.frame)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font2)
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_34, 0, 0, 1, 5)

        self.label_28 = QLabel(self.frame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font)

        self.gridLayout_6.addWidget(self.label_28, 5, 0, 1, 1)

        self.label_35 = QLabel(self.frame)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font)
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_35, 1, 1, 1, 2)

        self.label_32 = QLabel(self.frame)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font)

        self.gridLayout_6.addWidget(self.label_32, 7, 0, 1, 1)

        self.label_33 = QLabel(self.frame)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font)

        self.gridLayout_6.addWidget(self.label_33, 6, 0, 1, 1)

        self.lr_spSat = QLineEdit(self.frame)
        self.lr_spSat.setObjectName(u"lr_spSat")
        self.lr_spSat.setFont(font1)
        self.lr_spSat.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lr_spSat, 7, 1, 1, 2)

        self.label_29 = QLabel(self.frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font)

        self.gridLayout_6.addWidget(self.label_29, 4, 0, 1, 1)

        self.label_30 = QLabel(self.frame)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font)
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_30, 1, 3, 1, 2)

        self.lr_posP = QLineEdit(self.frame)
        self.lr_posP.setObjectName(u"lr_posP")
        self.lr_posP.setFont(font1)
        self.lr_posP.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lr_posP, 2, 1, 1, 2)

        self.pb_pidReadConf = QPushButton(self.frame)
        self.bg_read.addButton(self.pb_pidReadConf)
        self.pb_pidReadConf.setObjectName(u"pb_pidReadConf")

        self.gridLayout_6.addWidget(self.pb_pidReadConf, 9, 1, 1, 1)

        self.le_posSat = QLineEdit(self.frame)
        self.le_posSat.setObjectName(u"le_posSat")
        self.le_posSat.setFont(font1)

        self.gridLayout_6.addWidget(self.le_posSat, 4, 3, 1, 2)

        self.lr_spI = QLineEdit(self.frame)
        self.lr_spI.setObjectName(u"lr_spI")
        self.lr_spI.setFont(font1)
        self.lr_spI.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lr_spI, 6, 1, 1, 2)

        self.label_36 = QLabel(self.frame)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font)

        self.gridLayout_6.addWidget(self.label_36, 8, 0, 1, 1)

        self.label_31 = QLabel(self.frame)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font)

        self.gridLayout_6.addWidget(self.label_31, 2, 0, 1, 1)

        self.lr_posSat = QLineEdit(self.frame)
        self.lr_posSat.setObjectName(u"lr_posSat")
        self.lr_posSat.setFont(font1)
        self.lr_posSat.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lr_posSat, 4, 1, 1, 2)

        self.lr_posD = QLineEdit(self.frame)
        self.lr_posD.setObjectName(u"lr_posD")
        self.lr_posD.setFont(font1)
        self.lr_posD.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lr_posD, 3, 1, 1, 2)

        self.le_spSat = QLineEdit(self.frame)
        self.le_spSat.setObjectName(u"le_spSat")
        self.le_spSat.setFont(font1)

        self.gridLayout_6.addWidget(self.le_spSat, 7, 3, 1, 2)

        self.le_posP = QLineEdit(self.frame)
        self.le_posP.setObjectName(u"le_posP")
        self.le_posP.setFont(font1)

        self.gridLayout_6.addWidget(self.le_posP, 2, 3, 1, 2)

        self.le_spI = QLineEdit(self.frame)
        self.le_spI.setObjectName(u"le_spI")
        self.le_spI.setFont(font1)

        self.gridLayout_6.addWidget(self.le_spI, 6, 3, 1, 2)

        self.le_res = QLineEdit(self.frame)
        self.le_res.setObjectName(u"le_res")
        self.le_res.setFont(font1)

        self.gridLayout_6.addWidget(self.le_res, 8, 3, 1, 2)

        self.gridLayout_6.setColumnStretch(0, 50)

        self.horizontalLayout_2.addLayout(self.gridLayout_6)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pb_genReadMem = QPushButton(self.frame)
        self.bg_readM.addButton(self.pb_genReadMem)
        self.pb_genReadMem.setObjectName(u"pb_genReadMem")

        self.gridLayout_7.addWidget(self.pb_genReadMem, 9, 2, 1, 1)

        self.pb_genSaveConf = QPushButton(self.frame)
        self.bg_save.addButton(self.pb_genSaveConf)
        self.pb_genSaveConf.setObjectName(u"pb_genSaveConf")

        self.gridLayout_7.addWidget(self.pb_genSaveConf, 9, 4, 1, 1)

        self.label_37 = QLabel(self.frame)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font)

        self.gridLayout_7.addWidget(self.label_37, 3, 0, 1, 1)

        self.label_38 = QLabel(self.frame)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font)

        self.gridLayout_7.addWidget(self.label_38, 5, 0, 1, 1)

        self.le_res_4 = QLineEdit(self.frame)
        self.le_res_4.setObjectName(u"le_res_4")
        self.le_res_4.setFont(font1)

        self.gridLayout_7.addWidget(self.le_res_4, 6, 3, 1, 2)

        self.le_range = QLineEdit(self.frame)
        self.le_range.setObjectName(u"le_range")
        self.le_range.setFont(font1)

        self.gridLayout_7.addWidget(self.le_range, 3, 3, 1, 2)

        self.lr_res_2 = QLineEdit(self.frame)
        self.lr_res_2.setObjectName(u"lr_res_2")
        self.lr_res_2.setFont(font1)
        self.lr_res_2.setReadOnly(True)

        self.gridLayout_7.addWidget(self.lr_res_2, 4, 1, 1, 2)

        self.label_39 = QLabel(self.frame)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font)

        self.gridLayout_7.addWidget(self.label_39, 4, 0, 1, 1)

        self.label_40 = QLabel(self.frame)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font)
        self.label_40.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.label_40, 1, 3, 1, 2)

        self.le_res_3 = QLineEdit(self.frame)
        self.le_res_3.setObjectName(u"le_res_3")
        self.le_res_3.setFont(font1)

        self.gridLayout_7.addWidget(self.le_res_3, 5, 3, 1, 2)

        self.le_res_6 = QLineEdit(self.frame)
        self.le_res_6.setObjectName(u"le_res_6")
        self.le_res_6.setFont(font1)

        self.gridLayout_7.addWidget(self.le_res_6, 8, 3, 1, 2)

        self.lr_res_3 = QLineEdit(self.frame)
        self.lr_res_3.setObjectName(u"lr_res_3")
        self.lr_res_3.setFont(font1)
        self.lr_res_3.setReadOnly(True)

        self.gridLayout_7.addWidget(self.lr_res_3, 5, 1, 1, 2)

        self.label_41 = QLabel(self.frame)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font)

        self.gridLayout_7.addWidget(self.label_41, 2, 0, 1, 1)

        self.label_42 = QLabel(self.frame)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font)

        self.gridLayout_7.addWidget(self.label_42, 7, 0, 1, 1)

        self.lr_res_4 = QLineEdit(self.frame)
        self.lr_res_4.setObjectName(u"lr_res_4")
        self.lr_res_4.setFont(font1)
        self.lr_res_4.setReadOnly(True)

        self.gridLayout_7.addWidget(self.lr_res_4, 6, 1, 1, 2)

        self.label_43 = QLabel(self.frame)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font)

        self.gridLayout_7.addWidget(self.label_43, 6, 0, 1, 1)

        self.label_44 = QLabel(self.frame)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font2)
        self.label_44.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.label_44, 0, 0, 1, 5)

        self.label_45 = QLabel(self.frame)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font)
        self.label_45.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.label_45, 1, 1, 1, 2)

        self.le_res_2 = QLineEdit(self.frame)
        self.le_res_2.setObjectName(u"le_res_2")
        self.le_res_2.setFont(font1)

        self.gridLayout_7.addWidget(self.le_res_2, 4, 3, 1, 2)

        self.lr_res_6 = QLineEdit(self.frame)
        self.lr_res_6.setObjectName(u"lr_res_6")
        self.lr_res_6.setFont(font1)
        self.lr_res_6.setReadOnly(True)

        self.gridLayout_7.addWidget(self.lr_res_6, 8, 1, 1, 2)

        self.label_46 = QLabel(self.frame)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font)

        self.gridLayout_7.addWidget(self.label_46, 8, 0, 1, 1)

        self.le_res_5 = QLineEdit(self.frame)
        self.le_res_5.setObjectName(u"le_res_5")
        self.le_res_5.setFont(font1)

        self.gridLayout_7.addWidget(self.le_res_5, 7, 3, 1, 2)

        self.pb_genUpdateConf = QPushButton(self.frame)
        self.bg_update.addButton(self.pb_genUpdateConf)
        self.pb_genUpdateConf.setObjectName(u"pb_genUpdateConf")

        self.gridLayout_7.addWidget(self.pb_genUpdateConf, 9, 3, 1, 1)

        self.lr_range = QLineEdit(self.frame)
        self.lr_range.setObjectName(u"lr_range")
        self.lr_range.setFont(font1)
        self.lr_range.setReadOnly(True)

        self.gridLayout_7.addWidget(self.lr_range, 3, 1, 1, 2)

        self.pb_genReadConf = QPushButton(self.frame)
        self.bg_read.addButton(self.pb_genReadConf)
        self.pb_genReadConf.setObjectName(u"pb_genReadConf")

        self.gridLayout_7.addWidget(self.pb_genReadConf, 9, 1, 1, 1)

        self.le_zeroShift = QLineEdit(self.frame)
        self.le_zeroShift.setObjectName(u"le_zeroShift")
        self.le_zeroShift.setFont(font1)

        self.gridLayout_7.addWidget(self.le_zeroShift, 2, 3, 1, 2)

        self.lr_zeroShift = QLineEdit(self.frame)
        self.lr_zeroShift.setObjectName(u"lr_zeroShift")
        self.lr_zeroShift.setFont(font1)
        self.lr_zeroShift.setReadOnly(True)

        self.gridLayout_7.addWidget(self.lr_zeroShift, 2, 1, 1, 2)

        self.lr_res_5 = QLineEdit(self.frame)
        self.lr_res_5.setObjectName(u"lr_res_5")
        self.lr_res_5.setFont(font1)
        self.lr_res_5.setReadOnly(True)

        self.gridLayout_7.addWidget(self.lr_res_5, 7, 1, 1, 2)

        self.gridLayout_7.setColumnStretch(0, 50)

        self.horizontalLayout_2.addLayout(self.gridLayout_7)


        self.gridLayout_3.addWidget(self.frame, 1, 3, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lr_angle = QLineEdit(self.frame_3)
        self.lr_angle.setObjectName(u"lr_angle")
        self.lr_angle.setFont(font1)
        self.lr_angle.setReadOnly(True)

        self.gridLayout.addWidget(self.lr_angle, 0, 1, 1, 1)

        self.sb_genAmpl = QSpinBox(self.frame_3)
        self.sb_genAmpl.setObjectName(u"sb_genAmpl")
        self.sb_genAmpl.setMinimum(1)

        self.gridLayout.addWidget(self.sb_genAmpl, 1, 2, 1, 1)

        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 4)

        self.pb_send = QPushButton(self.frame_3)
        self.bg_send = QButtonGroup(MainWindow)
        self.bg_send.setObjectName(u"bg_send")
        self.bg_send.addButton(self.pb_send)
        self.pb_send.setObjectName(u"pb_send")

        self.gridLayout.addWidget(self.pb_send, 7, 0, 1, 2)

        self.l_pps = QLabel(self.frame_3)
        self.l_pps.setObjectName(u"l_pps")

        self.gridLayout.addWidget(self.l_pps, 7, 3, 1, 1)

        self.pb_gen = QPushButton(self.frame_3)
        self.pb_gen.setObjectName(u"pb_gen")
        self.pb_gen.setCheckable(True)

        self.gridLayout.addWidget(self.pb_gen, 1, 0, 1, 1)

        self.sb_genFreq = QSpinBox(self.frame_3)
        self.sb_genFreq.setObjectName(u"sb_genFreq")
        self.sb_genFreq.setWrapping(False)
        self.sb_genFreq.setMinimum(1)

        self.gridLayout.addWidget(self.sb_genFreq, 1, 1, 1, 1)

        self.cb_degrees = QCheckBox(self.frame_3)
        self.cb_degrees.setObjectName(u"cb_degrees")

        self.gridLayout.addWidget(self.cb_degrees, 0, 3, 1, 1)

        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.gridLayout.addWidget(self.label_14, 0, 2, 1, 1)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.cb_enable = QCheckBox(self.frame_3)
        self.cb_enable.setObjectName(u"cb_enable")

        self.gridLayout.addWidget(self.cb_enable, 3, 1, 1, 1)

        self.pb_setPos1 = QPushButton(self.frame_3)
        self.bg_send.addButton(self.pb_setPos1)
        self.pb_setPos1.setObjectName(u"pb_setPos1")

        self.gridLayout.addWidget(self.pb_setPos1, 3, 2, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.cb_appMode = QComboBox(self.frame_3)
        self.cb_appMode.addItem("")
        self.cb_appMode.addItem("")
        self.cb_appMode.setObjectName(u"cb_appMode")

        self.gridLayout.addWidget(self.cb_appMode, 4, 1, 1, 1)

        self.le_setPos = QLineEdit(self.frame_3)
        self.le_setPos.setObjectName(u"le_setPos")
        self.le_setPos.setFont(font1)

        self.gridLayout.addWidget(self.le_setPos, 5, 1, 1, 1)

        self.pb_setPos2 = QPushButton(self.frame_3)
        self.bg_send.addButton(self.pb_setPos2)
        self.pb_setPos2.setObjectName(u"pb_setPos2")

        self.gridLayout.addWidget(self.pb_setPos2, 4, 2, 1, 1)

        self.pb_setPos3 = QPushButton(self.frame_3)
        self.bg_send.addButton(self.pb_setPos3)
        self.pb_setPos3.setObjectName(u"pb_setPos3")

        self.gridLayout.addWidget(self.pb_setPos3, 5, 2, 1, 1)

        self.le_setPos1 = QLineEdit(self.frame_3)
        self.le_setPos1.setObjectName(u"le_setPos1")
        self.le_setPos1.setFont(font1)

        self.gridLayout.addWidget(self.le_setPos1, 3, 3, 1, 1)

        self.le_setPos2 = QLineEdit(self.frame_3)
        self.le_setPos2.setObjectName(u"le_setPos2")
        self.le_setPos2.setFont(font1)

        self.gridLayout.addWidget(self.le_setPos2, 4, 3, 1, 1)

        self.le_setPos3 = QLineEdit(self.frame_3)
        self.le_setPos3.setObjectName(u"le_setPos3")
        self.le_setPos3.setFont(font1)

        self.gridLayout.addWidget(self.le_setPos3, 5, 3, 1, 1)

        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.gridLayout.addWidget(self.label_17, 6, 0, 1, 1)

        self.cb_arr = QComboBox(self.frame_3)
        self.cb_arr.addItem("")
        self.cb_arr.addItem("")
        self.cb_arr.addItem("")
        self.cb_arr.setObjectName(u"cb_arr")

        self.gridLayout.addWidget(self.cb_arr, 6, 1, 1, 1)

        self.pb_arr = QPushButton(self.frame_3)
        self.pb_arr.setObjectName(u"pb_arr")
        self.pb_arr.setEnabled(True)
        self.pb_arr.setCheckable(False)
        self.pb_arr.setAutoExclusive(False)

        self.gridLayout.addWidget(self.pb_arr, 6, 2, 1, 1)

        self.gridLayout.setColumnMinimumWidth(3, 80)

        self.horizontalLayout_4.addLayout(self.gridLayout)


        self.gridLayout_3.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_5.addWidget(self.lineEdit, 4, 0, 1, 2)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_5.addWidget(self.lineEdit_2, 0, 0, 1, 2)

        self.radioButton_5 = QRadioButton(self.frame_2)
        self.bg_plots = QButtonGroup(MainWindow)
        self.bg_plots.setObjectName(u"bg_plots")
        self.bg_plots.setExclusive(False)
        self.bg_plots.addButton(self.radioButton_5)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setChecked(False)
        self.radioButton_5.setAutoExclusive(False)

        self.gridLayout_5.addWidget(self.radioButton_5, 11, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_5.addWidget(self.lineEdit_4, 8, 0, 1, 2)

        self.lineEdit_3 = QLineEdit(self.frame_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_5.addWidget(self.lineEdit_3, 6, 0, 1, 2)

        self.radioButton_2 = QRadioButton(self.frame_2)
        self.bg_plots.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setAutoExclusive(False)

        self.gridLayout_5.addWidget(self.radioButton_2, 5, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_5.addWidget(self.lineEdit_5, 10, 0, 1, 2)

        self.radioButton_3 = QRadioButton(self.frame_2)
        self.bg_plots.addButton(self.radioButton_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setAutoExclusive(False)

        self.gridLayout_5.addWidget(self.radioButton_3, 7, 0, 1, 1)

        self.radioButton = QRadioButton(self.frame_2)
        self.bg_plots.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)
        self.radioButton.setAutoExclusive(False)

        self.gridLayout_5.addWidget(self.radioButton, 2, 0, 1, 1)

        self.radioButton_4 = QRadioButton(self.frame_2)
        self.bg_plots.addButton(self.radioButton_4)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setAutoExclusive(False)

        self.gridLayout_5.addWidget(self.radioButton_4, 9, 0, 1, 1)

        self.pb_clrPlot_1 = QPushButton(self.frame_2)
        self.bg_clrPlots = QButtonGroup(MainWindow)
        self.bg_clrPlots.setObjectName(u"bg_clrPlots")
        self.bg_clrPlots.setExclusive(False)
        self.bg_clrPlots.addButton(self.pb_clrPlot_1)
        self.pb_clrPlot_1.setObjectName(u"pb_clrPlot_1")
        self.pb_clrPlot_1.setAutoFillBackground(True)

        self.gridLayout_5.addWidget(self.pb_clrPlot_1, 2, 1, 1, 1)

        self.pb_clrPlot_2 = QPushButton(self.frame_2)
        self.bg_clrPlots.addButton(self.pb_clrPlot_2)
        self.pb_clrPlot_2.setObjectName(u"pb_clrPlot_2")

        self.gridLayout_5.addWidget(self.pb_clrPlot_2, 5, 1, 1, 1)

        self.pb_clrPlot_3 = QPushButton(self.frame_2)
        self.bg_clrPlots.addButton(self.pb_clrPlot_3)
        self.pb_clrPlot_3.setObjectName(u"pb_clrPlot_3")

        self.gridLayout_5.addWidget(self.pb_clrPlot_3, 7, 1, 1, 1)

        self.pb_clrPlot_4 = QPushButton(self.frame_2)
        self.bg_clrPlots.addButton(self.pb_clrPlot_4)
        self.pb_clrPlot_4.setObjectName(u"pb_clrPlot_4")

        self.gridLayout_5.addWidget(self.pb_clrPlot_4, 9, 1, 1, 1)

        self.pb_clrPlot_5 = QPushButton(self.frame_2)
        self.bg_clrPlots.addButton(self.pb_clrPlot_5)
        self.pb_clrPlot_5.setObjectName(u"pb_clrPlot_5")

        self.gridLayout_5.addWidget(self.pb_clrPlot_5, 11, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_5)

        self.vl_plot = QVBoxLayout()
        self.vl_plot.setObjectName(u"vl_plot")

        self.horizontalLayout.addLayout(self.vl_plot)

        self.horizontalLayout.setStretch(1, 1500)

        self.horizontalLayout_3.addLayout(self.horizontalLayout)


        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 4)

        self.gridLayout_3.setRowStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1699, 33))
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
        self.pb_mReadMem.setText(QCoreApplication.translate("MainWindow", u"READ mem", None))
        self.pb_mSaveConf.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"El zero shift", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PWM", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Ph acc", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Ph step", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"CONFIG MOTOR", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Read", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Motor mode", None))
        self.pb_mUpdateConf.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.pb_mReadConf.setText(QCoreApplication.translate("MainWindow", u"READ", None))
        self.cb_ampSelect.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))
        self.cb_ampSelect.setItemText(1, QCoreApplication.translate("MainWindow", u"X1", None))
        self.cb_ampSelect.setItemText(2, QCoreApplication.translate("MainWindow", u"X2", None))
        self.cb_ampSelect.setItemText(3, QCoreApplication.translate("MainWindow", u"Y1", None))
        self.cb_ampSelect.setItemText(4, QCoreApplication.translate("MainWindow", u"Y2", None))

        self.cb_mtMode.setItemText(0, QCoreApplication.translate("MainWindow", u"DRIVER_OPEN", None))
        self.cb_mtMode.setItemText(1, QCoreApplication.translate("MainWindow", u"DRIVER_CLOSE", None))
        self.cb_mtMode.setItemText(2, QCoreApplication.translate("MainWindow", u"DRIVER_FOC", None))

        self.pb_pidUpdateConf.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.pb_pidSaveConf.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.pb_pidReadMem.setText(QCoreApplication.translate("MainWindow", u"READ mem", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"POS D", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"CONFIG PID CONTROL LOOP", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"SP P", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Read", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"SP Sat", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"SP I", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"POS Sat", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.pb_pidReadConf.setText(QCoreApplication.translate("MainWindow", u"READ", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"RESERVE", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"POS P", None))
        self.pb_genReadMem.setText(QCoreApplication.translate("MainWindow", u"READ mem", None))
        self.pb_genSaveConf.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Range", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"RESERVE", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Arr zero shift", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Zero shift", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"RESERVE", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"RESERVE", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"CONFIG GENERAL", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Read", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"AMP ID", None))
        self.pb_genUpdateConf.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.pb_genReadConf.setText(QCoreApplication.translate("MainWindow", u"READ", None))
        self.sb_genAmpl.setSuffix(QCoreApplication.translate("MainWindow", u" \u00b0", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CONTROL", None))
        self.pb_send.setText(QCoreApplication.translate("MainWindow", u"SEND", None))
        self.l_pps.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pb_gen.setText(QCoreApplication.translate("MainWindow", u"GEN", None))
        self.sb_genFreq.setSuffix(QCoreApplication.translate("MainWindow", u" Hz", None))
        self.cb_degrees.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Angle:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Degrees:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enable:", None))
        self.cb_enable.setText("")
        self.pb_setPos1.setText(QCoreApplication.translate("MainWindow", u"SetPos 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"App Mode:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Set Pos:", None))
        self.cb_appMode.setItemText(0, QCoreApplication.translate("MainWindow", u"APP_OPEN", None))
        self.cb_appMode.setItemText(1, QCoreApplication.translate("MainWindow", u"APP_CLOSE", None))

        self.pb_setPos2.setText(QCoreApplication.translate("MainWindow", u"SetPos 2", None))
        self.pb_setPos3.setText(QCoreApplication.translate("MainWindow", u"SetPos 3", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Arr Mode:", None))
        self.cb_arr.setItemText(0, QCoreApplication.translate("MainWindow", u"NONE", None))
        self.cb_arr.setItemText(1, QCoreApplication.translate("MainWindow", u"ARR", None))
        self.cb_arr.setItemText(2, QCoreApplication.translate("MainWindow", u"RARR", None))

        self.pb_arr.setText("")
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
        self.menuCalls.setTitle(QCoreApplication.translate("MainWindow", u"Calls", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

