import algebre as alg
import numpy as np
from math import cos, pi, sin
import individu as ind

def collision_laterale(u,v):
    return -u, v

def collision_longitudinale(u,v):
    return u,-v

def collision_coin(u,v):
    return -u,-v

def collision_particule(I_1,I_2):

    """I_1 et I_2 sont des objets Individu"""
    x1 = np.array((I_1.x,I_1.y))
    x2 = np.array((I_2.x,I_2.y))
    v1 = np.array((I_1.vx,I_1.vy))
    v2 = np.array((I_2.vx,I_2.vy))
    d = np.linalg.norm(x1-x2)**2
    u_estime = v1 - (2 * I_2.masse * np.dot(v1-v2,x1-x2) / (d * (I_1.masse + I_2.masse))) * (x1-x2)
    v_estime = v2 - (2 * I_1.masse * np.dot(v2-v1,x2-x1) / (d * (I_1.masse + I_2.masse))) * (x2-x1)
    return u_estime[0], u_estime[1], v_estime[0], v_estime[1]

def init_vitesse():
    return alg.uniform(-2,2), alg.uniform(-2,2)

def loi_isolement(I_1):
    choix = alg.uniform(0,1)
    if choix < 0.05:
        return 0,0 
    else:
        return I_1.vx,I_1.vy

if "__main__" == __name__:
    
    pass
    #print(collision_particule(4,0,-6,0,3,5)) # Cas 1D wikipédia
    #print(collision_particule(1,0,0,0,1,1)) # Cas 1D avec masse identique et un individu à l'arret
    #print(collision_particule(1,0,-1,0,2,1))
    #print(collision_particule(1,0,0.5,0,1,1))

