import random
from Base_Casino import *
from Joueur import *
import time


global couleur 
couleur = ["♥" ,"♣" ,"♦" ,"♠"] 
global chiffre
chiffre = ["2","3","4","5","6","7","8","9","10"]
global tete
tete = ["V","Q","K","A"]
global valeur
valeur = {"2": 2 , "3": 3 ,"4": 4 , "5": 5 , "6":6 , "7": 7 , "8": 8 ,"9": 9 , "10": 10 , "V": 10 ,"Q" : 10 ,"K": 10 , "A" : (1,11)}


def pioche():
    """
    pioche(none)->None
    cette fonction créer une liste contenant les cartes , la pioche
    """
    
    global pioche
    pioche = []
    
    for k in range(7):
        for i in range(len(couleur)):
            for j in range(len(chiffre)):
                pioche.append((couleur[i],chiffre[j]))
                
            for t in range(len(tete)):
                pioche.append((couleur[i],tete[t]))
    
    random.shuffle(pioche)
    

def distribution(deck):
    """
    distribution(deck : list)
    cette fonction permet de distribuer une carte au joueur a qui appartient le 'deck' cette carte est récupérer dans la pioche de façon aléatoire.
    """
    carte = pioche.pop()
    if carte[1] == "A" :
        deck[1] = (deck[1] + valeur[carte[1]][0] , deck[1] + valeur[carte[1]][1])
        deck.append(carte)
        
        if deck[0] == "Joueur" :
            valide = False
            
            while not valide :
                choix = str(input(f"Vous avez piocher un As l'as peut valoir 1 ou 11 cela vous donnerait donc \n 1 : {deck[1][0]} points \n ou \n 2 : {deck[1][1]} points \n choisisez celui que vous voulez en entrant le numero correspondant ")) 
                
                if choix == "1":
                    deck[1] = deck[1][0]
                    valide = True
                
                elif choix == "2":
                    deck[1] = deck[1][1]
                    valide = True
                
                else :
                    print("Erreur de saisie")
        
        else :
            if deck[1][1] <= 21 :
                deck[1] = deck[1][1]
            
            else :
                deck[1] = deck[1][0]
    else : 
        deck[1] += valeur[carte[1]]
        deck.append(carte)
    
    
def affichage(croupier_carte, joueur_carte):
    """
    affichage(deck : list)->None 
    permet d'afficher les cartes de la personne .
    """
    espace(100)
    
    print("Voici les Cartes du Croupier :")
    for i in range (2, len(croupier_carte)):
        print(croupier_carte[i])
        
    print(f"Pour un total de {croupier_carte[1]}")  
    time.sleep(2)
    espace(5)
    
    print("Voici vos Cartes :")
    for i in range(2,len(joueur_carte)):
        print(joueur_carte[i])
        
    print(f"Pour un total de {joueur_carte[1]}")
    time.sleep(2)

        
def blackjack_main(joueur, casino):
    """
    blackjack_main(joueur : inst , casino : inst )-> None
    cette fonction est la fonction prinpale permettant de lancer les différente fonction pour faire une partie de BlackJack
    """
    pioche()
    fin = False
    
    def _blackjack_main():
        """
        _blackjack_main()-> None
       cette fonction est une sous fonction de la fonction blackjack_main() permettant de mettre en place le fonctionnement le BlackJack
        """
        mise = joueur.mise(casino)
        joueur_carte = ["Joueur",0]
        croupier_carte = ["Croupier",0]
        distribution(joueur_carte)
        distribution(joueur_carte)
        distribution(croupier_carte)
        
        def blackjack_main_partie(valide):
            """
            blackjack_main_partie(valide : bool)-> None
            Cette sous fonction de la fonction _blackjack_main met en fonctionnement et suis le fonctionnement du BlackJack tour par tour
            """
            fin = False
            perdu = False
            
            while not fin and not perdu :
                
                if joueur_carte[1] > 21 :
                    affichage(croupier_carte, joueur_carte)
                    perdu = True
                    print("Vous avez perdu ")
                    return 0

                elif croupier_carte[1] > 21 :
                    affichage(croupier_carte, joueur_carte)
                    fin = True
                    print("Le croupier a perdu")
                    return 2
                    
                elif joueur_carte[1] == 21 :
                    affichage(croupier_carte, joueur_carte)
                    fin = True
                    print("BlackJack Félicitations vous avez gagné 1.5 fois de plus votre mise de départ")
                    return 2.5
                
                else :
                    affichage(croupier_carte, joueur_carte)
                    
                    while not valide :
                        choix = str(input("Vous souhaitez tirer une carte ? (si oui écrivez tirage ) ou vous arreter la ? (si oui écrivez stop) : ")).lower().strip()
                        
                        if choix == "tirage":
                            distribution(joueur_carte)
                            return blackjack_main_partie(False)
                       
                        elif choix == "stop" :
                           valide = True
                        
                        else :
                            print("Vous avez fait une erreur de saisie ")
                        
                    while croupier_carte[1] < 17 :
                        distribution(croupier_carte)
                        return blackjack_main_partie(True)
                    
                    fin = True
                    if croupier_carte[1] > 21 :
                        affichage(croupier_carte, joueur_carte)
                        print("Vous avez gagné")
                        return 2
                    
                    elif croupier_carte[1] > joueur_carte[1] :
                        affichage(croupier_carte, joueur_carte)
                        print(f"Vous avez perdu car vous avez {joueur_carte[1]} points et le croupier à {croupier_carte[1]} points")
                        return 0
                    
                    elif croupier_carte[1] == joueur_carte[1]:
                        affichage(croupier_carte, joueur_carte)
                        print("Vous avez fait égalité ")
                        return 1
                    
                    else :
                        affichage(croupier_carte, joueur_carte)
                        print("Vous avez gagné ")
                        return 2
                          
        multiplicateur = blackjack_main_partie(False)
        gain = mise * multiplicateur 
        joueur._jetons += gain
        casino._jetons -= gain
        update_jetons(casino._id_joueur , casino._jetons)
        update_jetons(joueur._id_joueur , joueur._jetons)
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
        
        if fin == False :
            _blackjack_main()
    
    _blackjack_main()
    
    
if __name__ == "__main__" :
    blackjack_main()