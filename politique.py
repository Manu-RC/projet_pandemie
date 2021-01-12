from individu import Individu

def isolement(simulation):

    for individu in simulation.population:
        if individu.etat != "Infecte":
            individu.move(simulation.x_max,simulation.y_max)
    simulation.time += simulation.time_increment

def couvre_feu(simulation):

    if (simulation.time % 10) < 1:
        for individu in simulation.population:
            individu.move(simulation.x_max,simulation.y_max)
    simulation.time += simulation.time_increment

def pas_de_politique(simulation):

    for individu in simulation.population :
        individu.move(simulation.x_max,simulation.y_max)
    simulation.time += simulation.time_increment



            