import numpy as np
from math import sqrt


def uniform(a,b):
    """Sort un nombre compris entre a et b de manière aléatoire"""
    return a + (b-a) * np.random.uniform(0,1)

def gaussienne(facteur):
    """Sort un nombre compris entre 0 et 1 suivant loi normal spécifique
        Potentiellement, on peut avoir une valeur en dehors de [0,1]
        Dans ce cas on affecte la valeur du taux de contagion ou le taux de letalite cf appelle dans simu"""
    float_rand = 0.1 * np.random.randn() + facteur #on recentre la loi normale moyenne=facteur et 0.1 la variance
    if float_rand > 1 :
        return facteur
    elif float_rand < 0 :
        return facteur
    else:
        return float_rand

def seed():
    np.random.seed()
    
def binomiale(p):
    return np.random.binomial(1, p)

def distance(cercle_1,cercle_2):
    """ Entrée : un couple (position x, position y, rayon)
        Sortie : un flottant """
    return sqrt((cercle_1[0]-cercle_2[0])**2 + (cercle_1[1]-cercle_2[1])**2)

if "__main__" == __name__:
    pass
