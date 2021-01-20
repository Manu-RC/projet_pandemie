import tkinter
import main

def lancement():
    longueur = axe_x.get()
    largeur = axe_y.get()
    population = population_totale.get()
    population_malade = population_contamine.get()
    vitesse_borne_init = vitesse_init.get()
    taux_rules_respect = rules_respect.get()
    hit_time_init = hit_time.get()
    taux_contagion_init = taux_contagion.get()
    mutation_init = mutation.get()
    letalite_init = letalite.get()
    duree_transmisibilite_init = duree_transmisibilite.get()
    main.main(longueur,largeur,population,population_malade,vitesse_borne_init,taux_rules_respect,hit_time_init,taux_contagion_init,mutation_init,duree_transmisibilite_init,letalite_init)

def my_scale(fenetre, label=None, from_=None, to=None, resolution=None, length=None, variable=None, font=None, fg=None, bg=None, command=None, side=None):

    scale =  tkinter.Scale(fenetre, orient='horizontal', from_=from_, to=to, resolution=resolution, length=length, label=label, variable=variable, font=font, fg=fg, bg=bg, command=command)
    scale.pack(side=side)

def my_frame(fenetre, background=None, bordure=None, relief=None,expand=None,side=None,fill=None):
    frame = tkinter.Frame(fenetre, bg=background, bd=bordure, relief=relief)
    frame.pack(expand=expand, fill=fill, side=side)
    return frame

def my_label(fenetre,text=None,font=None,bg=None, fg=None, expand=None, side=None, fill=None):
    label = tkinter.Label(fenetre, text=text, font=font,bg=bg,fg=fg)
    label.pack(expand=expand,side=side,fill=fill)
    return label

def update_population_tot(*args):
    population_totale.set(population_totale.get())

def update_population_mal(*args):
    population_contamine.set(population_contamine.get())

def update_hit_time(*args):
    hit_time.set(hit_time.get())

def update_taux_contagion(*args):
    taux_contagion.set(taux_contagion.get())

def update_mutation(*args):
    mutation.set(mutation.get())

def update_duree_transmisibilite(*args):
    duree_transmisibilite.set(duree_transmisibilite.get())

def update_letalite(*args):
    letalite.set(letalite.get())

def update_x(*args):
    axe_x.set(axe_x.get())

def update_y(*args):
    axe_y.set(axe_y.get())

def update_borne_vitesse(*args):
    vitesse_init.set(vitesse_init.get())

def update_rules_respect(*args):
    rules_respect.set(rules_respect.get())

# Création de la fenêtre
menu_principal = tkinter.Tk()
menu_principal.title("Simulateur de pendémie")
menu_principal.geometry("1080x720")
menu_principal.minsize(1000,800)
menu_principal.iconbitmap("logo_projet.ico") #pour mettre une icone
menu_principal.config(background='#E9F273')

image = tkinter.PhotoImage(file="logo_projet.png").zoom(50).subsample(50)
canvas = tkinter.Canvas(menu_principal, width=150, height=150, bg="#E9F273", bd=0, highlightthickness=0)
canvas.create_image(100, 100, image=image)
canvas.pack(expand="YES", fill="y", side="top")

# Creation du titre principal
titre_principal = "Simulateur de propagation de maladie"
bg_titre = "#E9F273"
fg_titre = "black"
size_titre   = 30
police_titre = "arial"
font_titre_principal = (police_titre,size_titre)
expand_titre = "YES"

label_title = tkinter.Label(menu_principal,text=titre_principal, font=font_titre_principal, bg=bg_titre, fg=fg_titre)
label_title.pack(expand=expand_titre)

# creation des Frames
bg_frame =  "#E9F273"
bd_frame = 5
relief_frame = "groove"
expand_frame = "TRUE"

frame_pop     = tkinter.Frame(menu_principal, bg=bg_frame, bd=bd_frame, relief=relief_frame)
frame_pop.pack(expand=expand_frame)
frame_lancer  = tkinter.Frame(menu_principal, bg=bg_frame, bd=bd_frame, relief=relief_frame)
frame_lancer.pack(expand=expand_frame, side="right", fill="x")
frame_domaine = tkinter.Frame(menu_principal, bg=bg_frame, bd=bd_frame, relief=relief_frame)
frame_domaine.pack(side="right", fill="y")
frame_maladie = tkinter.Frame(menu_principal, bg=bg_frame, bd=bd_frame, relief=relief_frame)
frame_maladie.pack(side="left", fill="y")

