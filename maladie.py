import algebre as alg

class Maladie:

	def __init__(self,hit_time,taux_contagion,taux_mutation,duree_transmissibilite,letalite):
		"""Classe où sont stockés les parametres de la maladie
		letalite : c'est un taux, c'est la probabilité de mourir de la maladie
		contagion : probabilité de transmettre le virus en cas de contact avec un autre individu
		mutation :  ...
		"""


		self.hit_time = hit_time                                #le temps où l'individu a été infécté
		self.taux_contagion = taux_contagion					#Le taux de contagion de la maladie transmise
		self.taux_mutation = taux_mutation						#Le taux de contagion de la maladie transmise
		self.duree_transmissibilite = duree_transmissibilite	#la durée où le virus est contagieux
		self.letalite = letalite								#la létalité du virus 
	
	def mutate(self):
		state = alg.binomiale(self.taux_mutation)
		if state == 1:
			self.duree_transmissibilite += 0.5 * self.duree_transmissibilite
			self.taux_mutation -= 0.5 * self.taux_mutation













