import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

from Backend import arrayhandler


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0, 0, 170, 30)
    win.setWindowTitle("APM")
    win.setAttribute(PyQt5.QtCore.Qt.WA_TranslucentBackground, True)
    win.setWindowFlags(PyQt5.QtCore.Qt.FramelessWindowHint)
    win.setWindowFlags(Qt.FramelessWindowHint)
    win.setWindowFlag(Qt.WindowStaysOnTopHint, True)
    label = QtWidgets.QLabel('White', win)
    label.setFixedWidth(170)
    label.setFont(QFont('Arial', 12))
    label.setStyleSheet('color: White')
    label.setText("Current apm: " + str(get_length_array_apm_frontend()))
    win.show()

    def update_apm():
        label.setText("Current apm: " + str(get_length_array_apm_frontend()))

    timer = QTimer()
    timer.setInterval(1000)
    timer.timeout.connect(update_apm)
    timer.start()

    app.exec_()


def get_length_array_apm_frontend():
    return arrayhandler.get_length_array_apm_backend()


def start_window():
    window()
