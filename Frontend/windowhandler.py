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
    win.setGeometry(0, 0, 270, 50)
    win.setWindowTitle("APM")
    win.setAttribute(PyQt5.QtCore.Qt.WA_TranslucentBackground, True)
    win.setWindowFlags(PyQt5.QtCore.Qt.FramelessWindowHint)
    win.setWindowFlags(Qt.FramelessWindowHint)
    win.setWindowFlag(Qt.WindowStaysOnTopHint, True)
    label = QtWidgets.QLabel('White', win)
    label.setFixedWidth(270)
    label.setFixedHeight(50)
    label.setFont(QFont('Arial', 12))
    label.setStyleSheet('color: White')
    label.setText("Current apm: Bist du ein Pleb?" + "\n" +
                    "Max apm: " + str(arrayhandler.max_apm) + "\n" +
                    "Total actions: " + str(get_total_actions_from_backend()))
    win.show()

    def update_apm():
        if get_length_array_apm_frontend() > 0:
            label.setText("Current apm: " + str(get_length_array_apm_frontend()) + "\n" +
                            "Max apm: " + str(arrayhandler.max_apm) + "\n" +
                            "Total actions: " + str(get_total_actions_from_backend()))
        else:
            label.setText("Current apm: Bist du ein Pleb?" + "\n" +
                            "Max apm: " + str(arrayhandler.max_apm) + "\n" +
                            "Total actions: " + str(get_total_actions_from_backend()))
    timer = QTimer()
    timer.setInterval(1000)
    timer.timeout.connect(update_apm)
    timer.start()

    app.exec_()


def get_length_array_apm_frontend():
    return arrayhandler.get_length_array_apm_backend()


def get_total_actions_from_backend():
    return arrayhandler.get_total_actions()

def start_window():
    window()
