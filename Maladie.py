import numpy as np

def gaussienne(facteur):
	proba = 0.1*np.random.randn()+facteur #on recentre la loi normale
	if proba > 1 :return facteur
	return proba



class Maladie:

	def __init__(self,hit_time,Taux_contagion,Taux_mutation,Duree_transmissibilite,lethalite):
		self.hit_time = hit_time
		self.Taux_contagion = Taux_contagion
		self.Taux_mutation = Taux_mutation
		self.Duree_transmissibilite = Duree_transmissibilite
		self.lethalite = lethalite
	
	def mutate(self):
		state=np.random.binomial(1,self.Taux_mutation)
		if state == 1:
			self.Duree_transmissibilite += 0.1 * self.Duree_transmissibilite
			self.Taux_mutation -= 0.5 * self.Taux_mutation











