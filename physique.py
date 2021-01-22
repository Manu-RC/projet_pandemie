import algebre as alg
import numpy as np
from math import cos, pi, sin
import individu as ind

def collision_laterale(u,v):
    """Réflection suivant l'axe y. Seul la composante vx est modifiée par son opposé"""
    return -u, v

def collision_longitudinale(u,v):
    """Réfection suivant l'axe x, Seul la composante vy est modifiée par son oppposé"""
    return u,-v

def collision_coin(u,v):
    """Réflection suivant les axes x et y. La vitesse est en sorti est opposée"""
    return -u,-v

def collision_particule(I_1,I_2):
    """I_1 et I_2 sont des objets Individu
    Utilisation d'une physique de collision élastique. Il y a conservation de l'energie cinétique.
    Les formules utilisées sont issues de la page wikipédia : https://en.wikipedia.org/wiki/Elastic_collision"""
    x1 = np.array((I_1.x,I_1.y))
    x2 = np.array((I_2.x,I_2.y))
    v1 = np.array((I_1.vx,I_1.vy))
    v2 = np.array((I_2.vx,I_2.vy))
    d = np.linalg.norm(x1-x2)**2
    u_estime = v1 - (2 * I_2.masse * np.dot(v1-v2,x1-x2) / (d * (I_1.masse + I_2.masse))) * (x1-x2)
    v_estime = v2 - (2 * I_1.masse * np.dot(v2-v1,x2-x1) / (d * (I_1.masse + I_2.masse))) * (x2-x1)
    return u_estime[0], u_estime[1], v_estime[0], v_estime[1]

def init_vitesse(borne_vitesse):
    """Initialise le vecteur vitesse des individus"""
    return alg.uniform(-borne_vitesse,borne_vitesse), alg.uniform(-borne_vitesse,borne_vitesse)

def loi_isolement(I_1):
    """On regarde si l'invidu respecte les lois, si il les respect l'arrete en lui mettant une vitesse nulle"""
    if I_1.respect:
        return 0,0 
    else:
        return I_1.vx,I_1.vy
