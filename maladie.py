import algebre as alg

class Maladie:

	def __init__(self,hit_time,taux_contagion,taux_mutation,duree_transmissibilite,letalite):
		"""Classe où sont stockés les parametres de la maladie"""


		self.hit_time = hit_time                                #le temps où l'individu a été infécté
		self.taux_contagion = taux_contagion					#Le taux de contagion de la maladie transmise
		self.taux_mutation = taux_mutation						#Le taux de contagion de la maladie transmise
		self.duree_transmissibilite = duree_transmissibilite	#la durée où le virus est contagieux
		self.letalite = letalite								# c'est un taux, ajuste la probabilité de mourir de la maladie
		self.date_retablissement = self.hit_time + self.duree_transmissibilite

	def mutate(self):
		"""Fait muter la maladie"""
		state = alg.binomiale(self.taux_mutation)
		if state == 1: #la maladie va muter
			self.duree_transmissibilite += 0.5 * self.duree_transmissibilite
			self.taux_mutation -= 0.5 * self.taux_mutation

	def decide_fate(self,individu):
		"""Décide en fonction de la létalité si un individu doit mourir ou non lors de son temps passé malade"""
		state = alg.binomiale(alg.gaussienne(self.letalite))
		if state == 1 : #l'individu doit mourir
			# on tire au hasard une date entre le moment ou il devient malade et le moment théorique ou il doit guérir
			individu.date_deces = alg.uniform(self.hit_time,self.date_retablissement) 













