import numpy as np
from individu import Individu
import physique
import algebre as alg
from Maladie import Maladie
import politique


class Simulation :
    """ Cette classe permet la génération des différentes particules, gère les collisions entre les particules
        et les bords du domaines ; ainsi que l'avancement dans le temps de la simulation. """

    def __init__(self,x_max,y_max,maladie_init,politique=None):
        
        #maladie initialisée pour un certain nombre d'individus au départ
        self.maladie_init = maladie_init
        #dimensions de l'environnement
        self.x_max = x_max
        self.y_max = y_max
        self.population = []
        #horloge de la simulation 
        self.time = 0
        #pas de temps de la simulation
        self.time_increment = 0.1
        self.morts = 0
        self.sains = 0
        self.infectes = 0
        self.immunises = 0
        self.pourcentage_contamines= None
        #historique de la simulation pour les courbes du graphe
        self.historique = []   # de la forme [temps ,sains,infectes,morts]
        self.politique = politique


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
        pred = individu.next_position()
        x,y,r = pred[0],pred[1],individu.rayon
        if x-r < 0 and 0 <= y-r <= y+r <= self.y_max:
            individu.touch =  "left_wall"
        elif x+r > self.x_max and 0 <= y-r <= y+r <= self.y_max:
            individu.touch = "right_wall"
        elif 0 <= x-r <= x+r <= self.x_max and y-r < 0:
            individu.touch = "up_wall"
        elif 0 <= x-r <= x+r <= self.x_max and y+r > self.y_max:
            individu.touch = "down_wall"
        elif x-r < 0 and y-r < 0:
            individu.touch = "up-left_corner"
        elif x+r > self.x_max and y-r < 0:
            individu.touch = "up-right_corner"
        elif x-r < 0 and y+r > self.y_max:
            individu.touch = "down-right_corner"
        elif x+r > self.x_max and y+r > self.y_max:
            individu.touch = "down-left_corner"
        else :
            return (x,y,r)

    def prediction_is_valid(self,individu):
        """Teste si la prédiction sort ou non l'individu des limites de la simulation (plus courte que predict_for_all)"""
        r = individu.rayon
        x,y,r = individu.x + individu.vx * self.time_increment, individu.y + individu.vy * self.time_increment, individu.rayon
        return  (0 <= x-r < x+r <= self.x_max) and  (0 <= y-r < y+r <= self.y_max)


    def advance(self):
        """avance la simulation:prédit les collisions,update les états,applique la politique en vigueur"""
        self.predict_for_all()
        self.Restate_for_all()
        if self.politique=="isolement":
            politique.isolement(self) #la simulation avance selon les regles de l'isolement cf politique.py
        elif self.politique=="couvre-feu":
            politique.couvre_feu(self)
        else:
            politique.pas_de_politique(self)
        self.historique += [self.time,self.sains,self.infectes,self.immunises,self.morts]

    def change_speed(self,var): #change la vitesse de réalisation de la simulation 
        """ Change la vitesse de réalisation de la simulation """
        self.time_increment *= var

    def generation(self,rayon,nb_particule,nombre_contamines):

        np.random.seed()
        x_particules = nb_particule // 2
        y_particules = nb_particule - x_particules
        pas_x = int(self.x_max / (2 * x_particules))
        pas_y = int(self.y_max / (2 * y_particules))
        x_array = [0] * nb_particule
        y_array = [0] * nb_particule
        k = 0
        while k < nb_particule:
            x_array[k] = alg.uniform(k * pas_x + rayon, (k+1)*pas_x - rayon)
            y_array[k] = alg.uniform(k * pas_y + rayon, (k+1)*pas_y - rayon)
            k += 1
        for i in range(nb_particule):
            if i < nombre_contamines:
                x = int(alg.uniform(0,nb_particule-i))
                y = int(alg.uniform(0,nb_particule-i))
                individu = Individu(rayon,x_array[x],y_array[y],alg.uniform(-2,2),alg.uniform(-2,2),self,self.maladie_init)
                individu.etat = "Infecte"
                self.population.append(individu)
                x_array.pop(x)
                y_array.pop(y)
            else:
                x = int(alg.uniform(0,nb_particule-i))
                y = int(alg.uniform(0,nb_particule-i))
                self.population.append(Individu(rayon,x_array[x],y_array[y],alg.uniform(-2,2),alg.uniform(-2,2),self))
                x_array.pop(x)
                y_array.pop(y)
        self.infectes = nombre_contamines
        self.sains = len(self.population)-self.infectes-self.immunises


        
    def Restate_for_all(self):
        
        for individu in self.population:
            if type(individu.touch) != str and individu.touch is not None :
                self.Restate(individu)
            elif individu.touch is None :
                if individu.etat == "Infecte" and (self.time - individu.maladie.hit_time) > individu.maladie.Duree_transmissibilite :
                    individu.etat = "Immunise"
                    individu.hit_time = 0
                    self.immunises +=1
                    self.infectes-=1

    def Restate(self,individu):
        
        if individu.etat == "Sain" and individu.touch.etat == "Infecte" :
            State = np.random.binomial(1,individu.touch.maladie.Taux_contagion)
            if State == 1 :
                maladie = individu.touch.maladie
                individu.maladie = Maladie(self.time,maladie.Taux_contagion,maladie.Taux_mutation,maladie.Duree_transmissibilite)
                individu.etat = "Infecte"
                self.sains -= 1
                self.infectes += 1

	    # if individu.etat == "Sain" and individu.collision.etat == "Rétabli" :#Durée de la période de contagion dans l'attribut collision
		#     State = np.random.binomial(1,individu.Maladie.Taux_contagion)
		#     hit_timeframe = individu.simulation.time - individu.collision.Maladie.hit_time
		
		#     if State == 1 and hit_timeframe <= individu.Maladie.Durée_transmissibilité and hit_timeframe != individu.simulation.time :
        #         individu.etat = "Infécté"
        #         individu.hit_time = Simulation.time
        #         self.sains-=1
        #         self.infectes +=1
        elif individu.etat == "Infecte" and (self.time - individu.maladie.hit_time) > individu.maladie.Duree_transmissibilite :
            individu.etat = "Immunise"
            individu.hit_time = 0
            self.immunises +=1
            self.sains +=1
            self.infectes-=1

	    # if (individu.etat == "Rétabli" and individu.Maladie.hit_time == 0) and (individu.collision.etat == "Infécté" or (individu.collision.etat == "Rétabli" and hit_timeframe < individu.Maladie.Durée_transmissibilité and hit_timeframe != Simulation.time)) :
        #     individu.Maladie.hit_time = Simulation.time

def collision(cercle1,cercle2):

    rayon_1 = cercle1[2]
    rayon_2 = cercle2[2]
    if alg.distance(cercle1,cercle2) < (rayon_1 + rayon_2) :
        return True
    else:
        return False


    