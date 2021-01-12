from fenetre_graphique import Ui_Pandemie
from universe import Universe 
from simulation import Simulation
from Maladie import Maladie
from sortie import Sortie
import sys
from PyQt5 import QtWidgets, QtGui, QtCore


        
        
def main():

    #maladie initiale
    hit_time = 0
    Taux_contagion = 1
    muta_init = 0.01
    Duree_transmissibilite = 200
    maladie_init = Maladie(hit_time,Taux_contagion,muta_init,Duree_transmissibilite)

    nombre_contamines_init = 30

    longueur = 500
    hauteur = 500
    nombre_individus = 50
    rayon = 5
    refresh_time = 10 #millisecondes

    app = QtWidgets.QApplication(sys.argv)
    
    out = Sortie(longueur,hauteur,nombre_individus,rayon,refresh_time,maladie_init,nombre_contamines_init)

    out.univers.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()


