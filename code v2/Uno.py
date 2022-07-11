""""

Uno

"""

from Uno_code import *
    
def uno_main():
    """
    uno(None)-> None
    cette fonction est la fonction principale , c'est a partir de cette fonction que les parties vont être commencez , Elle initialise la partie , et l'organise tout le long jusqu'a la victoire d'un des joueurs .
    """
    liste_joueur = [] #Créer une liste contenant tous les joueurs
    nb_joueur = int(input("\nVeuillez choisir le nombre de joueurs : ")) #Récuperation du nombre de joueur
    pioche = creation_pioche() #Création de la Pioche
    for i in range(nb_joueur):

        creation_joueur(pioche, liste_joueur) #Création des joueurs

    affichage_liste(liste_joueur)
    x = random.randint(-1, nb_joueur-1) #{x} est la variable qui permet de controller le tour de chaque joueur 
    time.sleep(1)
    print(f"\nLe joueur commencant est : {liste_joueur[x]._name}")
    time.sleep(1.5)
    defausse = Pile(9999)
    carte_haut_defausse = ajoute(defausse, piocher(pioche)) #On pioche la première carte que l'on met en haut de la Défausse.

    while len(liste_joueur[0]._deck) > 0 and len(liste_joueur[1]._deck) > 0 : 

        if len(pioche) < 10 : #si Cette condition est vérifier cela signifie qu'il y a moins de 10 cartes dans la pioche ce qui est assez peux et donc on retourne la défausse pour recuperer une pioche 

            temp = defausse.depile()
            while defausse.est_vide == False :

                pioche.append(defausse.depile())

            pioche.shuffle() #permet de mélanger la pioche 
            defausse.empile(temp) 
            
        espace(100)
        x = (x+ choix_carte(liste_joueur,x,defausse,pioche,carte_haut_defausse,nb_joueur))%(nb_joueur)
        x = (x+1)%(nb_joueur)
        carte_haut_defausse = ajoute(defausse,defausse.depile())

    if len(liste_joueur[0]._deck) == 0  :

        print(f"\nLa partie est terminer le gagnant est : {liste_joueur[0]._name} ")

    else :
        
        print(f"\nLa partie est terminer le gagnant est : {liste_joueur[1]._name} ")