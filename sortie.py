from interface_graphique import Ui_Form
from universe import Universe 
from simulation import Simulation
from Maladie import Maladie
from PyQt5 import QtCore, QtGui, QtWidgets
from individu import Individu


class Sortie : 

    def __init__(self,dimension_x,dimension_y,nombre_individus,rayon,refresh_time,maladie_init):

        self.ui = Ui_Form()
        

        self.simulation = Simulation(dimension_x,dimension_y,maladie_init)
        self.simulation.generation(rayon,nombre_individus)

        self.refresh_time = refresh_time
        
        #connexion de la scene de l'univers au widget
        self.univers = Universe(self.simulation,refresh_time)
        self.ui.setupUi(self.univers)
        self.ui.graphicsView.setScene(self.univers.scene)


        

        #connexion du timer à l'evolution de la simulation
        self.univers.timer.timeout.connect(self.update_simu)

        #connexion des boutons start et stop
        self.ui.StartButton.clicked.connect(self.start)
        self.ui.Stopbutton.clicked.connect(self.stop)
        
        #connexion de la progress bar au pourcentage de personnes contaminées
        self.ui.Barre_contamination.setValue(self.simulation.pourcentage_contamines)


    def update_simu(self):  
        """met à jour visuellement les différents états de la simulation """
        self.simulation.advance()
        self.univers.scene.clear()
        self.ui.Compteur_malades.display(self.simulation.malades)
        group = QtWidgets.QGraphicsItemGroup()
        self.univers.scene.addItem(group)

        for individu in self.simulation.population:

            bounds = QtCore.QRectF(individu.x,individu.y,individu.rayon*2,individu.rayon*2)
            item = QtWidgets.QGraphicsEllipseItem(bounds, group)
            if individu.etat == "contaminé":
                item.setBrush(QtGui.QBrush(QtGui.QColor("red")))
            elif individu.etat == "immunisé":
                item.setBrush(QtGui.QBrush(QtGui.QColor("yellow")))
            else:
                item.setBrush(QtGui.QBrush(QtGui.QColor("green")))

    def playpause(self):
        """this slot toggles the replay using the timer as model"""
        if self.univers.timer.isActive():
            self.univers.timer.stop()
        else:
            self.univers.timer.start(self.refresh_time)


    def start(self):

        if not self.univers.timer.isActive():

            self.univers.timer.start(self.refresh_time)

    def stop(self):

        if self.univers.timer.isActive():

            self.univers.timer.stop()