# Parametre des sous titre
size_st = 20
police_st = "arial"
font_st = (police_st,size_st)
bg_st = "#E9F273"
fg_st = "black"
# Parametrage supplémentaire sur les different sous titre
titre_domaine = "Choix du domaine"
titre_pop = "Paramètres sur la population"
titre_maladie = "Paramètre sur la maladie"
titre_lancer = "Démarrer la simulation"
expand_pop_titre = "YES"
expand_maladie_titre = "YES"
side_lancer = "left"

label_domaine    = tkinter.Label(frame_domaine, text=titre_domaine, font=font_st, bg=bg_st, fg=fg_st)
label_domaine.pack()
label_population = tkinter.Label(frame_pop, text=titre_pop, font=font_st, bg=bg_st, fg=fg_st)
label_population.pack(expand=expand_pop_titre)
label_maladie    = tkinter.Label(frame_maladie, text=titre_maladie, font=font_st, bg=bg_st, fg=fg_st)
label_maladie.pack(expand=expand_maladie_titre)
label_lancer     = tkinter.Label(frame_lancer, text=titre_lancer, font=font_st, bg=bg_st, fg=fg_st)
label_lancer.pack(side=side_lancer)

#Valeur initiales des variables de controle
valeur_init_domaine = 550
valeur_init_pop_totale = 90
valeur_init_pop_contamine = 30
valeur_init_vitesse = 2
valeur_rules_respect_init = 0.95
valeur_init_hit_time = 0
valeur_init_taux_contagion = 0.5
valeur_init_mutation = 0.1
valeur_init_duree_transmissibilite = 200
valeur_init_letalite = 0.1


# Création des variables de controles
axe_x = tkinter.IntVar()
axe_x.trace("w",update_x)
axe_x.set(valeur_init_domaine)

axe_y = tkinter.IntVar()
axe_y.trace("w", update_y)
axe_y.set(valeur_init_domaine)

population_totale = tkinter.IntVar()
population_totale.trace("w",update_population_tot)
population_totale.set(valeur_init_pop_totale)

population_contamine = tkinter.IntVar()
population_contamine.trace("w",update_population_mal)
population_contamine.set(valeur_init_pop_contamine)

vitesse_init = tkinter.DoubleVar()
vitesse_init.trace("w",update_borne_vitesse)
vitesse_init.set(valeur_init_vitesse)

rules_respect = tkinter.DoubleVar()
rules_respect.trace("w",update_rules_respect)
rules_respect.set(valeur_rules_respect_init)

hit_time = tkinter.DoubleVar()
hit_time.trace("w",update_hit_time)
hit_time.set(valeur_init_hit_time)

taux_contagion = tkinter.DoubleVar()
taux_contagion.trace("w",update_taux_contagion)
taux_contagion.set(valeur_init_taux_contagion)

mutation = tkinter.DoubleVar()
mutation.trace("w",update_mutation)
mutation.set(valeur_init_mutation)

duree_transmisibilite = tkinter.IntVar()
duree_transmisibilite.trace("w",update_duree_transmisibilite)
duree_transmisibilite.set(valeur_init_duree_transmissibilite)

letalite = tkinter.DoubleVar()
letalite.trace("w",update_letalite)
letalite.set(valeur_init_letalite)

# Creation des differents curseurs de l'application
#Variable communes
fg_scale = "black"
bg_scale = '#AF000C'
resolution_taux = 0.01
resolution_int = 1
debut_valeur_taux = 0
fin_valeur_taux = 1

# Le domaine
titre_axe_domaine_x = "Axe des x"
titre_axe_domaine_y = "Axe des y"
police_axe_dom = "arial"
size_police_axe_dom = 20
font_axe_dom = (police_axe_dom,size_police_axe_dom)
debut_axe_dom = 300
fin_axe_dom   = 600
length_axe_dom  = 200

axe_x_entree = tkinter.Scale(frame_domaine, orient='horizontal', label=titre_axe_domaine_x, from_=debut_axe_dom, to_=fin_axe_dom, resolution=resolution_int, length=length_axe_dom, variable=axe_x, font=font_axe_dom, fg=fg_scale, bg=bg_scale, command=update_x(axe_x))
axe_y_entree = tkinter.Scale(frame_domaine, orient='horizontal', label=titre_axe_domaine_y, from_=debut_axe_dom, to_=fin_axe_dom, resolution=resolution_int, length=length_axe_dom, variable=axe_y, font=font_axe_dom, fg=fg_scale, bg=bg_scale, command=update_y(axe_y))
axe_x_entree.pack()
axe_y_entree.pack()

# La population
titre_pop_totale = "population totale"
titre_pop_contaminee = "population contaminée"
titre_vitesse = "Borne vitesse"
titre_respect = "Respect du confinement"
length_axe_pop = 250
size_police_pop = 15
police_pop = "arial"
font_pop = (police_pop,size_police_pop)
resolution_vitesse = 0.1
side_pop_global = "left"
side_pop_locale = "right"
debut_axe_pop_tot = 50
fin_axe_pop_tot = 100
debut_axe_pop_sick = 2
fin_axe_pop_sick = 48
debut_axe_vitesse = 0
fin_axe_vitesse = 2.5

