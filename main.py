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
    Taux_contagion = 0.5
    muta_init = 0.01
    Duree_transmissibilite = 200
    lethalite = 1
    maladie_init = Maladie(hit_time,Taux_contagion,muta_init,Duree_transmissibilite,lethalite)

    nombre_contamines_init = 30

    longueur = 800
    hauteur = 500
    nombre_individus = 100
    rayon = 4
    refresh_time = 20 #millisecondes

    app = QtWidgets.QApplication(sys.argv)
    
    out = Sortie(longueur,hauteur,nombre_individus,rayon,refresh_time,maladie_init,nombre_contamines_init)

    out.univers.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()


