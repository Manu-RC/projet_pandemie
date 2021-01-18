import matplotlib.pyplot as plt
from fenetre_graphique import Ui_Pandemie
from universe import Universe 
from simulation import Simulation
from Maladie import Maladie
from PyQt5 import QtCore, QtGui, QtWidgets
from individu import Individu
import politique


class Sortie : 

    def __init__(self,dimension_x,dimension_y,nombre_individus,rayon,refresh_time,maladie_init,nombre_contamines_init):

        self.ui = Ui_Pandemie()
        
        self.universe_width = dimension_y
        self.universe_height = dimension_x
        self.simulation = Simulation(dimension_x,dimension_y,maladie_init)
        self.simulation.generation(rayon,nombre_individus,nombre_contamines_init)
        self.refresh_time = refresh_time
        
        #connexion de la scene de l'univers au widget
        self.univers = Universe(self.simulation,refresh_time)
        self.ui.setupUi(self.univers)
        self.ui.graphicsView.setScene(self.univers.scene)
        self.fit_scene_in_view()
        self.set_simu()



        

        #connexion du timer à l'evolution de la simulation
        self.univers.timer.timeout.connect(self.update_simu)

        #connexion des boutons start et stop
        self.ui.StartButton.clicked.connect(self.start)
        self.ui.StopButton.clicked.connect(self.stop)

        #connexion des boutons d'accélération et de décélération de la simulation
        self.ui.x2.clicked.connect(self.x2)
        self.ui.x4.clicked.connect(self.x4)

        self.ui.reduce_speed_x4.clicked.connect(self.reduce_speed_x4)
        self.ui.reduce_speed_x2.clicked.connect(self.reduce_speed_x2)

        #connexion de la Combo Box
        self.ui.choice_politique.currentTextChanged.connect(self.choice_politique)

        #connexion du bouton Graph
        self.ui.Graph_button.clicked.connect(self.open_close_history)

    def fit_scene_in_view(self):
        self.ui.graphicsView.fitInView(self.ui.graphicsView.sceneRect(), QtCore.Qt.KeepAspectRatio)

    def set_simu(self):

        group = QtWidgets.QGraphicsItemGroup()
        self.univers.scene.addItem(group)
        simu_contour = QtCore.QRectF(0,0,self.universe_height,self.universe_width)
        item_contour = QtWidgets.QGraphicsRectItem(simu_contour, group)
        for individu in self.simulation.population:

            bounds = QtCore.QRectF(individu.x,individu.y,individu.rayon*2,individu.rayon*2)
            item = QtWidgets.QGraphicsEllipseItem(bounds, group)
            if individu.etat == "Infecte":
                item.setBrush(QtGui.QBrush(QtGui.QColor("red")))
            elif individu.etat == "Immunise":
                item.setBrush(QtGui.QBrush(QtGui.QColor("yellow")))
            else:
                item.setBrush(QtGui.QBrush(QtGui.QColor("green")))

    def update_simu(self):  
        """met à jour visuellement les différents états de la simulation """
        self.simulation.advance()
        self.univers.scene.clear()
        self.ui.Compteur_infectes.display(self.simulation.infectes)
        self.ui.Compteur_Morts.display(self.simulation.morts)
        self.ui.Compteur_sains.display(self.simulation.sains)
        self.ui.Compteur_population_totale.display(len(self.simulation.population))
        self.ui.Compteur_immunises.display(self.simulation.immunises)
        group = QtWidgets.QGraphicsItemGroup()
        self.univers.scene.addItem(group)
        simu_contour = QtCore.QRectF(0,0,self.universe_height,self.universe_width)
        item_contour = QtWidgets.QGraphicsRectItem(simu_contour, group)
        for individu in self.simulation.population:

            bounds = QtCore.QRectF(individu.x,individu.y,individu.rayon*2,individu.rayon*2)
            item = QtWidgets.QGraphicsEllipseItem(bounds, group)
            if individu.etat == "Infecte":
                item.setBrush(QtGui.QBrush(QtGui.QColor("red")))
            elif individu.etat == "Immunise":
                item.setBrush(QtGui.QBrush(QtGui.QColor("yellow")))
            else:
                item.setBrush(QtGui.QBrush(QtGui.QColor("green")))
    

    def open_close_history(self):
        if not(open_history.has_been_called):
            open_history(self.simulation)
        else:
            close_history()
        # open_history(self.simulation)
    
    

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

    def x2(self):
        self.simulation.change_speed(2)

    def x4(self):
        self.simulation.change_speed(4)

    def reduce_speed_x4(self):
        self.simulation.change_speed(0.25)

    def reduce_speed_x2(self):
        self.simulation.change_speed(0.5)

    def choice_politique(self):
        if self.ui.choice_politique.currentText() == "Confinement":
            self.simulation.politique = "confinement"
        if self.ui.choice_politique.currentText() == "Couvre-feu":
            self.simulation.politique = "couvre-feu"
        else:
            self.simulation.politique = None


"----------------------------------------------------------- POUR LE GRAPHE"

def open_history(simulation): 
        """affiche les courbes représentant l'historique de la simulation"""
        open_history.has_been_called=True
        def plot_current_state():
            time = []
            sains = []
            infectes = []
            immunises = []
            morts = []
            for etat in simulation.historique:
                time.append(etat[0])
                sains.append(etat[1])
                infectes.append(etat[2])
                immunises.append(etat[3])
                morts.append(etat[4])
            plt.plot(time,sains,color="green")
            plt.plot(time,infectes,color="red")
            plt.plot(time,immunises,color="yellow")
            plt.plot(time,morts,color="black")

        plt.title = "Historique de la simulation"
        plt.xlabel("temps")
        plot_current_state()
        while not(close_history.has_been_called):
            plt.clf()
            plot_current_state()
            plt.pause(0.2)
        plt.close()
        close_history.has_been_called=False
open_history.has_been_called=False  

def close_history():
    """permet de signaler à open_history quand est ce que l'utilisateur veut fermer le graphe"""               
    close_history.has_been_called=True
    open_history.has_been_called=False
    pass
close_history.has_been_called=False




