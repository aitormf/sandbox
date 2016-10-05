#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtGui,QtCore,QtSvg
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItem
import math

from qfi import qfi_rc

class qfi_ALT (QGraphicsView):

    viewUpdate = QtCore.pyqtSignal()

    def __init__(self,winParent):
        QGraphicsView.__init__(self)

        self.winParent=winParent

        self.viewUpdate.connect(self.updateView)
        
        self.m_altitude = 0
        self.m_pressure = 28

        self.m_originalHeight = 240
        self.m_originalWidth = 240

        self.m_originalAltCtr = QtCore.QPointF(120,120)

        self.m_face1Z = -50
        self.m_face2Z = -40
        self.m_face3Z = -30
        self.m_hand1Z = -20
        self.m_hand2Z = -10
        self.m_caseZ = 10


        self.m_scene = QGraphicsScene(self)
        self.setScene(self.m_scene)

        self.init()

        

    def init (self):
        self.m_scaleX = self.width() / self.m_originalWidth
        self.m_scaleY = self.height() / self.m_originalHeight


        self.m_itemFace_1 = QtSvg.QGraphicsSvgItem(":/qfi/images/alt/alt_face_1.svg")
        self.m_itemFace_1.setCacheMode (QGraphicsItem.NoCache)
        self.m_itemFace_1.setZValue( self.m_face1Z )
        self.m_itemFace_1.setTransform( QtGui.QTransform.fromScale( self.m_scaleX, self.m_scaleY ), True )
        self.m_itemFace_1.setTransformOriginPoint( self.m_originalAltCtr )
        self.m_scene.addItem (self.m_itemFace_1)

        self.m_itemFace_2 = QtSvg.QGraphicsSvgItem(":/qfi/images/alt/alt_face_2.svg")
        self.m_itemFace_2.setCacheMode (QGraphicsItem.NoCache)
        self.m_itemFace_2.setZValue( self.m_face2Z )
        self.m_itemFace_2.setTransform( QtGui.QTransform.fromScale( self.m_scaleX, self.m_scaleY ), True )
        self.m_itemFace_2.setTransformOriginPoint( self.m_originalAltCtr )
        self.m_scene.addItem (self.m_itemFace_2)

        self.m_itemFace_3 = QtSvg.QGraphicsSvgItem(":/qfi/images/alt/alt_face_3.svg")
        self.m_itemFace_3.setCacheMode (QGraphicsItem.NoCache)
        self.m_itemFace_3.setZValue( self.m_face3Z )
        self.m_itemFace_3.setTransform( QtGui.QTransform.fromScale( self.m_scaleX, self.m_scaleY ), True )
        self.m_itemFace_3.setTransformOriginPoint( self.m_originalAltCtr )
        self.m_scene.addItem (self.m_itemFace_3)

        self.m_itemHand_1 = QtSvg.QGraphicsSvgItem(":/qfi/images/alt/alt_hand_1.svg")
        self.m_itemHand_1.setCacheMode (QGraphicsItem.NoCache)
        self.m_itemHand_1.setZValue( self.m_hand1Z )
        self.m_itemHand_1.setTransform( QtGui.QTransform.fromScale( self.m_scaleX, self.m_scaleY ), True )
        self.m_itemHand_1.setTransformOriginPoint( self.m_originalAltCtr )
        self.m_scene.addItem (self.m_itemHand_1)

        self.m_itemHand_2 = QtSvg.QGraphicsSvgItem(":/qfi/images/alt/alt_hand_2.svg")
        self.m_itemHand_2.setCacheMode (QGraphicsItem.NoCache)
        self.m_itemHand_2.setZValue( self.m_hand2Z )
        self.m_itemHand_2.setTransform( QtGui.QTransform.fromScale( self.m_scaleX, self.m_scaleY ), True )
        self.m_itemHand_2.setTransformOriginPoint( self.m_originalAltCtr )
        self.m_scene.addItem (self.m_itemHand_2)

        self.m_itemCase = QtSvg.QGraphicsSvgItem(":/qfi/images/alt/alt_case.svg")
        self.m_itemCase.setCacheMode (QGraphicsItem.NoCache)
        self.m_itemCase.setZValue( self.m_caseZ )
        self.m_itemCase.setTransform( QtGui.QTransform.fromScale( self.m_scaleX, self.m_scaleY ), True )
        self.m_itemCase.setTransformOriginPoint( self.m_originalAltCtr )
        self.m_scene.addItem (self.m_itemCase)

        self.centerOn (self.width()/2, self.height()/2)

        self.updateView()

    def reinit(self):
        if (self.m_scene):
            self.m_scene.clear()
            self.init()

    def update(self):
        self.updateView()

    def setAltitude (self, altitude):
        self.m_altitude = altitude

    def setPressure (self, pressure):
        self.m_pressure = pressure
        if (self.m_pressure < 28):
            self.m_pressure = 28
        if (self.m_pressure > 31.5):
            self.m_pressure = 31.5

    def resizeEvent (self, event):
        QGraphicsView.resizeEvent (self,event)
        self.reinit()

    def reset (self):
        self.m_itemFace_1 = None
        self.m_itemFace_2 = None
        self.m_itemFace_3 = None
        self.m_itemHand_1 = None
        self.m_itemHand_2 = None
        self.m_itemCase   = None

        self.m_altitude =  0.0
        self.m_pressure = 28.0


    def updateView(self):
        altitude = math.ceil(self.m_altitude + 0.5)
        angleH1 = self.m_altitude * 0.036
        angleH2 = ( altitude % 1000 ) * 0.36
        angleF1 = (self.m_pressure - 28.0 ) * 100.0
        angleF3 = self.m_altitude * 0.0036

        self.m_itemHand_1.setRotation(angleH1)
        self.m_itemHand_2.setRotation(angleH2)
        self.m_itemFace_1.setRotation(- angleF1)
        self.m_itemFace_3.setRotation(angleF3)

        self.m_scene.update()


