import numpy as np
from individu import Individu
import physique
import algebre as alg


class Simulation :
    """ Cette classe permet la génération des différentes particules, gère les collisions entre les particules
        et les bords du domaines ; ainsi que l'avancement dans le temps de la simulation. """

    def __init__(self,maladie,x_max,y_max):

        #dimensions de l'environnement
        self.x_max = x_max
        self.y_max = y_max
        self.population = []
        self.maladie = maladie
        #horloge de la simulation 
        self.time = 0
        #pas de temps de la simulation
        self.time_increment = 0.1

    def predict_for_all(self):
        """prédit la position de chaque individu et crée des paires de collision si collision il y a"""
        predictions = [self.predict(individu) for individu in self.population]  #contient les prochaines coordonnees des individus ou None s'ils touchent déjà un mur ou un coin
        n = len(self.population)
        for i in range(n-1):
            for j in range(i+1,n): #les individus avant i ont deja ete traites
                if predictions[i] is not None and predictions[j] is not None :
                    if collision(predictions[i],predictions[j]):
                        #on donne a chaque individu l'individu avec qui il va entrer en collision
                        individu_i = self.population[i]
                        individu_j = self.population[j]
                        #print("Individu numero ", i, " :  \n", individu_i)
                        #i_vx, i_vy, j_vx, j_vy = physique.collision_particule(individu_i,individu_j)
                        individu_i.touch = individu_j
                        individu_j.touch = individu_i

    def predict(self, individu): #depend de comment l'interface graphique interprete la matrice (ne pas suppr)
        """renvoie les prochaines coordonnees ou donne a l'individu l'obstacle qu'il rencontre (peut etre amelioree)"""
        x,y,r = individu.x + individu.vx * self.time_increment, individu.y + individu.vy * self.time_increment, individu.rayon
        if x-r < 0 and 0 <= y-r <= y+r <= self.y_max :
            individu.touch =  "left_wall"
        elif x+r > self.x_max and 0 <= y-r <= y+r <= self.y_max :
            individu.touch = "right_wall"
        elif 0 <= x-r <= x+r <= self.x_max and y-r < 0  :
            individu.touch = "up_wall"
        elif 0 <= x-r <= x+r <= self.x_max and y+r > self.y_max :
            individu.touch = "down_wall"
        elif x-r < 0 and y-r < 0 :
            individu.touch = "up-left_corner"
        elif x+r > self.x_max and y-r < 0 :
            individu.touch = "up-right_corner"
        elif x-r < 0 and y+r > self.y_max :
            individu.touch = "down-right_corner"
        elif x+r > self.x_max and y+r > self.y_max :
            individu.touch = "down-left_corner"
        else :
            return (x,y,r)


    def prediction_is_valid(self,individu): 
        """Teste si la prédiction sort ou non l'individu des limites de la simulation (plus courte que predict_for_all)"""
        r = individu.rayon

        x,y,r = individu.x + individu.vx * self.time_increment, individu.y + individu.vy * self.time_increment, individu.rayon

        return  (0 <= x-r < x+r <= self.x_max) and  (0 <= y-r < y+r <= self.y_max)


    def advance(self):
        
        self.predict_for_all()
        for individu in self.population :
            individu.move(self.x_max,self.y_max,self.time_increment)
        self.time += self.time_increment
        print("LE TEMPS : ", self.time)

    def change_speed(self,var): #change la vitesse de réalisation de la simulation 
        """ Change la vitesse de réalisation de la simulation """
        if self.time_increment - var > 0 :
            self.time_increment += var

    def generation(self,rayon,nb_particule):

        np.random.seed()
        x_particules = nb_particule // 2
        y_particules = nb_particule - x_particules
        pas_x = int(self.x_max / (2 * x_particules))
        pas_y = int(self.y_max / (2 * y_particules))
        x_array = [0] * nb_particule
        y_array = [0] * nb_particule
        try:
            for k,i in enumerate(range(0,self.x_max,pas_x)):
                x_array[k] = alg.uniform(i+rayon,i + pas_x - rayon -1)
            for k,j in enumerate(range(0,self.y_max, pas_y)):
                y_array[k] = alg.uniform(j+rayon,j+pas_y -rayon -1)
        except:
            pass
        for i in range(nb_particule):
            x = int(alg.uniform(0,nb_particule-i))
            y = int(alg.uniform(0,nb_particule-i))
            self.population.append(Individu(rayon,x_array[x],y_array[y],alg.uniform(-2,2),alg.uniform(-2,2),self))
            x_array.pop(x)
            y_array.pop(y)


def collision(cercle1,cercle2):

    rayon_1 = cercle1[2]
    rayon_2 = cercle2[2]
    if alg.distance(cercle1,cercle2) < rayon_1 + rayon_2 :
        return True
    else:
        return False


    