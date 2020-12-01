import numpy as np
from math import sqrt, cos, pi, sin


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
    #theta = angle_theta(ux,uy)
    #if theta == 0:
        #return ux / cos(theta)
    #else:
        #return uy / sin(theta)
    return sqrt(ux**2 + uy**2)

def vecteur(ax,ay,bx,by):
    return bx - ax , by -ay

if "__main__" == __name__:

    #Test unitaire fonction angle theta
    angle1 = angle_theta(1,2)
    print(angle1)
    print(np.arccos((1 / np.math.sqrt(5))))

    #Test unitaire de la fonction angle phi
    angle2 = angle_phi(1,0,2,0)
    print(angle2)