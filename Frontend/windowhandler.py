import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

import sys

import tools.constants
from Backend import arrayhandler

start_time = 0


def window():
    global start_time
    start_time = time.time()
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0, 40, 600, 80)
    win.setWindowTitle("APM")
    win.setAttribute(PyQt5.QtCore.Qt.WA_TranslucentBackground, True)
    win.setWindowFlags(PyQt5.QtCore.Qt.FramelessWindowHint)
    win.setWindowFlags(Qt.FramelessWindowHint)
    win.setWindowFlag(Qt.WindowStaysOnTopHint, True)
    label = QtWidgets.QLabel('White', win)
    label.setFixedWidth(600)
    label.setFixedHeight(80)
    label.setFont(QFont('Arial', 12))
    label.setStyleSheet('color: White')
    labelSetText(label, tools.constants.PLEB)
    win.show()

    def update_apm():
        if get_length_array_apm_frontend() > 300:
            labelSetText(label, tools.constants.LOVE)
        elif get_length_array_apm_frontend() > 200:
            labelSetText(label, tools.constants.MICROGOD)
        elif get_length_array_apm_frontend() > 100:
            labelSetText(label, tools.constants.MICRO)
        elif get_length_array_apm_frontend() > 50:
            labelSetText(label, tools.constants.START_TO_MICRO)
        elif get_length_array_apm_frontend() > 20:
            labelSetText(label, tools.constants.BEGINNER)
        elif get_length_array_apm_frontend() > 0:
            labelSetText(label, tools.constants.NOOB)
        else:
            labelSetText(label, tools.constants.PLEB)
    timer = QTimer()
    timer.setInterval(1000)
    timer.timeout.connect(update_apm)
    timer.start()
    app.exec_()


def labelSetText(label, text):
    label.setText(tools.constants.CURRENT_APM + str(get_length_array_apm_frontend()) + " " + text + "\n" +
                  tools.constants.MAX_APM + str(arrayhandler.max_apm) + "\n" +
                  tools.constants.TOTAL_ACTIONS + str(get_total_actions_from_backend()))


def get_length_array_apm_frontend():
    return arrayhandler.get_length_array_apm_backend()


def get_total_actions_from_backend():
    return arrayhandler.get_total_actions()


def start_window():
    window()
