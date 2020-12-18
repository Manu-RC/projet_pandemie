from interface_graphique import Ui_Form
from universe import Universe 
from simulation import Simulation
from Maladie import Maladie
from sortie import Sortie
import sys
from PyQt5 import QtWidgets, QtGui, QtCore


        
        
def main():

    longueur = 500
    hauteur = 500
    nombre_individus = 50
    rayon = 5
    refresh_time = 10 #millisecondes

    app = QtWidgets.QApplication(sys.argv)
    
    out = Sortie(longueur,hauteur,nombre_individus,rayon,refresh_time)

    out.univers.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()


