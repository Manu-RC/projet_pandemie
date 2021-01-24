							BONJOUR 

---PRESENTATION---

Ce projet porte sur la simulation graphique d'une pandémie avec des individus représentés par des disques dont la
couleur varie selon l'état (sain,malade,immunisé) qui se déplacent en suivant une physique de chocs élastiques
à chaque collision avec un mur ou un autre individu. L'évolution de la simulation sera régie en grande partie par de 
l'aléatoire, ne vous attendez pas à voir deux fois la même simulation avec des paramètres identiques (cf. utilisation).

L'enjeu n'est pas ici de recréer une pandémie réelle mais bien de la modéliser, rendant ce programme plus ludique que
véridique ! BON JEU !

---UTILISATION---

Pour lancer une simulation, vous devrez éxecuter le fichier menu.py, celui-ci vous affichera alors un menu avec des 
paramètres que vous pourrez choisir à votre guise et qui impacteront l'évolution de la simulation. Une fois choisis, 
cliquez sur "LANCER LA SIMULATION" et le main.py s'exécutera et la simulation commencera.

Vous pouvez :
- Lancer la simulation avec le bouton "START"
- Arrêter la simulation avec le bouton "STOP"
- Ralentir la simulation avec "<<" et "<"
- Accélérer la simulation avec ">>" et ">"
- Choisir parmi les modes de déplacement des individus en temps réel : "Vie normale", "Isolement", "Couvre-feu"
- Afficher le graphe dynamique de la situation des individus de la simulation avec le bouton "Graph" 
  --> ATTENTION ! Pour fermer le graphe réappuyez sur "Graph", NE FERMEZ PAS la fenêtre matplotlib (il aime pas trop) :(

Pour tout fermer, fermez la fenêtre de la simulation. 

---INFORMATIONS COMPLEMENTAIRES---

Les paramètres sont bornés de telle manière à obtenir une simulation optimale et ne pas obtenir de bug ou de lag.
