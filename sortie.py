from interface_graphique import Ui_Form
from universe import Universe 
from simulation import Simulation
from Maladie import Maladie

from individu import Individu


class Sortie : 

    def __init__(self):

        self.ui = Ui_Form()
        
        
        maladie = Maladie(0)
        simulation = Simulation(maladie,900,900)

        simulation.gen(100,10)
        self.univers = Universe(simulation)
        self.ui.setupUi(self.univers)
        self.ui.graphicsView.setScene(self.univers.scene)

    
        # self.ui.StartButton.clicked.connect(univers.stop)
        # self.ui.Stopbutton.clicked.connect(univers.start)

        univers = Universe(simulation)
        self.ui.setupUi(univers)
        self.ui.graphicsView.setScene(univers.scene)

    
        self.ui.StartButton.clicked.connect(univers.stop)
        self.ui.Stopbutton.clicked.connect(univers.start)


