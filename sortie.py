from interface_graphique import Ui_Form
from universe import Universe 
from simulation import Simulation
from Maladie import Maladie

from individu import Individu


class Sortie : 

    def __init__(self,dimension_x,dimension_y,nombre_individus,rayon,refresh_time):

        self.ui = Ui_Form()
        
        simulation = Simulation(dimension_x,dimension_y)
        simulation.generation(rayon,nombre_individus)
        
        self.univers = Universe(simulation,refresh_time)
        self.ui.setupUi(self.univers)
        self.ui.graphicsView.setScene(self.univers.scene)

        # univers = Universe(simulation)
        # self.ui.setupUi(univers)
        # self.ui.graphicsView.setScene(univers.scene)

    
        self.ui.StartButton.clicked.connect(self.univers.start)
        self.ui.Stopbutton.clicked.connect(self.univers.stop)


