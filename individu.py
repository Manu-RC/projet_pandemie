import numpy
import physique

class Individu:
    """Initialisation d'un individu
    Un individu est défini par sa position (x,y), sa vitesse de déplacement et sa taille modilisé par un rayon
    """

    def __init__(self, rayon, x, y, vx, vy, masse=1): #j'ai modifié les entrees car il n'y avait pas vx et vy
        self.rayon = rayon
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.touch = None
        self.masse = masse
        self.etat = 'sain'

    def set_position(self, t):
        self.x += self.vx * t
        self.y += self.vy * t

    def set_vitesse(self,vx,vy):
        self.vx = vx
        self.vy = vy

    def move(self,t):

        pass





def contact(i1, i2):
    #i1 et i2 sont des objets Individu
    #retourne un booleen
    return True

if "__main__" == __name__:
    I_1 = Individu(1,3,4,2)
    I_2 = Individu(1,2,6,0)

