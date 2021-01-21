import physique
import simulation


class Individu:
    """Initialisation d'un individu
    Un individu est défini par sa position (x,y), sa vitesse de déplacement et sa taille modilisé par un rayon
    Les parametres de la simulation sont aussi fournit par l'attribut simulation qui une instantiation de classe simulation
    On supposera dans notre modèle que chaque individu est masse unitaire
    """

    def __init__(self, rayon, x, y, vx, vy, simulation,taux_respect_rules, maladie=None, masse=1):  
        self.rayon = rayon
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.simulation = simulation
        self.touch = None
        self.masse = masse
        self.etat = "Sain"  # "Sain" "Infecte" ou "Immunise" (les morts sont supprimés de la population)
        self.maladie = maladie
        self.taux_respect_rules = taux_respect_rules

    def __repr__(self):
        return "position x : {0:02f} \n " \
        "position y : {1:02f} \n " \
        "vitesse vx : {2:02f} \n " \
        "vitesse vy : {3:02f} \n " \
        "my touch   : {6} \n" \
        "------------------------ \n ".format(self.x,self.y,self.vx,self.vy,self.ax,self.ay,self.touch)

    def set_position(self, x, y):
        """met à jour la position (peut être sujet à approximation)"""
        dt = self.simulation.time_increment
        self.x = x + self.vx * dt
        self.y = y + self.vy * dt

    def next_position(self):
        """renvoie la prochaine position (si tout se passe bien)"""
        dt = self.simulation.time_increment
        x = self.x + self.vx * dt
        y = self.y + self.vy * dt

        return x, y

    def set_vitesse(self, vx, vy):
        """affecte un nouveau vecteur vitesse"""
        self.vx = vx
        self.vy = vy

    def move(self, x_max, y_max):
        """Gestion du mouvement en fonction de la condition initiale touch (defini dans simulation)"""
        # Mise à jour de la vitesse et position en cas de contact avec le mur de droite ou de gauche
        if self.touch in ["left_wall", "right_wall"]:
            self.move_vertical_wall(x_max)
        # Mise à jour de la vitesse et de la position en cas de contact avec le mur haut et le mur bas
        elif self.touch in ["up_wall", "down_wall"]:
            self.move_horizontal_wall(y_max)
        # Mise à jour de la vitesse et de la position en cas de contact avec un coin
        elif self.touch in ["up-left_corner", "up-right_corner", "down-rigth_corner", "down-left_corner"]:
            self.move_corner(x_max, y_max)
        # Mise à jour de la position en cas de contact avec une autre particule
        elif type(self.touch) is Individu:
            self.move_contact()
        # Particule qui est rentrée en contact avec une autre, tout a déjà été traité
        elif self.touch == "done":
            pass
        # Mise à jour de la vitesse et de la position si aucun contact pendant dt
        else:
            self.move_classic()
        self.touch = None

    def move_classic(self):
        self.set_vitesse(self.vx, self.vy)
        self.set_position(self.x, self.y)

    def move_horizontal_wall(self, y_max):
        u, v = physique.collision_longitudinale(self.vx, self.vy)
        self.set_vitesse(u, v)
        if self.touch == "up_wall":
            self.set_position(self.x, self.rayon)
        else:
            self.set_position(self.x, y_max - self.rayon)

    def move_vertical_wall(self, x_max):
        u, v = physique.collision_laterale(self.vx, self.vy)
        self.set_vitesse(u, v)
        if self.touch == "left_wall":
            self.set_position(self.rayon, self.y)
        else:
            self.set_position(x_max - self.rayon, self.y)

    def move_contact(self):
        u1, v1, u2, v2 = physique.collision_particule(self, self.touch)
        # Mise à jour des vitesses des 2 individus à la fois
        self.set_vitesse(u1, v1)
        self.touch.set_vitesse(u2, v2)
        self.set_position(self.x, self.y)
        self.touch.set_position(self.touch.x, self.touch.y)
        # On ne recalule pas la physique de collision avec l'individu 2 
        self.touch.touch = "done"

    def move_corner(self, x_max, y_max):
        u, v = physique.collision_coin(self.vx, self.vy)
        self.set_vitesse(u, v)
        if self.touch == "up-left_corner":
            self.set_position(self.rayon, self.rayon)
        elif self.touch == "up-right_corner":
            self.set_position(x_max - self.rayon, self.rayon)
        elif self.touch == "down-left_corner":
            self.set_position(self.rayon, y_max - self.rayon)
        elif self.touch == "down-right_corner":
            self.set_position(x_max - self.rayon, y_max - self.rayon)

    def move_reinit(self, x_max, y_max, vitesse_init):
        # Redemmarrage des particules qui ont respecté leur isolement et que les conditions d'isolement sont finies (cf politique.py et physique.py) 
        if self.vx == 0 and self.vy == 0:
            u, v = physique.init_vitesse(vitesse_init)
            self.set_vitesse(u, v)
        self.move(x_max, y_max)

    def move_isolement(self, x_max, y_max):
        self.move(x_max, y_max)
        u, v = physique.loi_isolement(self)
        self.set_vitesse(u, v)
        self.set_position(self.x, self.y)
        self.touch = None

    def move_couvre_feu(self, x_max, y_max):
        self.move(x_max, y_max)
        u, v = physique.loi_isolement(self)
        self.set_vitesse(u, v)
        self.set_position(self.x, self.y)
        self.touch = None