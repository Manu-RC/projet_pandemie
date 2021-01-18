from Maladie import Maladie
from sortie import Sortie
import sys
from PyQt5 import QtWidgets


def main(longueur,largeur,nombre_individus,nombre_contamines_init):

    #maladie initiale
    hit_time = 0
    Taux_contagion = 0.5
    muta_init = 0.01
    Duree_transmissibilite = 200
    lethalite = 1
    maladie_init = Maladie(hit_time,Taux_contagion,muta_init,Duree_transmissibilite,lethalite)

    rayon = 4
    refresh_time = 20 #millisecondes

    app = QtWidgets.QApplication(sys.argv)
    
    out = Sortie(longueur,largeur,nombre_individus,rayon,refresh_time,maladie_init,nombre_contamines_init)

    out.univers.show()
    sys.exit(app.exec_())






