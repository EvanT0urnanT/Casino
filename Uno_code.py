""""

Uno_code

"""
import random #importation de la bibliothèque random permettant d'utiliser les methodes permettant de realiser des actions aléatoire .
import time #importation de la bibliothèque time permettant d'attendre x minutes entre deux lignes par exemples , ici pour gagner de la fluidité sur l'affichage par exemple
from Pile import *
from Carte import *
from Joueur import *

    

def affichage_liste(liste):
    """
    affichage_liste(liste : list)-> None
    cette fonction prend une liste ici une liste de joueur , afin d'afficher les participants de la partie . 
    """
    print("\nLes joueurs inscrits sont : ")
    time.sleep(1)
    for i in range(len(liste)):
        time.sleep(0.25)
        print(f"{i+1} : {liste[i]._name}")


def creation_joueur(pioche , liste_joueur): #Cette fonction est importante car elle permet de créer automatiquement des joueurs grace a la ligne2 , ensuite on lui distribue directement ses cartes grace a la ligne3 , on trie ensuite ses cartes par couleurs a la ligne4 et on fini par ajouter le nouveau joueur a la liste des joueurs , cela est fait a la ligne5.
    """
    creation_joueur(pioche : list , liste_joueur : list)-> None
    Cette fonction à pour objectif de créer des instances de la Classe{Joueur} avec le pseudo choisit par le Joueur, ensuite lui distribuer ses cartes , lui trier , et pour finir ajouter le joueur a la liste {liste_joueur}
    """
    pseudo = str(input(("\nVeuillez choisir votre pseudo :\n"))) #ligne1
    joueur = Joueur(0,pseudo,0)   #ligne2
    joueur.distribuer(pioche)   #ligne3
    joueur.trier()  #ligne4
    liste_joueur.append(joueur) #ligne5


def creation_pioche():
    """
    creation_pioche(None)-> list
    fonction {pioche} qui retourne la list {pioche} et ses élements, si présents, comprennant toutes les cartes de la partie .
    """
    pioche = [] #creation d'une liste vide appeler pioche 
    for i in range(2): #ajout de toutes les cartes dans la pioche .
        
        pioche.append(Carte("Rouge", "+2"))
        pioche.append(Carte("Bleu", "+2"))
        pioche.append(Carte("Vert", "+2"))
        pioche.append(Carte("Jaune", "+2"))
        pioche.append(Carte("Noir", "+4"))
        pioche.append(Carte("Noir", "+4"))
        pioche.append(Carte("Noir", "Choix_Couleur"))
        pioche.append(Carte("Noir", "Choix_Couleur"))
        pioche.append(Carte("Rouge", "Changement_de_sens"))
        pioche.append(Carte("Bleu", "Changement_de_sens"))
        pioche.append(Carte("Vert", "Changement_de_sens"))
        pioche.append(Carte("Jaune", "Changement_de_sens"))
        pioche.append(Carte("Rouge", "Passe_ton_tour"))
        pioche.append(Carte("Bleu", "Passe_ton_tour"))
        pioche.append(Carte("Vert", "Passe_ton_tour"))
        pioche.append(Carte("Jaune", "Passe_ton_tour"))
        for j in range(30):
            #(j%10) est un calcul spécial car il regarde uniquement le reste de la division de (j par 10) donc pour j=1 cela vaut 1 pour j=5 on a 5 pour j = 10 on retourne a 0 pour j=15 on a 5 etc etc 
            pioche.append(Carte("Rouge", (j%10))) 
            pioche.append(Carte("Bleu", (j%10)))
            pioche.append(Carte("Vert", (j%10)))
            pioche.append(Carte("Jaune", (j%10)))
            
    return pioche



def piocher(pioche):
    """
    piocher (pioche : list)->instance
    Piocher est une fonction permettant de retourner une carte (tirée aléatoirement) de la pioche 
    """
    n = random.randint(0, len(pioche) -1) #on assigne a {n} un nombre aléatoire allant de 0 a la longueur total de la liste -1
    return pioche.pop(n) 


def ajoute(defausse, element):
    """
    ajoute (defausse -> (Pile,list) , element -> instance ) -> None
    On empile/ajoute une carte sur le tas({defausse})
    
    """
    defausse.empile(element)
    return element


