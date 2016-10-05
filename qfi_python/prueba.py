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

from qfi import qfi_ALT

from qfi import qfi_rc


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.w = qfi_ALT.qfi_ALT(self)
        #self.w.resize(250, 150)

        self.layout = QGridLayout()
        self.layout.addWidget(self.w, 0, 0)

        self.setLayout(self.layout)
        self.show()




if __name__ == '__main__':
    #app = QApplication(sys.argv)
    #win = Window()
    app = QApplication(sys.argv) 
    svgWidget = QtSvg.QSvgWidget(":/qfi/images/alt/alt_face_2.svg")
    svgWidget.setGeometry(50,50,759,668)
    svgWidget.show()

    sys.exit(app.exec_())
