import math
import numpy as np
from individu import Individu

class Simulation : 

    def __init__(self,maladie,x_max,y_max):

        #dimensions de l'environnement
        self.x_max = x_max
        self.y_max = y_max
        
        self.population = []

        self.maladie = maladie
        
        #horloge de la simulation 
        self.time = 0
        
        #pas de temps de la simulation
        self.time_increment = 1

        

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

                        individu_i.collision = individu_j
                        individu_j.collision = individu_i

    def predict(self, individu): #depend de comment l'interface graphique interprete la matrice (ne pas suppr)
        """renvoie les prochaines coordonnees ou donne a l'individu l'obstacle qu'il rencontre (peut etre amelioree)"""

        x,y,r = individu.x + individu.vx , individu.y + individu.vy , individu.rayon
    
        if x-r < 0 and 0 <= y-r <= y+r <= self.y_max : 

            individu.touch =  "left wall" 

        elif x+r > self.x_max and 0 <= y-r <= y+r <= self.y_max : 

            individu.touch = "right wall"

        elif 0 <= x-r <= x+r <= self.x_max and y-r < 0  :

            individu.touch = "up wall"

        elif 0 <= x-r <= x+r <= self.x_max and y+r > self.y_max :

            individu.touch = "down wall"

        elif x-r < 0 and y-r < 0 : 

            individu.touch = "up-left corner"

        elif x+r > self.x_max and y-r < 0 : 

            individu.touch = "up-right corner"

        elif x-r < 0 and y+r > self.y_max : 

            individu.touch = "down-right corner"

        elif x+r > self.x_max and y+r > self.y_max : 

            individu.touch = "down-left corner"

        else :
            return (x,y,r)

    
    def advance(self):
        
        self.predict_for_all()
        for individu in self.population : 

            individu.move(self.time_increment)    #depend du nom de la fonction qui fait mouvoir un individu 

        self.time += self.time_increment


    def change_speed(self,var): #change la vitesse de réalisation de la simulation 

        if self.time_increment - var > 0 :

            self.time_increment += var

    def gen(self,n,radius):#Génération aléatoire des individus 
    
    
        x_array = [0]*n
    
        y_array = [0]*n
    
    #Pour éviter les chevauchements lors de la génération avec contrainte d'un individu par incrément de Y
    
        radius_prime = radius
        
        sub = self.x_max//radius
        
        i = 0
        
        while sub < self.x_max and i < n :
        
            
        
            x_array[i] = np.random.uniform(radius_prime,self.y_max)
        
            y_array[i] = np.random.uniform(radius,radius+sub)
        
            radius += sub

            i += 1
    
        velocity_array_x = np.random.uniform(-max(self.x_max,self.y_max)/100,max(self.x_max,self.y_max)/100,n) #Liste vecteurs vitesse
    
        velocity_array_y = np.random.uniform(-max(self.x_max,self.y_max)/100,max(self.x_max,self.y_max)/100,n)

    
        for i in range(n):
        
            self.population.append(Individu(radius_prime,x_array[i],y_array[i],velocity_array_x[i],velocity_array_y[i]))


    













def distance(v_1,v_2):

    return math.sqrt( (v_1[0]-v_2[0])**2 + (v_1[1]-v_2[1])**2 )
    
def collision(v_1,v_2):

    rayon_1 = v_1[2]
    rayon_2 = v_2[2]

    if distance(v_1,v_2) < rayon_1+rayon_2 :

        return True

    else:

        return False


    