def carte_plus_2(x, nb_joueur, liste_joueur, pioche, n):
    """
    carte_plus_2(x : int, nb_joueur : int, liste_joueur : list, pioche : list, n : int)-> int
    Cette fonction correspond a l'utilisation d'une carte +2 d'un des deux joueurs , On demande au joueurs adverse si ils souhaitent en utiliser un , sinon il pioche les {n}*2 cartes dans la {pioche}, une fois les cartes piocher par un des deux joueurs on renvoie l'entier 1 permettant d'augmenter {x} et donc permettant de ne pas faire jouer le joueur qui pioche 

    {x} : est un entier permettant de savoir a n'importe quel moment a quel joueur est ce le tour de joueur 
    {nb_joueur} : est un entier permettant de savoir combien de joueur sont dans la partie 
    {liste_joueur} : est une liste contenant les {nb_joueur} joueurs
    {pioche} : est la liste contenant les cartes dans la pioche 
    {n} : est un entier correspondant au nombre de carte +2 mise a la suite pour pouvoir disstribuer le bon nombre de cartes . 
    """
    espace()
    liste_joueur[x].affichage2()
    num_carte = input(f"\n {liste_joueur[x]._name}\nVotre adversaire a utiliser un +2 avez vous un +2 pour le contrer  ?\n Si oui donner le numero de la Carte sinon écrivez 'pioche' ")
    if num_carte.lower().strip() == "pioche" : #On utilise la methode .strip() pour enlever tous les espaces au début et a la fin , cela permet d'éviter les fautes de frappes tels qu'un espace au début ou a la fin et la méthode .lower() pour tout mettre en minuscule et donc éviter les soucis de minuscules / majuscules  .

        for i in range((2*n)): 
            
            liste_joueur[x]._deck.append(piocher(pioche))
            liste_joueur[x].affichage2()
            
        liste_joueur[x].trier()
        return 1 #le return 1 permet d'éviter que le joueur qui vient de piocher puisse jouer . 

    carte_jouer = liste_joueur[x]._deck.pop(int(num_carte) -1)
    if carte_jouer._numero != "+2":
        
        liste_joueur[x]._deck.append(carte_jouer)
        liste_joueur[x].trier()
        print("\nLa carte choisis n'est pas jouable")
        return carte_plus_2(x, nb_joueur, liste_joueur, pioche, n)
        
    if carte_jouer._numero == "+2" :
        
        n = n + 1 #On incrémente {n} ce qui signifie qu'une nouvelle carte +2 a été utiliser .
        return carte_plus_2((x+1)%(nb_joueur), nb_joueur, liste_joueur, pioche, n) #Dans le cas où une nouvelle carte +2 a été utiliser on appelle a nouveau la fonction mais sur le joueur suivant  
    

def carte_plus_4(x, nb_joueur, liste_joueur, pioche, n, defausse):
    """
    carte_plus_4(x : int, nb_joueur : int, liste_joueur : list, pioche : list, n : int, defausse : Pile)-> int
    Cette fonction correspond a l'utilisation d'une carte +4 d'un des deux joueurs , On demande au(x) joueur(s) adverse(s) si il(s) souhaite(nt) en utiliser un , sinon il(s) pioche(nt) les {n}*4 cartes dans la {pioche} une fois les cartes piochées par un des deux joueurs, on renvoie l'entier 1 permettant d'augmenter {x} et donc permettant de ne pas faire jouer le joueur qui pioche 

    {x} : est un entier permettant de savoir à n'importe quel moment à quel(s) joueur(s) est-ce le tour de jouer 
    {nb_joueur} : est un entier permettant de savoir combien de joueurs sont dans la partie 
    {liste_joueur} : est une liste contenant les {nb_joueur} joueurs
    {pioche} : est la liste contenant les cartes dans la pioche 
    {n} : est un entier correspondant au nombre de carte +4 mise a la suite pour pouvoir disstribuer le bon nombre de cartes .
    {defausse} : correspond à la défausse , utilisée ici pour appeler la fonction {choix_couleur} permettant au joueur ayant utilisée le +4 de choisir la couleur de la carte en haut de la défausse . 
    """
    liste_joueur[x].affichage2()
    num_carte = input(f"\n{liste_joueur[x]._name} Votre adversaire a utilisé un +4.\nAvez-vous un +4 pour le contrer  ?\nSi oui, donner le numéro de la Carte sinon écrivez pioche ")
    if str(num_carte).lower().strip() == "pioche" :  #On utilise la methode .strip() pour enlever tous les espaces au début et a la fin , cela permet d'éviter les fautes de frappes tels qu'un espace au début ou a la fin et la méthode .lower() pour tout mettre en minuscule et donc éviter les soucis de minuscules / majuscules .

        for i in range((4*n)):

            liste_joueur[x]._deck.append(piocher(pioche))

        liste_joueur[x].affichage2()
        liste_joueur[x].trier()
        choix_couleur(defausse,(x+1)%(nb_joueur),liste_joueur)
        return 1 #le return 1 permet d'éviter que le joueur qui vient de piocher puisse jouer .

    carte_jouer = liste_joueur[x]._deck[int(num_carte)-1]
    if carte_jouer._numero != "+4":

        liste_joueur[x]._deck.append(carte_jouer)
        liste_joueur[x].trier()
        print("La carte choisis n'est pas jouable")
        return carte_plus_4(x,nb_joueur,liste_joueur,pioche,n)

    if carte_jouer._numero == "+4" :

        n = n + 1 #On incrémente {n} ce qui signifie qu'une nouvelle carte +4 a été utiliser .
        return carte_plus_4((x+1)%(nb_joueur),nb_joueur,liste_joueur,pioche,n,defausse) #Dans le cas où une nouvelle carte +4 a été utiliser on appelle a nouveau la fonction mais sur le joueur suivant  


