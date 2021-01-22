
from PyQt5 import QtWidgets, QtGui, QtCore


class Universe(QtWidgets.QWidget) :
    """Classe qui sert seulement à créer une scene"""
    def __init__(self,simu,refresh_time):

        super().__init__()
        self.simu = simu
        self.length = simu.x_max
        self.height = simu.y_max
        self.scene = QtWidgets.QGraphicsScene()
        self.timer = QtCore.QTimer(self)
        self.refresh_time = refresh_time

    



