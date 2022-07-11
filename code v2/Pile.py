""""

Pile

"""

class Pile(): 
    """
    Simule une structure de pile à l'aide d'un tableau et un pointeur sur le sommet de la pile.
    """


    #constructeur
    def __init__(self, max):
        """
        __init__(self : Pile , max : int)-> None
        créer une instance de la class {Pile} de taille maximum {max} puis attribut à l'instance {self} l'attribut {sommet}
        """
        self.sommet = 0     #pointe sur l'emplacement où sera empilé le prochain élément
        self.pile = [0] * max 
    
    
    def est_vide(self): #méthode vérifiant si l'instance {self} est vide , renvoie True si c le cas , sinon renvoie false 
        """
        est_vide(self: Pile) -> Bool
        teste si la pile est vide
        """
        return self.sommet == 0 
    
    
    def empile(self, x): #méthode ajoutant {x} a l'index self.sommet 
        """
        empile(self: Pile, x: Élement) -> None
        Ajoute x au sommet de p
        """
        try :
            self.pile[self.sommet] = x 
            self.sommet = self.sommet + 1
        
        except :
            print("La pile est pleine")
        
        return None
    
    
    def depile(self): #méthode enlevant et renvoyant le dernier élément de l'instance de la Classe {Pile} (equivalent du .pop() pour une liste)      Pile = FILO (First In Last Out)
        """
        depile(self: Pile) -> Élément
        Enlève et renvoie l'objet au sommet de p
        """
        #génére une AssertionError si la pile est vide
        assert not(self.est_vide()),"Pile vide"
        self.sommet = self.sommet - 1
        return self.pile[self.sommet]
    
    
    def taille(self):
        """
        taille(self: Pile) -> int 
        Renvoie un entier correspondant aux nombres d'éléments dans {self}
        """
        return self.sommet
        

    def vider(self):
        """
        vider(self: Pile) -> None
        Vide tous les éléments de {self} , mais ne les renvoient pas 

        """
        self.sommet = 0 #Lorsque nous vidons une Pile nous enlevons pas chaque élément on met juste le curseur {self.sommet} a 0 ce qui va donc écraser au fur et a mesure les anciens éléments .
        return None