def choix_couleur(defausse, x, liste_joueur):
    """
    choix_couleur(defausse, x, liste_joueur)
    Cette fonction permet au joueur ayant utilisé une carte changement de couleur,de choisir une couleur, la couleur choisit prendra la forme d'une carte aléatoire de cette même couleur 

    {defausse} : ceci est une liste contenant la défausse elle nous permet d'ajouter une carte en haut de la défausse pour modifier la couleur du jeu 
    {x} : est un entier permettant de savoir à n'importe quel moment à quel(s) joueur(s) est-ce le tour de jouer 
    {liste_joueur} : est une liste contenant les {nb_joueur} joueurs
    """
    couleur_changement = input(f"\n{liste_joueur[x]._name} Vous avez joué une carte qui vous permet de changer de couleur une carte sera mis en haut de la défausse avec la couleur que vous souhaitez .\nÉcrivez la couleur souhaitée parmis ( Rouge , Bleu , Vert , Jaune )")
    if str(couleur_changement).lower().strip() == "rouge" : #On utilise la methode .strip() pour enlever tous les espaces au début et a la fin , cela permet d'éviter les fautes de frappes tels qu'un espace au début ou a la fin et la méthode .lower() pour tout mettre en minuscule et donc éviter les soucis de minuscules / majuscules .

        defausse.empile(Carte("Rouge",random.randint(0,9))) #On créer une carte de Couleur Rouge et de numero (aléatoire entre 0 et 9) 

    elif str(couleur_changement).lower().strip() == "bleu" :#On utilise la methode .strip() pour enlever tous les espaces au début et a la fin , cela permet d'éviter les fautes de frappes tels qu'un espace au début ou a la fin et la méthode .lower() pour tout mettre en minuscule et donc éviter les soucis de minuscules / majuscules .

        defausse.empile(Carte("Bleu",random.randint(0,9)))#On créer une carte de Couleur Bleu et de numero (aléatoire entre 0 et 9) 

    elif str(couleur_changement).lower().strip() == "vert" :#On utilise la methode .strip() pour enlever tous les espaces au début et a la fin , cela permet d'éviter les fautes de frappes tels qu'un espace au début ou a la fin et la méthode .lower() pour tout mettre en minuscule et donc éviter les soucis de minuscules / majuscules .

        defausse.empile(Carte("Vert",random.randint(0,9)))#On créer une carte de Couleur Vert et de numero (aléatoire entre 0 et 9) 
    
    elif str(couleur_changement).lower().strip() == "jaune" :#On utilise la methode .strip() pour enlever tous les espaces au début et a la fin , cela permet d'éviter les fautes de frappes tels qu'un espace au début ou a la fin et la méthode .lower() pour tout mettre en minuscule et donc éviter les soucis de minuscules / majuscules .

        defausse.empile(Carte("Jaune",random.randint(0,9)))#On créer une carte de Couleur Jaune et de numero (aléatoire entre 0 et 9) 
    
    else :
        
        choix_couleur(defausse,x,liste_joueur) 
    

