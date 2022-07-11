import getpass
import mysql.connector as mariadb
import time
from interface_connexion import *
from interface_erreur import *
from interface_accueil import *



def espace(i):
    """
    espace(int)-> None
    Simule un grand espace pour faciliter la visibilité
    """
    time.sleep(1)
    for _ in range(i):

        print(" ") 
    
    
def liste_joueur():
    """
    liste_joueur()->list
    renvoie une liste contenant des tuples contenant les id_joueur , pseudo et nb_jetons de tout les joueurs possédant un compte
    """
    req_liste_joueur = """select id_joueur , pseudo , nb_jetons from joueur"""
    cursor.execute(req_liste_joueur)
    return cursor.fetchall()


def get_id_joueur(pseudo , mdp):
    """
    get_id_joueur(pseudo : str , mdp : str) -> list
    renvoie une liste de tuples contenant l'id_joueur du joueur qui a pour pseudo {pseudo} et pour mdp {mdp} si il existe sinon la liste contiendra
    des tuples vide
    """
    req_id_joueur = f"""select id_joueur from joueur where pseudo = '{pseudo}' and mdp = '{mdp}' """
    cursor.execute(req_id_joueur)
    return cursor.fetchall()


def get_joueur(id_joueur):
    """
    get_joueur(id_joueur : int) -> list
    renvoie une liste de tuples contenant les infos (pseudo , nb_jetons ) du joueur qui a pour id_joueur {id_joueur}
    """
    req_joueur = f"""select pseudo , nb_jetons from joueur where id_joueur = '{id_joueur}' """
    cursor.execute(req_joueur)
    return cursor.fetchall()


def update_jetons(id_joueur , jetons):
    """
    update_jetons(id_joueur : int , jetons : int) -> None
    modifie dans la base de donées le nombre de jetons du joueur {id_joueur} par {jetons}
    """
    req_update = f"""update joueur set nb_jetons = '{jetons}' where id_joueur = '{id_joueur}'  """
    cursor.execute(req_update)
    mariadb_connection.commit()


def inscription(infos):
    """
    inscription()-> None
    Cette fonction permet a un joueur de se créer un compte avec le pseudo
    et le mdp qu'il souhaite a condition que le pseudo utilisé ne sois pas déjà utilisé .
    """
    dispo = False
    mdp_valide = False
    
    while dispo == False :
        pseudo = infos[1]
        req_dispo = f"""select pseudo from joueur where pseudo = '{pseudo}'"""
        cursor.execute(req_dispo)
        
        if len(cursor.fetchall()) > 0 :
            interface_erreur_main("Ce pseudo est déjà utiliser choisissez en un autre")
            return None
            
        else :
            dispo = True
            
            while mdp_valide == False :
                mdp = infos[2]
                mdp2 = infos[3]
                
                if mdp == mdp2 :
                    mdp_valide = True
                    
                else :
                    print("Vos mot de passe ne sont pas identique ")
                    
            if (str(input(f"Vous avez choisis en pseudo : {pseudo} êtes vous sur de votre choix ? \n Yes ? \n No ? \n"))).lower() == "yes" :
                req_inscription = """insert into joueur (pseudo , mdp , nb_jetons) values (%s,%s,%s) ; """
                data = [(str(pseudo) , str(mdp) , 100)]
                for item in data :
                    cursor.execute(req_inscription,item)
                    mariadb_connection.commit()
                    return
                
            else :
                dispo = False
                mdp_valide = False
                
                
def connexion(connecter,infos):
    """
    connexion(connecter : bool)-> tupl
    Cette fonction renvoie l'id_joueur d'un joueur une fois qu'il s'est connecter grâce a son pseudo et son mot de passe 
    """
    while not connecter :
        pseudo = infos[1]
        mdp = infos[2]
        #pseudo = "Protodox"
        #mdp = "Protodox"
        id_joueur = get_id_joueur(pseudo , mdp)
        
        if len(id_joueur) > 0 :
            id_joueur = id_joueur[0][0]
            connecter = True
            return (connecter , id_joueur)
        
        else :
            print("Nous n'avons pas trouver de compte correspondant à vos informations . Vérifiez les informations et réesayez .")
            choix = str(input("Si vous ne possédez pas de compte écrivez Inscription sinon si vous avez fait une simple erreur écrivez recommencer .")).lower().strip()
            
            if choix == "inscription":
                return (connecter , None)
            
    
def base_casino_main():
    """
    base_casino_main()->tupl
    cette fonction appele plusieurs fonctions pour pouvoir permettre aux joueurs de se connecter / s'inscrire .
    Avant de renvoyer les infos du joueurs pour qu'ils puissent être utiliser après 
    """
    HOST = "www.assertongue.fr"
    USER = "tnsi3"
    DATABASE = "joueur"
    try:
        global mariadb_connection
        mariadb_connection = mariadb.connect(host=HOST, user=USER, password="s03z", database=DATABASE)
        print(f"Connexion réussie de {USER} sur la base {DATABASE}.")
        # création d'un curseur (mémoire tampon)
        global cursor
        cursor = mariadb_connection.cursor()
    # si pb de connexion
    except mariadb.Error as error:
        print(f"Erreur : {error}")
    print(mariadb_connection)
    #toutes les lignes si dessus permettent de se connecter à une base de données .
    connecter = False
    while connecter == False :
        infos = interface_connexion_main()
            
        if infos[0] == "inscription" :
            inscription(infos)
            connecter = False
            
        
        elif infos[0] == "connexion" :
            resultat = connexion(connecter,infos)
            connecter = resultat[0]
            global id_joueur
            id_joueur = resultat[1]
            
        elif infos[0] == "quitter" :
            return 
            
    info_joueur = get_joueur(id_joueur)
    interface_accueil_main(info_joueur)
    espace(5)
    print(f"Bienvenue {info_joueur[0][0]} vous avez actuellement {info_joueur[0][1]} jetons")
    time.sleep(2)
    espace(5)
    info_joueur.append(id_joueur)
    return info_joueur
            

