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
    """I1 et I2 sont des objets individu"""
    if I_1 == I_2:
        return I_1.vx,I_1.vy,I_2.vx,I_2.vy
    else:
        theta_1 = alg.angle_theta(I_1.vx,I_1.vy)
        theta_2 = alg.angle_theta(I_2.vx,I_2.vy)
        phi = alg.angle_phi(I_1.vx,I_1.vy,I_2.vx,I_2.vy)
        #Calcul de u et v
        u = alg.vitesse(I_1.vx,I_1.vy)
        v= alg.vitesse(I_2.vx,I_2.vy)
        # Estimation de la nouvelle vitesse pour la particule 1
        ux_estime = round((u * cos(theta_1 - phi)  * (I_1.masse - I_2.masse) + 2 * I_2.masse * v * cos(theta_2 - phi)) * cos(phi) / (I_1.masse + I_2.masse) + u * sin(theta_1 - phi) * cos(phi + pi / 2),2)
        uy_estime = round((u * cos(theta_1 - phi)  * (I_1.masse - I_2.masse) + 2 * I_2.masse * v * cos(theta_2 - phi)) * sin(phi) / (I_1.masse + I_2.masse) + u * sin(theta_1 - phi) * sin(phi + pi / 2),2)
        # Estimation de la nouvelle vitesse pour la particule 2
        vx_estime = round((v * cos(theta_2 - phi)  * (I_1.masse - I_2.masse) + 2 * I_1.masse * u * cos(theta_1 - phi)) * cos(phi) / (I_1.masse + I_2.masse) + v * sin(theta_2 - phi) * cos(phi + pi / 2),2)
        vy_estime = round((v * cos(theta_2 - phi)  * (I_1.masse - I_2.masse) + 2 * I_1.masse * u * cos(theta_1 - phi)) * sin(phi) / (I_1.masse + I_2.masse) + v * sin(theta_2 - phi) * sin(phi + pi / 2),2)

        return ux_estime, uy_estime, vx_estime, vy_estime


if "__main__" == __name__:
    
    pass
    #print(collision_particule(4,0,-6,0,3,5)) # Cas 1D wikipédia
    #print(collision_particule(1,0,0,0,1,1)) # Cas 1D avec masse identique et un individu à l'arret
    #print(collision_particule(1,0,-1,0,2,1))
    #print(collision_particule(1,0,0.5,0,1,1))

