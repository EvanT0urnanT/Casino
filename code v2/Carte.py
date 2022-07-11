""""

Carte

"""

class Carte():
    def __init__(self, couleur, numero):
        """
        init(self : instance , couleur : str , numero : int) -> None
        créer une instance de la class {Carte} puis attribut à l'instance {self} les attributs {couleur} et {numero}
        """
        self._couleur = couleur
        self._numero = numero