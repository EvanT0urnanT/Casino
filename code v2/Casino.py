from Base_Casino import *
from Joueur import *
from Machine import *
from Boites import *
from Uno import *
from BlackJack import *
   


def choix_jeux():
    """
    choix_jeux()->str
    renvoie le nom du jeux choisis par le joueur
    """
    print("Bienvenue au Casino à quel jeux souhaitez vous jouer ? ")
    time.sleep(1)
    espace(5)
    choisis = False
    
    while not choisis :
        choix = str(input("Choisisez le jeux auquel vous souhaitez jouer. \n \n Machine \n Boites \n Uno \n BlackJack \n "))
        espace(5)
        
        if choix.lower() == "machine" or choix.lower() == "boites" or choix.lower() == "uno" or choix.lower() == "blackjack":
            print(f"Vous avez choisis de jouer à {choix} ")
            return choix


def main():
    """
    main()->None
    Appel toute les fonctions nécessaire pour permettre aux joueurs de se connecter / inscrire et de jouer aux mini jeux qu'ils souhaitent 
    """
    global info_joueur
    info_joueur = base_casino_main() #sous la forme [(pseudo, jetons), id_joueur]
    casino = Joueur(1,"Casino",get_joueur(1)[0][1])
    joueur = Joueur(info_joueur[1], info_joueur[0][0], info_joueur[0][1])
    
    def _main():
        """
        _main()->None
        Cette fonction est une sous fonction de main()
        """
        choix = choix_jeux()
        
        if choix.lower() == "machine" :
            machine_main(joueur, casino)
        
        elif choix.lower() == "boites" :
            boites_main(joueur, casino)
        
        elif choix.lower() == "uno" :
            uno_main()
        
        elif choix.lower() == "blackjack" :
            blackjack_main(joueur, casino)
    
    _main()
    fin = False
    
    while not fin :
        arret = str(input("Ecrivez fin lorsque vous souhaitez arreter ou accueil pour continuer à jouer au Casino "))
        
        if arret.lower() == "fin":
            fin = True
        
        elif arret.lower() == "accueil" :
            print("Vous avez décidez de continuer ")
            _main()

            
    
    
    
if __name__ == "__main__" :
    main()