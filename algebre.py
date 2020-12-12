import numpy as np
from math import sqrt, cos, pi, sin


def liste_nombre(n):
    return [i for i in range(0,n-1)]

def uniform(a,b):
    """Sort un nombre compris entre a et b de manière aléatoire"""
    return a + (b-a) * np.random.uniform(0,1)

def angle_phi(ux,uy,vx,vy):
    if ux == 0 and uy == 0:
        return angle_theta(vx,vy)
    elif vx == 0 and vy ==0:
        return angle_theta(ux,uy)
    else:
        u = [ux,uy]
        v = [vx,vy]
        return np.arccos(produit_scalaire(u,v))

def angle_theta(vx,vy):
    if vx == 0 and vy == 0:
        return 0
    else:
        v = [vx,vy]
        return np.arccos(vx / np.linalg.norm(v))

def normalisation(u):
    return u / np.linalg.norm(u)

def produit_scalaire(u,v):
    return np.dot(normalisation(u),normalisation(v))

def vitesse(ux,uy):
    return sqrt(ux**2 + uy**2)

def vecteur(ax,ay,bx,by):
    return bx - ax , by -ay

def distance(cercle_1,cercle_2):
    """ Entrée : un couple (position x, position y, rayon)
        Sortie : un flottant """
    return sqrt((cercle_1[0]-cercle_2[0])**2 + (cercle_1[1]-cercle_2[1])**2)


if "__main__" == __name__:

    #Test unitaire fonction angle theta
    angle1 = angle_theta(1,2)
    print(angle1)
    print(np.arccos((1 / np.math.sqrt(5))))

    #Test unitaire de la fonction angle phi
    angle2 = angle_phi(1,0,2,0)
    print(angle2)