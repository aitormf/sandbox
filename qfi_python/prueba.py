#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from PyQt5 import QtGui,QtCore,QtSvg

from threadGUI import ThreadGUI
from qfi import qfi_ADI, qfi_ALT, qfi_SI, qfi_HSI, qfi_VSI, qfi_TC
import math


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.layout = QGridLayout()

        self.w = qfi_ADI.qfi_ADI(self)
        self.w.resize(240, 240)
        self.w.reinit()
        self.layout.addWidget(self.w, 0, 0)

        self.y = qfi_ALT.qfi_ALT(self)
        self.y.resize(240, 240)
        self.y.reinit()
        self.layout.addWidget(self.y, 0, 1)

        self.hsi = qfi_HSI.qfi_HSI(self)
        self.hsi.resize(240, 240)
        self.hsi.reinit()
        self.layout.addWidget(self.hsi, 1, 0)

        self.asi = qfi_SI.qfi_SI(self)
        self.asi.resize(240, 240)
        self.asi.reinit()
        self.layout.addWidget(self.asi, 1, 1)

        self.vsi = qfi_VSI.qfi_VSI(self)
        self.vsi.resize(240, 240)
        self.vsi.reinit()
        self.layout.addWidget(self.vsi, 2, 0)

        self.tc = qfi_TC.qfi_TC(self)
        self.tc.resize(240, 240)
        self.tc.reinit()
        self.layout.addWidget(self.tc, 2, 1)


        self.setLayout(self.layout)

        self.show()

    def update(self, val):
        self.w.setRoll(10*math.cos(val))
        self.w.setPitch(10*math.cos(val))
        self.asi.setSpeed(val)
        self.hsi.setHeading(val)
        self.vsi.setClimbRate(val)
        self.y.setAltitude(val)
        self.tc.setTurnRate(10*math.cos(val))
        self.tc.setSlipSkid(10*math.cos(val))
        self.w.viewUpdate.emit()
        self.y.viewUpdate.emit()
        self.asi.viewUpdate.emit()
        self.hsi.viewUpdate.emit()
        self.vsi.viewUpdate.emit()
        self.tc.viewUpdate.emit()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()

    t2 = ThreadGUI(win)
    t2.daemon = True
    t2.start()

    sys.exit(app.exec_())
