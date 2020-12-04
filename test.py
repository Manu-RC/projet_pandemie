import math
import sys
import random as rd
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPen, QBrush, QColor

class PanZoomView(QtWidgets.QGraphicsView):
    """An interactive view that supports Pan and Zoom functions"""

    def __init__(self, scene):
        super().__init__(scene)


class Universe(QtWidgets.QWidget) :

    def __init__(self,l,h):

        super().__init__()
        self.length = l
        self.height = h
        self.setWindowTitle("test")
        self.resize(l,h)
        self.scene = QtWidgets.QGraphicsScene()
        self.view = PanZoomView(self.scene)
        self.items = QtWidgets.QGraphicsItemGroup()
        self.scene.addItem(self.items)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.add_rd_people)
        root_layout = QtWidgets.QVBoxLayout(self)
        root_layout.addWidget(self.view)
        self.add_rd_people()
        self.add_shortcut('f', lambda: self.playpause())
        
        self.show()
        
   

    def add_rd_people(self):

        self.scene.clear()
        group = QtWidgets.QGraphicsItemGroup()
        self.scene.addItem(group)

        for i in range(10):

            rd_x = rd.uniform(10,self.length)
            rd_y = rd.uniform(10,self.height) 
            bounds = QtCore.QRectF(rd_x,rd_y, 10, 10)
            item = QtWidgets.QGraphicsEllipseItem(bounds, group )
            item.setBrush(QBrush(QColor("red")))

        
        
    
    # def fit_scene_in_view(self):
    #     self.view.fitInView(self.view.sceneRect(), QtCore.Qt.KeepAspectRatio)

    def add_shortcut(self,text, slot):
            """creates an application-wide key binding"""
            shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(text), self)
            shortcut.activated.connect(slot)

    def playpause(self):
        """this slot toggles the replay using the timer as model"""
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(10)

    

def main():

    # Initialize Qt
    ## The main application (type QtWidgets.QApplication)
    app = QtWidgets.QApplication([])
    # create the radar view and the time navigation interface
    ## The main graphical window (type radarview.Radarview)
    main_window = Universe(500,500)

    # enter the main loop
    sys.exit(app.exec_())


main()