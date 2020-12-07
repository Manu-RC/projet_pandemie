#




def maladie_Basic(population,Taux_contagion,Durée_transmissibilité):
	S =len(population)
	
	I = 0

	R = 0

	for individu in population :
		
		if individu.collision != None :
			
			Restate(individu)



		

















def Restate(individu):
	 
	 

	if individu.etat == "Saint" and individu.collision.etat == "Infécté" :
	 	
		State = np.random.binomial(1,Taux_contagion,1)[0]
	 	
		if State == 1 : 

			individu.etat = "Infécté"

			individu.hit_time = Simulation.time
	 	
	 		S -= 1

	 		I += 1


	if individu.etat == "Saint" and individu.collision.etat == "Rétabli" :#Durée de la période de contagion dans l'attribut collision

	 	State = np.random.binomial(1,Taux_contagion,1)[0]

	 	hit_timeframe = Simulation.time - individu.collision.hit_time

	 	if State == 1 and hit_timeframe <= Durée_transmissibilité and hit_timeframe != Simulation.time :


	 		individu.etat = "Infécté"

	 		individu.hit_time = Simulation.time

	 		S-=1

	 		I +=1


	if individu.etat == "Infécté" and hit_timeframe > Durée_transmissibilité :

			individu.etat = "Rétabli"

			individu.hit_time = 0

			R +=1

			I-=1

	if (individu.etat == "Rétabli" and individu.hit_time == 0) and (individu.collision.etat == "Infécté" or (individu.collision.etat == "Rétabli" and hit_timeframe < Durée_transmissibilité and hit_timeframe != Simulation.time)) :

		individu.hit_time = Simulation.time