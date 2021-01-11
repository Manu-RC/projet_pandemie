import math
import sys
import simulation
import random as rd
from PyQt5 import QtWidgets, QtGui, QtCore


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
        self.add_shortcut('f', lambda: self.playpause())
        
    


    def add_shortcut(self,text, slot):
        """creates an application-wide key binding"""
        shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(text), self)
        shortcut.activated.connect(slot)

