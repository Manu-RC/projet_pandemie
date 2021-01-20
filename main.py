from maladie import Maladie
from sortie import Sortie
import sys
from PyQt5 import QtWidgets


def main(longueur,largeur,nombre_individus,nombre_contamines_init,borne_vitesse_init,taux_respect_rules,hit_time,taux_contagion,mutation_init,duree_transmissibilite_init,letalite):

    maladie_init = Maladie(hit_time,taux_contagion,mutation_init,duree_transmissibilite_init,letalite)
    rayon = 4
    refresh_time = 20 #millisecondes
    app = QtWidgets.QApplication(sys.argv)
    out = Sortie(longueur,largeur,nombre_individus,rayon,refresh_time,maladie_init,nombre_contamines_init,borne_vitesse_init,taux_respect_rules)
    out.univers.show()
    sys.exit(app.exec_())






