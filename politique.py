from individu import Individu

def confinement(simulation):

    for individu in simulation.population:
        if individu.etat != "Infecte":
            individu.move(simulation.x_max,simulation.y_max)




            