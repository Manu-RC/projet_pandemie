import numpy as np

def gaussienne(facteur):#loi de proba gaussienne autour du facteur souhaité en restant dans l'intervalle [0.1]
	proba = 0.1*np.random.randn()+facteur #on recentre la loi normale
	if proba > 1 :return facteur
	return proba



class Maladie:#la classe où sont stockés tous les parametres de la maladie

	def __init__(self,hit_time,Taux_contagion,Taux_mutation,Duree_transmissibilite,lethalite):

		self.hit_time = hit_time                                #le temps où l'individu a été infécté
		self.Taux_contagion = Taux_contagion					#Le taux de contagion de la maladie transmise
		self.Taux_mutation = Taux_mutation						#Le taux de contagion de la maladie transmise
		self.Duree_transmissibilite = Duree_transmissibilite	#la durée où le virus est contagieux
		self.lethalite = lethalite								#la létalité du virus 
	
	def mutate(self):
		State=np.random.binomial(1,self.Taux_mutation)
		if State == 1:
			self.Duree_transmissibilite += 0.5*self.Duree_transmissibilite
			self.Taux_mutation -= 0.5*self.Taux_mutation











