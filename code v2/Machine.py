import random
import time 
from Joueur import *
from Base_Casino import *



def machine_affichage():
    """
    machine_affichage()-> tupl
    Créer l'affichage de la machine et tire trois chiffres aléatoire puis les renvoie pour voir si il y a des combinaisons gagnantes 
    """
    espace(100)
    nb1 = random.randint(0,9)
    nb2 = random.randint(0,9)
    nb3 = random.randint(0,9)
    
    for i in range (85):
        print("-",end = "")
    print(" ")
    
    for i in range (85):
        print("-",end = "")
    print(" ")
    
    for i in range (85):
        print("-",end = "")
    print(" ")
    
    for i in range (19):
        print("-",end = "")
    print(" ",end = "")
    print(nb1,end = "")
    print(" ",end = "")
    
    for i in range (19):
        print("-",end = "")
    print(" ",end = "")
    print(nb2,end = "")
    print(" ",end = "")
    
    for i in range (19):
        print("-",end = "")
    print(" ",end = "")
    print(nb3,end = "")
    print(" ",end = "")
    
    for i in range (19):
        print("-",end = "")
    print(" ")
    
    for i in range (85):
        print("-",end = "")
    print(" ")
    
    for i in range (85):
        print("-",end = "")
    print(" ")
    
    for i in range (85):
        print("-",end = "")
    print(" ")
    print(" ")
    return (nb1,nb2,nb3)


def machine_victoire(resultat , mise , joueur, jackpots , casino):
    """
    machine_victoire(resultat : tupl , mise : int , joueur : instance , jackpots : instance , casino : instance)
    Cette fonction permet de vérifier si les numéros tirés au hasard font partis des combinaisons gagnantes si c'est le cas le multiplicateur augmente et a la fin le gain correspond a la mise * le multiplicateur 
    """
    nb_win = 0
    multiplicateur = 0
    gain = 0
    time.sleep(0.5)
    print(f"Vous avez misez {mise} jetons , il vous reste {joueur._jetons} jetons ")
    print(" ")
    
    if resultat.count(7) > 0 :
        
        if resultat.count(7) <= 2 :
            
            time.sleep(0.5)
            print(f"Victoire vous avez {resultat.count(7)} chiffre 7")
            print(" ")
            multiplicateur += 1 * resultat.count(7)
            nb_win += 1 
            
        else :
            print("Jackpots !!!!!!")
            if jackpots._jetons <= mise *7 :
                multiplicateur = 5
                nb_win += 1 
            else :
                gain = jackpots._jetons /2
                jackpots._jetons = jackpots._jetons / 2
                print(f"Vous avez gagner {gain} vous avez donc maintenant {joueur._jetons + gain }")
                return gain 
            
    if resultat.count(resultat[0]) > 1 :
        time.sleep(0.5)
        print(f"Victoire vous avez {resultat.count(resultat[0])} chiffres identiques ")
        print(" ")
        nb_win += 1
        multiplicateur += 2
        
    elif resultat.count(resultat[1]) > 1 :
        time.sleep(0.5)
        print(f"Victoire vous avez {resultat.count(resultat[1])} chiffres identiques ")
        print(" ")
        nb_win += 1
        multiplicateur += 2
        
    if resultat[2] == (resultat[1]+1) and resultat[1] == (resultat[0]+1):
        time.sleep(0.5)
        print("Victoire, vous avez gagner grace a une suite ")
        print(" ")
        nb_win += 1
        multiplicateur += 5
        
    if resultat[0]%2 == 0 and resultat[1]%2 == 0 and resultat[2]%2 == 0 :
        time.sleep(0.5)
        print("Victoire, vos trois chiffres sont pairs vous avez donc gagner")
        print(" ")
        nb_win += 1
        multiplicateur += 2
        
    if nb_win == 0 :
        time.sleep(0.5)
        print("Perdu")
        print(" ")
        jackpots._jetons = jackpots._jetons + mise / 10
        casino._jetons = casino._jetons -(mise / 10)

    else :
        gain = mise * multiplicateur
        time.sleep(0.5)
        print(" ")
        print(" ")
        print(f"Vous avez gagné {gain} jetons grâce a un multiplicateur de *{multiplicateur} et une mise initiale de {mise} vous avez donc maintenant {joueur._jetons + gain} jetons ")
        print(" ")
        print(" ")
    update_jetons(jackpots._id_joueur , jackpots._jetons)
    return gain 


def machine_main(joueur, casino):
    """
    machine_main(joueur : Joueur() , casino : Joueur() )->None
    Cette fonction appelle toute les fonctions nécessaire pour pouvoire permettre aux joueurs de jouer à la machine à sous 
    """
    jackpots = Joueur(2,"Jackpots" , get_joueur(2)[0][1]) 
    
    def _main():
        """
        _main()->None
        Cette fonction est une sous fonction de machine_main()
        """
        machine_mise = joueur.mise(casino)
        
        if machine_mise == None : 
            time.sleep(0.5)
            print("Vous ne pouvez pas jouer avec 0 jetons .")
            print(" ")
            return 
            
        else : 
            def __main():
                """
                __main()->None
                Cette fonction est une sous fonction de _main()
                """
                resultat = machine_affichage() #on obtient les 3 chiffres sous forme d'un tuple
                gain = machine_victoire(resultat , machine_mise , joueur , jackpots, casino) 
                joueur._jetons += gain
                update_jetons(joueur._id_joueur , joueur._jetons)
                casino._jetons -= gain
                update_jetons(casino._id_joueur , casino._jetons)
                time.sleep(0.5)
                tour = str(input("Si vous souhaitez arreter de jouer écrivez 'Stop' sinon si vous souhaitez changer votre mise écrivez 'mise',\n si vous souhaitez continuer de jouer avec la meme mise n'écrivez rien : ")).lower().strip()
                print(" ")
                if tour == "stop" or tour == "mise":
                    
                    if tour == 'stop':
                        
                        time.sleep(0.5)
                        print(f"Vous avez décidez d'arreter de jouer , vous avez : {joueur._jetons} jetons ")
                        time.sleep(2.5)
                        espace(3)
                        return True
                        
                    else :
                        _main()
                        
                else :
                    if machine_mise <= joueur._jetons :
                        joueur._jetons -= machine_mise
                        casino._jetons += machine_mise
                        __main()
                        
                    else :
                        time.sleep(0.5)
                        print(f"Vous ne possédez pas suffisement de jetons, misez un nombre de jetons inférieur ou égale a votre nombre de jetons : {joueur._jetons}")
                        print(" ")
                        _main()
                        
            __main()
            
    _main()

    