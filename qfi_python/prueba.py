#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we create a simple
window in PyQt5.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from PyQt5 import QtGui,QtCore,QtSvg

from threadGUI import ThreadGUI
from qfi import qfi_ADI


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.w = qfi_ADI.qfi_ADI(self)
        print (self.w.width())
        self.w.resize(240, 240)
        self.w.reinit()

        self.layout = QGridLayout()
        self.layout.addWidget(self.w, 0, 0)
        self.setLayout(self.layout)

        self.show()

    def update(self, val):
        self.w.setRoll(val)
        self.w.setPitch(val)
        self.w.viewUpdate.emit()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()

    t2 = ThreadGUI(win)
    t2.daemon = True
    t2.start()

    sys.exit(app.exec_())
