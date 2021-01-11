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




#kill dans simulation
if individu.etat == "Infecte" and (self.time - individu.maladie.hit_time) == individu.maladie.Duree_transmissibilite//2 : #complixation du covid apparaissent 6 jours aprés l'infection
	State= np.random.binomial(1,individu.maladie.lethalite)#lethalité entre 0.1% et 1% 
	if State ==1 :
		self.morts +=1
		self.infectes -=1
		self.population.pop(individu)







