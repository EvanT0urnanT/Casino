import random
import time
from Base_Casino import *


class Joueur():
    
    
    def __init__(self, id_joueur, name, jetons):
        """
        __init__(self, id_joueur : int ,name : str , jetons : int)
        Cette fonction créer des instances de la classe Joueur() avec les attributs : id_joueur , name , jetons , deck
        """
        
        self._id_joueur = id_joueur
        self._name = name
        self._jetons = jetons
        self._deck = [] #création d'une liste Vide 


    def mise(self , casino):
        """
        mise(self : instance , casino : instance)-> int or None
        Cette fonction permet de récupérer la mise du Joueur tout en vérifiant qu'il possède suffisement de jetons .
        """
        if self._jetons > 0 :
            mise_temp = int(input(f"Vous possédez {self._jetons} jetons , Combien de jetons souhaitez vous miser ? : "))
            
            if mise_temp > self._jetons :
                print(f"Vous ne pouvez pas miser autant({mise_temp} jetons ) car vous avez {self._jetons} jetons")
                return self.mise(casino)
            
            elif mise_temp == 0 :
                print("Vous ne pouvez pas misez 0 jetons.")
                return self.mise(casino)
            
            else :
                self._jetons = self._jetons - mise_temp
                casino._jetons = casino._jetons + mise_temp
                print(casino._jetons)
                print(self._jetons)
                print(f"Vous avez miser {mise_temp} jetons , il vous reste donc {self._jetons}")
                update_jetons(self._id_joueur , self._jetons)
                update_jetons(casino._id_joueur , casino._jetons)
                return mise_temp
        
        else : 
            print("Vous ne possedez pas suffisement de jetons car vous avez 0 jetons ")
            return None
        
        
    def distribuer(self, pioche):
        """
        distribuer (self : instance , pioche : list ) -> None
        Méthode permettant de distribuer au joueur, {self}, ses cartes de départ  
        """
        # distribuer a chcun des joueurs 7 cartes de la pioche une par une
        assert not len(pioche) <= 7, "Il y a trop de joueur" #On verifie qu'il y a suffisemment de carte pour pouvoir en distribuer 7 a tous les joueurs , sinon un message disant "Il y a trop de joueur apparait"
        
        while len(self._deck) < 7:
            n = random.randint(0, len(pioche) - 1) #utilisation de la méthode randint appartenant a la bibliothèque random pour tirer un numéro aléatoire et donc tirer une carte aléatoire dans la pioche 
            self._deck.append(pioche.pop(n))


    def affichage2(self):
        """
        affichage2 ( self : instance ) -> None
        methode affichant les cartes d'un joueur, {self}
        """
        print(f"Voici , Vos cartes ({self._name}) :")
        print("\n") #permet de faire un saut de 3/4 lignes .
        
        for i in range(len(self._deck)):
            time.sleep(0.1) #utilisation de la méthode .sleep() de la bibliothèque time . Permettant de créer un temps d'attente de 0.1 secondes entre chaque affichage
            print(f"{i+1} : {self._deck[i]._numero,self._deck[i]._couleur}")


    def trier(self):
        """
        trier(self : instance)-> None
        {trier} est une méthode qui a pour objectif de trier les cartes du joueur {self} par couleur , pour ce faire elle emploie une sous fonction {_trier}
        """
        temp = self._deck.copy() #temp est une copy temporaire de l'instance self
        self._deck.clear() # On supprime le contenu de l'instance self

        def _trier(couleur): #sous fonction évitant de créer a chaque fois un nouveau temp ou de clear self._deck() a chaque tour 
            """
            _trier(couleur : str)-> None
            {_trier} est une sous fonction de la methode {trier} qui a pour objectif de trier par couleur les cartes du joueur {self} . 
            """
            i = 0 #{i} est une variable 
            
            while len(temp) > 0 and i < len(temp):
                
                if temp[i]._couleur == couleur:
                    self._deck.append(temp.pop(i))
                    i -= 1
                i += 1

        _trier("Rouge")
        _trier("Bleu")
        _trier("Vert")
        _trier("Jaune")
        _trier("Noir")
        self.affichage2()
        
    