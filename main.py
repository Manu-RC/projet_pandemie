from interface_graphique import Ui_Form
from universe import Universe 
from simulation import Simulation
from Maladie import Maladie
from sortie import Sortie
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication


        
        
def main():

    app = QtWidgets.QApplication(sys.argv)
    
    out = Sortie()

    out.univers.show()
    out.ui.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()


