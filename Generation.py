import individu
import numpy as np
from math import sqrt






def gen(longueur,hauteur,n):#Génération aléatoire des individus 
	
	population = [0]*n
	
	x_array = [0]*n
	
	y_array = [0]*n
	
	#Pour éviter les chevauchements lors de la génération avec contrainte d'un individu par incrément de Y
	
	radius_prime = radius
		
	sub = longueur//radius
		
	i = 0
		
	while sub < longueur and i < n :
		
		i += 1
		
		x_array[i] = np.random.uniform(radius_prime,hauteur)
		
		y_array[i] = np.random.uniform(radius,radius+sub)
		
		radius += sub
	
	velocity_array_x = np.random.uniform(-max(longueur,hauteur)/100,max(longueur,hauteur)/100,n)
	
	velocity_array_y = np.random.uniform(-max(longueur,hauteur)/100,max(longueur,hauteur)/100,n)

	
	for i in range(n):
		
		population[i] = Individu(x_array[i],y_array[i],velocity_array[i])

		population[i].set_vitesse(velocity_array_x[i],velocity_array_y[i])

	return population
