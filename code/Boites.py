import random
import math
from Base_Casino import *
from Joueur import *



def boite_affichage(list):
    """
    boite_affichage(list : list ) -> None
    cette fonction prend une liste de caractère pour ensuite les utiliser pour pouvoir faire l'affichage du mini_jeux .
    """
    print("▬"*58)
    j = 0
    
    for _ in range(5):
        print("▌", end = "       " )
        print(" _        " * 5, end = "")
        print("▌")
        print("▌", end = "       " )

        for _ in range(5):
            print(f"|{list[j]}|       ", end = "")
            j+=1
        print("▌")
        print("▌", end = "       " )
        print(" ¯        " * 5, end = "")
        print("▌")

    print("▬"*58)


def nb_boite_gagnante():
    """
    nb_boite_gagnante()-> int
    renvoie le nombre de boite gagnante choisis par le joueur (25 > nb > 0 )
    """
    nombre_boite_gagnante = math.inf
    
    while nombre_boite_gagnante > 24 or nombre_boite_gagnante < 1 :
        nombre_boite_gagnante = int(input("Combien de boite gagnante souhaitez vous avoir ? le nombre doit être inférieur à 25 et supérieur à 0 : "))
        
    return nombre_boite_gagnante


def boites_main(joueur, casino):
    """
    boites_main(joueur : Joueur() , casino : Joueur())-> None
    Cette fonction correspond à tout les appels permettant de jouer au jeux des boites 
    """
    fin = False
    
    while not fin :
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"]
        nombre_boite_gagnante = nb_boite_gagnante()
        mise = joueur.mise(casino)
        multiplicateur = 1.1**(25 - nombre_boite_gagnante)
        liste_gagnante = []
        
        for _ in range(nombre_boite_gagnante):
            liste_gagnante.append("♥")
        
        for _ in range(25 - nombre_boite_gagnante):
            liste_gagnante.append("✶")
        random.shuffle(liste_gagnante)
        espace(100)
        boite_affichage(alphabet)
        time.sleep(1)
        espace(4)
        perdu = False
        
        while not perdu and not fin :
            existe = False
            
            while not existe :
                choix = str(input("choisisez une lettre : ")).lower().strip()
                espace(4)
                
                if choix in alphabet :
                    pos = alphabet.index(choix)
                    alphabet[pos] = liste_gagnante[pos]
                    espace(100)
                    boite_affichage(alphabet)
                    time.sleep(1)
                    existe = True
                    
                    if liste_gagnante[pos] == "✶" :
                        espace(2)
                        print("Vous avez perdu ")
                        perdu = True
                        casino._jetons += mise
                        update_jetons(casino._id_joueur , casino._jetons)
                        
                    else :
                        multiplicateur *= 1.1
                        espace(2)
                        print(f"Vous avez gagné , votre multiplicateur est désormais de {(multiplicateur-1)}")
                        time.sleep(2)
                        espace(2)
                        choix_suite = str(input("Si vous souhaitez vous arreter et récupérer vos gain écrivez stop sinon appuyez sur entrée pour tenter d'augmenter votre multiplicateur tout en risquant de tout perdre ")).lower().strip()
                        
                        if choix_suite.lower() == "stop" :
                            fin = True
                            joueur._jetons += int((multiplicateur-1) * mise)
                            update_jetons(joueur._id_joueur , joueur._jetons)
                            casino._jetons -= int((multiplicateur-1) * mise)
                            update_jetons(casino._id_joueur , casino._jetons)
        
        valide = False
        
        while not valide :
            espace(5)
            arret = str(input("Souhaitez vous refaire une partie ? \n Yes \n No \n "))
            
            if arret.lower() == "yes" :
                valide = True
                fin = False
            
            elif arret.lower() == "no" :
                fin = True
                valide = True
