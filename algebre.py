import numpy as np
from math import sqrt


def uniform(a,b):
    """Sort un nombre compris entre a et b de manière aléatoire"""
    return a + (b-a) * np.random.uniform(0,1)

def distance(cercle_1,cercle_2):
    """ Entrée : un couple (position x, position y, rayon)
        Sortie : un flottant """
    return sqrt((cercle_1[0]-cercle_2[0])**2 + (cercle_1[1]-cercle_2[1])**2)

if "__main__" == __name__:
    pass
