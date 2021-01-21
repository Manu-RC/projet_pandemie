from individu import Individu

def isolement(simulation):
    for individu in simulation.population:
        if individu.etat == "Infecte":
            individu.move_isolement(simulation.x_max, simulation.y_max)
        elif individu.etat == "Immunise":
            individu.move_reinit(simulation.x_max, simulation.y_max, simulation.borne_vitesse_init)
        else:
            individu.move(simulation.x_max, simulation.y_max)
    simulation.time += simulation.time_increment

def couvre_feu(simulation):
    if (simulation.time % 24) > 18:
        for individu in simulation.population:
            individu.move_couvre_feu(simulation.x_max, simulation.y_max)
    else:
        for individu in simulation.population:
            if individu.vx == 0 and individu.vy == 0:
                individu.move_reinit(simulation.x_max, simulation.y_max,simulation.borne_vitesse_init)
            else:
                individu.move(simulation.x_max, simulation.y_max)
    simulation.time += simulation.time_increment

def pas_de_politique(simulation):
    for individu in simulation.population:
        individu.move(simulation.x_max, simulation.y_max)
    simulation.time += simulation.time_increment