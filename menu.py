import tkinter
import main

def update_label(*args):
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

def lancement():
    longueur = axe_x.get()
    largeur = axe_y.get()
    population = population_totale.get()
    population_malade = population_contamine.get()
    main.main(longueur,largeur,population,population_malade)

def update_x(*args):
    axe_x.set(axe_x.get())

def update_y(*args):
    axe_y.set(axe_y.get())

menu_principal = tkinter.Tk()
menu_principal.title("Simulateur de pendémie")
menu_principal.geometry("1080x720")
menu_principal.minsize(1000,800)
menu_principal.iconbitmap("logo_projet.ico") #pour mettre une icone

# creer la frame
frame_pop = tkinter.Frame(menu_principal, bg="#096A09", bd=5, relief="groove")
frame_lancer = tkinter.Frame(menu_principal, bg="#096A09", bd=5, relief="groove")
frame_domaine = tkinter.Frame(menu_principal,bg="#096A09", bd=5, relief="groove")
frame_maladie = tkinter.Frame(menu_principal,bg="#096A09", bd=5, relief="groove")

menu_principal.config(background='#096A09')

image = tkinter.PhotoImage(file="logo_projet.png").zoom(50).subsample(50)
canvas = tkinter.Canvas(menu_principal,width=150, height=150,bg="#096A09", bd=0, highlightthickness=0)
canvas.create_image(100,100,image=image)
canvas.pack(expand="YES",fill="y",side="top")


# Le titre
label_title = tkinter.Label(menu_principal, text="Simulateur de propagation de maladie",font=("arial",30),bg='#096A09',fg='white')
label_title.pack(expand="YES")

# Parametres sur le domaine
label_domaine = tkinter.Label(frame_domaine,text="choix du domaine",font=("arial",20),bg='#096A09',fg='black')
label_domaine.pack()
axe_x = tkinter.IntVar()
axe_x.trace("w",update_x)
axe_x.set(600)
axe_x_entree = tkinter.Scale(frame_domaine,orient='horizontal', label="axe des X", from_=100, to=800, length=200, variable=axe_x,font=("arial",20), fg="black", bg='#D81702', activebackground="red", command=update_x(axe_x))
axe_y = tkinter.IntVar()
axe_y.trace("w",update_y)
axe_y.set(600)
axe_y_entree = tkinter.Scale(frame_domaine,orient='horizontal', label="axe des Y", from_=100, to=800, length=200, variable=axe_y,font=("arial",20), fg="black", bg='#D81702', activebackground="red", command=update_y(axe_y))
axe_x_entree.pack()
axe_y_entree.pack()

# Paramètres sur la population
label_population = tkinter.Label(frame_pop, text="Paramètres sur la population",font=("arial",25),bg='#096A09',fg='black')
label_population.pack(expand="YES")
population_totale = tkinter.IntVar()
population_totale.trace("w",update_label)
population_totale.set(90)
pop_entry = tkinter.Scale(frame_pop,orient='horizontal', from_=2, to=100, length=600, label="population totale", variable=population_totale, font=("arial",15), fg="black", bg='#D81702', activebackground="red", command=update_label(population_totale))
pop_entry.pack()

population_contamine = tkinter.IntVar()
population_contamine.trace("w",update_population_mal)
population_contamine.set(30)
pop_sick =  tkinter.Scale(frame_pop,orient='horizontal', from_=2, to=99, length=600, label="population contaminée", variable=population_contamine, font=("arial",15), fg="black", bg='#D81702', activebackground="red", command=update_population_mal(population_contamine))
pop_sick.pack()

# Paramètres sur la maladie
label_maladie =  tkinter.Label(frame_maladie, text="Paramètres maladie",font=("arial",20),bg='#096A09',fg='black')
label_maladie.pack(expand="YES")
hit_time = tkinter.DoubleVar()
hit_time.trace("w",update_hit_time)
hit_time.set(0)
hit_time_entry = tkinter.Scale(frame_maladie, orient="horizontal", from_=0, to=5,length=200, label="hit time", variable=hit_time, font=("arial",10), fg="black", bg='#D81702', activebackground="red", command=update_hit_time(hit_time))
hit_time_entry.pack()

taux_contagion = tkinter.DoubleVar()
taux_contagion.trace("w",update_taux_contagion)
taux_contagion.set(0.5)
taux_contagion_entry = tkinter.Scale(frame_maladie, orient="horizontal", from_=0, to=5,length=200, label="taux de contagion", variable=taux_contagion, font=("arial",10), fg="black", bg='#D81702', activebackground="red", command=update_taux_contagion(taux_contagion))
taux_contagion_entry.pack()

mutation = tkinter.DoubleVar()
mutation.trace("w",update_mutation)
mutation.set(0.01)
mutation_entry = tkinter.Scale(frame_maladie, orient="horizontal", from_=0, to=1,length=200, label="mutation", variable=mutation, font=("arial",10), fg="black", bg='#D81702', activebackground="red", command=update_mutation(mutation))
mutation_entry.pack()

duree_transmisibilite = tkinter.IntVar()
duree_transmisibilite.trace("w",update_duree_transmisibilite)
duree_transmisibilite.set(200)
duree_transmisibilite_entry = tkinter.Scale(frame_maladie, orient="horizontal", from_=0, to=1000,length=200, label="duree de transmisibilité", variable=duree_transmisibilite, font=("arial",10), fg="black", bg='#D81702', activebackground="red", command=update_duree_transmisibilite(duree_transmisibilite))
duree_transmisibilite_entry.pack()

letalite = tkinter.DoubleVar()
letalite.trace("w",update_letalite)
letalite.set(1)
letalite_entry = tkinter.Scale(frame_maladie, orient="horizontal", from_=0, to=10,length=200, label="létalité", variable=letalite, font=("arial",10), fg="black", bg='#D81702', activebackground="red", command=update_letalite(letalite))
letalite_entry.pack()

#Le bouton lancer
label_lancer =  tkinter.Label(frame_lancer, text="Démarrer la simulation",font=("arial",20),bg='#096A09',fg='black')
label_lancer.pack(side="left")
lancer_button = tkinter.Button(frame_lancer,text="LANCER",font=("arial",25), bg='red', fg='black',command=lancement)
lancer_button.pack(pady=25, fill="x")
lancer_button.pack()

frame_pop.pack(expand="YES",side="top",fill="both")
frame_lancer.pack(side="right", fill="x",expand="TRUE")
frame_domaine.pack(side="right",fill="y",expand="TRUE")
frame_maladie.pack(expand="YES",side="left",fill="y")

# Creation graphique
#canvas = tkinter.Canvas(frame_lancer, width=300, height=300, bg="#4065A4",bd=0, highlightthickness=0)
#canvas.create_window(1080*3/4, 420/4)
#canvas.pack(expand="YES")

menu_principal.mainloop()