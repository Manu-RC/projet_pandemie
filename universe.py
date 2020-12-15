import math
import sys
import simulation
import random as rd
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPen, QBrush, QColor

class Universe(QtWidgets.QWidget) :

    def __init__(self,simu,refresh_time):

        super().__init__()
        self.simu = simu
        self.length = simu.x_max
        self.height = simu.y_max
        self.setWindowTitle("test")
        self.scene = QtWidgets.QGraphicsScene()
        self.items = QtWidgets.QGraphicsItemGroup()
        self.scene.addItem(self.items)
        self.timer = QtCore.QTimer(self)
        self.refresh_time = refresh_time
        self.timer.timeout.connect(self.update_people)
        self.set_people()

        # self.timer.timeout.connect(self.simu.advance)

    

        self.add_shortcut('f', lambda: self.playpause())
        
    def set_people(self):

        group = QtWidgets.QGraphicsItemGroup()
        self.scene.addItem(group)

        for individu in self.simu.population:

            bounds = QtCore.QRectF(individu.x,individu.y,individu.rayon*2,individu.rayon*2)
            item = QtWidgets.QGraphicsEllipseItem(bounds, group)
            item.setBrush(QBrush(QColor("red")))
    
    
    def update_people(self):  
        """met à jour les emplacements des individus dans la scene"""
        self.simu.advance()
        self.scene.clear()
        group = QtWidgets.QGraphicsItemGroup()
        self.scene.addItem(group)

        for individu in self.simu.population:

            bounds = QtCore.QRectF(individu.x,individu.y,individu.rayon*2,individu.rayon*2)
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
            self.timer.start(self.refresh_time)


    def start(self):

        if not self.timer.isActive():

            self.timer.start(self.refresh_time)

    def stop(self):

        if self.timer.isActive():

            self.timer.stop()