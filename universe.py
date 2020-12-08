import math
import sys
import simulation
import random as rd
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPen, QBrush, QColor

class Universe(QtWidgets.QWidget) :

    def __init__(self,simu):

        super().__init__()
        self.simu = simu
        self.length = simu.x_max
        self.height = simu.y_max
        self.setWindowTitle("test")
        # self.resize(l,h)
        self.scene = QtWidgets.QGraphicsScene()
        self.items = QtWidgets.QGraphicsItemGroup()
        self.scene.addItem(self.items)
        self.timer = QtCore.QTimer(self)

        self.timer.timeout.connect(self.update_people)
        self.update_people()

        self.timer.timeout.connect(self.simu.advance())

        # self.add_rd_people()
        self.add_shortcut('f', lambda: self.playpause())
        

    # def add_rd_people(self):

    #     self.scene.clear()
    #     group = QtWidgets.QGraphicsItemGroup()
    #     self.scene.addItem(group)

    #     for i in range(10):

    #         rd_x = rd.uniform(10,self.length)
    #         rd_y = rd.uniform(10,self.height) 
    #         bounds = QtCore.QRectF(rd_x,rd_y, 10, 10)
    #         item = QtWidgets.QGraphicsEllipseItem(bounds, group )
    #         item.setBrush(QBrush(QColor("red")))

    def update_people(self):  
        """met à jour les emplacements des individus dans la scene"""
        self.simu.advance()
        self.scene.clear()
        group = QtWidgets.QGraphicsItemGroup()
        self.scene.addItem(group)

        for individu in self.simu.population:

            bounds = QtCore.QRectF(individu.x,individu.y,individu.rayon,individu.rayon)
            item = QtWidgets.QGraphicsEllipseItem(bounds, group)
            item.setBrush(QBrush(QColor("red")))  #pourra etre modifié par la suite


    def add_shortcut(self,text, slot):
            """creates an application-wide key binding"""
            shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(text), self)
            shortcut.activated.connect(slot)

    def playpause(self):
        """this slot toggles the replay using the timer as model"""
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(500)


    def start(self):

        if not self.timer.isActive():

            self.timer.start(500)

    def stop(self):

        if self.timer.isActive():

            self.timer.stop