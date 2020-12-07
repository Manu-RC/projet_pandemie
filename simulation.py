import math

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
    
        for i in range(n):
            for j in range(i,n): #les individus avant i ont deja ete traites

                if predictions[i] is not None and predictions[j] is not None :
                    if collision(predictions[i],predictions[j]): 
                        #on donne a chaque individu l'individu avec qui il va entrer en collision
                        individu_i = self.population[i]
                        individu_j = self.population[i]

                        individu_i.collision = individu_j
                        individu_j.collision = individu_i

    def predict(self, individu): #depend de comment l'interface graphique interprete la matrice (ne pas suppr)
        """renvoie les prochaines coordonnees ou donne a l'individu l'obstacle qu'il rencontre (peut etre amelioree)"""

        x,y,r = individu.x + individu.v_x , individu.y + individu.y , individu.r
    
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


def distance(v_1,v_2):

    return math.sqrt( (v_1[0]-v_2[0])**2 + (v_1[1]-v_2[1])**2 )
    
def collision(v_1,v_2):

    rayon_1 = v_1[2]
    rayon_2 = v_2[2]

    if distance(v_1,v_2) < rayon_1+rayon_2 :

        return True

    else:

        return False


    