import numpy as np

class Maladie:

	def __init__(self,hit_time,Taux_contagion,Taux_mutation,Duree_transmissibilite,lethalite):

		self.hit_time = hit_time
		self.Taux_contagion = Taux_contagion
		self.Taux_mutation = Taux_mutation
		self.Duree_transmissibilite = Duree_transmissibilite
		self.lethalite = lethalite
	
	def mutate(self):
		State=np.random.binomial(1,Taux_mutation)
		if State == 1:
			self.Duree_transmissibilite += 0.1*Duree_transmissibilite
			self.Taux_mutation -= 0.5*Taux_mutation











