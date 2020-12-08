from interface_graphique import Ui_Form
from universe import Universe 
from simulation import Simulation
from Maladie import Maladie

class Sortie : 

    def __init__(self):

        self.ui = Ui_Form()
        
        
        maladie = Maladie(0)
        simulation = Simulation(maladie,500,500)
        univers = Universe(simulation)
        self.ui.setupUi(univers)
        self.ui.graphicsView.setScene(univers.scene)

    
        self.ui.StartButton.clicked.connect(univers.stop)
        self.ui.Stopbutton.clicked.connect(univers.start)


