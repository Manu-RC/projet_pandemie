from individu import Individu

def isolement(simulation):
    """Réduit fortement les mouvements des individus contaminés"""
    for individu in simulation.population:
        if individu.etat == "Infecte":
            individu.move_isolement(simulation.x_max, simulation.y_max)
        elif individu.etat == "Immunise":
            # Redemarre l'individu qui est arreter depuis 
            individu.move_reinit(simulation.x_max, simulation.y_max, simulation.borne_vitesse_init)
        else:
            individu.move(simulation.x_max, simulation.y_max)
    simulation.time += simulation.time_increment

def couvre_feu(simulation): 
    """Impose un couvre-feu entre 18h et 6h :) """
    if 6 <=(simulation.time % 24) >= 18:
        for individu in simulation.population:
            individu.move_couvre_feu(simulation.x_max, simulation.y_max)
    else:
        # Quand le couvre-feu est fini, il faut redemarrer toutes les individu à l'arret ! 
        # Si on ne le fait pas, les individu ne bougeront plus vu que seul la vitesse à l'intant t est connu et non aux t-1,t-2...
        for individu in simulation.population:
            if individu.vx == 0 and individu.vy == 0:
                individu.move_reinit(simulation.x_max, simulation.y_max,simulation.borne_vitesse_init)
            else:
                individu.move(simulation.x_max, simulation.y_max)
    simulation.time += simulation.time_increment

def pas_de_politique(simulation):
    """C'est la liberté"""
    for individu in simulation.population:
        individu.move(simulation.x_max, simulation.y_max)
    simulation.time += simulation.time_increment