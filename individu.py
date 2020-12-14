import numpy
import physique
import simulation

class Individu:
    """Initialisation d'un individu
    Un individu est défini par sa position (x,y), sa vitesse de déplacement et sa taille modilisé par un rayon
    """

    def __init__(self, rayon, x, y, vx, vy, simulation, masse=1): #j'ai modifié les entrees car il n'y avait pas vx et vy
        self.rayon = rayon
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = 0   # Prise en compte de l'accélaration dans le calcul de la position
        self.ay = 0   # Permet d'atténuer le décalage entre l'image et les calcul de la simu
        self.simulation = simulation
        self.touch = None
        self.masse = masse
        self.etat = 'sain'
        
    def __repr__(self):
        return "position x : {0:02f} \n " \
               "position y : {1:02f} \n " \
               "vitesse vx : {2:02f} \n " \
               "vitesse vy : {3:02f} \n " \
               "acceleration ax : {4:02f} \n " \
               "acceleration ay : {5:02f} \n " \
               "my touch   : {6} \n" \
               "------------------------ \n ".format(self.x,self.y,self.vx,self.vy,self.ax,self.ay,self.touch)

    def set_position(self,x,y):
        """met à jour la position (peut être sujet à approximation)"""
        #self.x += self.vx * t
        #self.y += self.vy * t
        dt = self.simulation.time_increment
        self.x  = x + self.vx * dt #+  (self.ax * t**2) / 2
        self.y  = y + self.vy * dt #+  (self.ay * t**2) / 2

    def next_position(self):
        """renvoie la prochaine position (si tout se passe bien)"""
        #self.x += self.vx * t
        #self.y += self.vy * t
        dt = self.simulation.time_increment
        x  = self.x + self.vx * dt #+  (self.ax * t**2) / 2
        y  = self.y + self.vy * dt #+  (self.ay * t**2) / 2

        return x,y

    def set_vitesse(self,vx,vy):
        """affecte un nouveau vecteur vitesse"""
        self.vx = vx
        self.vy = vy

    def set_acceleration(self,vx,vy):
        dt = self.simulation.time_increment
        self.ax = (vx - self.vx) / dt
        self.ay = (vy - self.vy) / dt

    def move(self,x_max,y_max):

        # Mise à jour de la vitesse et position en cas de contact avec le mur de droite ou de gauche
        if self.touch in ["left_wall","right_wall"]:
            u, v = physique.collision_laterale(self.vx,self.vy)
            self.set_vitesse(u,v)
            if self.touch == "left_wall":
                self.set_position(self.rayon,self.y)
            else:
                self.set_position(x_max-self.rayon,self.y)
        # Mise à jour de la vitesse et de la position en cas de contact avec le mur haut et le mur bas
        elif self.touch in ["up_wall","down_wall"]:
            u, v = physique.collision_longitudinale(self.vx,self.vy)
            self.set_vitesse(u,v)
            if self.touch == "up_wall":
                self.set_position(self.x,self.rayon)
            else:
                self.set_position(self.x,y_max-self.rayon)
        # Mise à jour de la vitesse et de la position en cas de contact avec un coin
        elif self.touch in ["up-left_corner","up-right_corner","down-rigth_corner","down-left_corner"]:
            u,v = physique.collision_coin(self.vx,self.vy)
            self.set_vitesse(u,v)
            if self.touch == "up-left_corner":
                self.set_position(self.rayon,1+self.rayon)
            elif self.touch == "up-right_corner":
                self.set_position(x_max-self.rayon,self.rayon)
            elif self.touch == "down-left_corner":
                self.set_position(self.rayon,y_max - self.rayon)
            elif self.touch == "down-right_corner":
                self.set_position(x_max-self.rayon,y_max-self.rayon)
        # Mise à jour de la position en cas de contact avec une autre particule
        elif type(self.touch) is Individu:
            u1,v1,u2,v2 = physique.collision_particule(self,self.touch)
            self.set_vitesse(u1,v1)
            self.touch.set_vitesse(u2,v2)
            self.set_position(self.x,self.y)
            self.touch.set_position(self.touch.x,self.touch.y)
            self.touch.touch = "done"
        # Particule qui est rentrée en contact avec une autre, tout a déjà été traité
        elif self.touch == "done":
            pass
        # Mise à jour de la vitesse et de la position si aucun contact pendant dt
        else:
            self.set_vitesse(self.vx,self.vy)
            self.set_position(self.x,self.y)
        self.touch = None