def choix_carte(liste_joueur, x, defausse, pioche, carte_haut_defausse, nb_joueur):
    """
    choix_carte(liste_joueur : list, x : int, defausse : Pile, pioche : list, carte_haut_defausse : instance(Carte), nb_joueur : int)-> int
    Cette fonction est la fonction principale permettant de réaliser un tour au joueur {x} , Il va choisir sa carte , elle va être testée pour vérifier qu'elle soit jouable, et si c'est le cas, elle sera jouée 

    {x} : est un entier permettant de savoir à n'importe quel moment à quel(s) joueur(s) est-ce le tour de jouer 
    {nb_joueur} : est un entier permettant de savoir combien de joueurs sont dans la partie 
    {liste_joueur} : est une liste contenant les {nb_joueur} joueurs
    {pioche} : est la liste contenant les cartes dans la pioche 
    {defausse} : correspond à la défausse, utilisée ici pour appeler la fonction {choix_couleur} permettant au joueur ayant utilisée le +4, de choisir la couleur de la carte en haut de la défausse .
    {carte_haut_defausse} : est la carte qui est en haut de la défausse  
    """
    print(f"\nLa carte en haut de la défausse est la suivante : ({carte_haut_defausse._numero},{carte_haut_defausse._couleur}) ")
    time.sleep(2)
    liste_joueur[x].affichage2()
    time.sleep(0.2)
    num_carte = input("\nVeuillez choisir le numéro de la carte ( visible sur la gauche ) , que vous souhaitez jouer.\nOu si aucunes de vos cartes sont jouables, entrez (pioche) : ")
    if str(num_carte).lower().strip() == "pioche" : #On utilise la methode .strip() pour enlever tous les espaces au début et a la fin , cela permet d'éviter les fautes de frappes tels qu'un espace au début ou a la fin et la méthode .lower() pour tout mettre en minuscule et donc éviter les soucis de minuscules / majuscules .

        time.sleep(1)
        carte_piocher = piocher(pioche) #On pioche une carte dans la pioche et on la sauvegarde dans carte_piocher
        (liste_joueur[x]._deck).append(carte_piocher)
        print(f"\nVous avez piocher ({carte_piocher._numero},{carte_piocher._couleur}) ")
        time.sleep(1)
        liste_joueur[x].trier()
        return 0

    try :

        num_carte = int(num_carte)
        while num_carte > len(liste_joueur[x]._deck):

            num_carte = input("\nChoisissez le numéro de la carte ( visible sur la gauche ), que vous souhaitez jouer\nOu alors, si aucunes de vos cartes sont jouables, entrez : (pioche)")
            num_carte = int(num_carte)

        carte_jouer = liste_joueur[x]._deck[num_carte-1]
        print(f"Vous avez joué la carte suivante . ({carte_jouer._numero},{carte_jouer._couleur})")
        time.sleep(1)
        #test :
        temp = defausse.depile()

        if carte_jouer._numero == temp._numero or carte_jouer._couleur == temp._couleur or carte_jouer._couleur == "Noir" or temp._couleur == "Noir" :
            
            print("\nLa carte choisi est Jouable")
            defausse.empile(temp)
            defausse.empile((liste_joueur[x]._deck).pop(num_carte - 1))#On empile sur la defausse la carte choisis par le joueur
            time.sleep(1)
            liste_joueur[x].affichage2()
            time.sleep(1)

            if carte_jouer._numero == "+2" :
                defausse.empile(carte_jouer)
                n = 1 #{n} Correspond au nombre de carte +2 jouer
                return carte_plus_2(((x+1)%(nb_joueur)),nb_joueur,liste_joueur,pioche,n)

            elif carte_jouer._couleur == "Noir" :

                if carte_jouer._numero == "+4":
                    
                    n = 1 #{n} Correspond au nombre de carte +4 jouer
                    return carte_plus_4(((x+1)%(nb_joueur)),nb_joueur,liste_joueur,pioche,n,defausse)

                else :

                    choix_couleur(defausse,x,liste_joueur)
            
            elif carte_jouer._numero == "Changement_de_sens":

                liste_joueur.reverse() #On inverse le sens et donc pour faire cela on "retourne " la liste des joueurs
            
            elif carte_jouer._numero == "Passe_ton_tour":
                
                return 1 #le return 1 permet d'éviter que le joueur qui vient de piocher puisse jouer .
        else :

            print("\nVotre carte n'est pas jouable ")
            defausse.empile(temp)
            time.sleep(1)
            return (choix_carte(liste_joueur,x,defausse,pioche,carte_haut_defausse,nb_joueur))

    except :

        print("Votre entrée n'est pas conforme .")
        return (choix_carte(liste_joueur,x,defausse,pioche,carte_haut_defausse,nb_joueur))
        
    return 0 #le return 0 permet de laisser le fonctionnement de tour original se réaliser
    