pop_entry = tkinter.Scale(frame_pop, orient='horizontal', label=titre_pop_totale,from_=debut_axe_pop_tot, to_=fin_axe_pop_tot, resolution=resolution_int, length=length_axe_pop, variable=population_totale, font=font_pop, fg=fg_scale, bg=bg_scale, command=update_population_tot(population_totale))
pop_sick_entry = tkinter.Scale(frame_pop, orient='horizontal', label=titre_pop_totale, from_=debut_axe_pop_sick, to_=fin_axe_pop_sick, resolution=resolution_int, length=length_axe_pop, variable=population_contamine, font=font_pop, fg=fg_scale, bg=bg_scale, command=update_population_mal(population_contamine))
vitesse_init_entry = tkinter.Scale(frame_pop, orient='horizontal', label=titre_vitesse, from_=debut_axe_vitesse, to_=fin_axe_vitesse, resolution=resolution_int, length=length_axe_pop, variable=vitesse_init, font=font_pop, fg=fg_scale, bg=bg_scale, commande=update_borne_vitesse(vitesse_init))
rules_respect_entry = tkinter.Scale(frame_pop, orient='horizontal', label=titre_respect, from_=debut_valeur_taux, to_=fin_valeur_taux, resolution=resolution_taux, length=length_axe_pop, variable=rules_respect,font=font_pop, fg=fg_scale, bg=bg_scale, command=update_rules_respect(rules_respect))
pop_entry.pack(side=side_pop_global)
pop_sick_entry.pack(side=side_pop_global)
vitesse_init_entry.pack(side=side_pop_locale)
rules_respect_entry.pack(side=side_pop_locale)

#La maladie maladie
titre_hit_time = "hit time"
titre_contagion = "taux de contagion"
titre_mutation = "taux de mutation"
titre_duree_trans = "durée de transmissibilité"
titre_letalite = "taux de letalite"
length_maladie = 200
size_police_maladie = 10
police_maladie = "arial"
font_maladie = (police_maladie, size_police_maladie)
debut_axe_hit_time = 0
fin_axe_hit_time = 5
debut_axe_duree_trans = 0
fin_axe_duree_trans = 200

hit_time_entry = tkinter.Scale(frame_maladie, orient='horizontal', from_=debut_axe_hit_time, to=fin_axe_hit_time, resolution=resolution_int, length=length_maladie, label=titre_hit_time,
                                   variable=hit_time, font=font_maladie, fg=fg_scale, bg=bg_scale, command=update_hit_time(hit_time))
hit_time_entry.pack()
taux_contagion_entry = tkinter.Scale(frame_maladie, orient='horizontal', from_=debut_valeur_taux, to=fin_valeur_taux, resolution=resolution_taux, length=length_maladie, label=titre_contagion,
                                         variable=taux_contagion, font=font_maladie,fg=fg_scale, bg=bg_scale, command=update_taux_contagion(taux_contagion))
taux_contagion_entry.pack()
mutation_entry =  tkinter.Scale(frame_maladie, orient='horizontal', label=titre_mutation, from_=debut_valeur_taux, to_=fin_valeur_taux, resolution=resolution_taux, length=length_maladie, variable=mutation,
                                    font=font_maladie, fg=fg_scale, bg=bg_scale, command=update_mutation(mutation))
mutation_entry.pack()
duree_transmisibilite_entry = tkinter.Scale(frame_maladie, orient='horizontal', label=titre_duree_trans, from_=debut_axe_duree_trans, to_=fin_axe_duree_trans, resolution=resolution_int, length=length_maladie,
                                                variable=duree_transmisibilite, font=font_maladie, fg=fg_scale, bg=bg_scale, command=update_duree_transmisibilite(duree_transmisibilite))
duree_transmisibilite_entry.pack()
letalite_entry = tkinter.Scale(frame_maladie,orient='horizontal', label=titre_letalite, from_=debut_valeur_taux, to_=fin_valeur_taux, resolution=resolution_taux, length=length_maladie,
                                   variable=letalite, font=font_maladie, fg=fg_scale, bg=bg_scale, command=update_letalite(letalite))
letalite_entry.pack()
#Le bouton lancer
lancer_button = tkinter.Button(frame_lancer,text="LANCER",font=("arial",25), bg='#AF000C', fg='black',command=lancement)
lancer_button.pack(pady=25, fill="x")
lancer_button.pack()

menu_principal.mainloop()
