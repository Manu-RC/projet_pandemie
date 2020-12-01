import algebre as alg
import numpy as np
from math import cos, pi, sin


def collision_laterale(u,v):
    return -u, v

def collision_longitudinale(u,v):
    return u,-v

def collision_particule(ux,uy,vx,vy,m1,m2):

    theta_1 = alg.angle_theta(ux,uy)
    theta_2 = alg.angle_theta(vx,vy)
    phi = alg.angle_phi(ux,uy,vx,vy)
    print(theta_1, theta_2)
    print(phi)
    #Calcul de u et v
    u = alg.vitesse(ux,uy)
    print("vitesse u : ", u)
    v= alg.vitesse(vx,vy)
    print("vitesse v : ", v)
    # Estimation de la nouvelle vitesse
    ux_estime = round((u * cos(theta_1 - phi)  * (m1 - m2) + 2 * m2 * v * cos(theta_2 - phi)) * cos(phi) / (m1 + m2) + u * sin(theta_1 - phi) * cos(phi + pi / 2),2)
    uy_estime = round((u * cos(theta_1 - phi)  * (m1 - m2) + 2 * m2 * v * cos(theta_2 - phi)) * sin(phi) / (m1 + m2) + u * sin(theta_1 - phi) * sin(phi + pi / 2),2)

    vx_estime = round((v * cos(theta_2 - phi)  * (m2 - m1) + 2 * m1 * u * cos(theta_1 - phi)) * cos(phi) / (m1 + m2) + v * sin(theta_2 - phi) * cos(phi + pi / 2),2)
    vy_estime = round((v * cos(theta_2 - phi)  * (m2 - m1) + 2 * m1 * u * cos(theta_1 - phi)) * sin(phi) / (m1 + m2) + v * sin(theta_2 - phi) * sin(phi + pi / 2),2)

    return ux_estime, uy_estime, vx_estime, vy_estime


if "__main__" == __name__:

    print(collision_particule(4,0,-6,0,3,5)) # Cas 1D wikipédia
    print(collision_particule(1,0,0,0,1,1)) # Cas 1D avec masse identique et un individu à l'arret
    print(collision_particule(1,0,-1,0,2,1))
    print(collision_particule(1,0,0.5,0,1,1))


