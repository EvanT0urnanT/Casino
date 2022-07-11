from tkinter import *

def quitter():
    window.destroy()
    
def valide():
    print(choix_jeux.get(),choix_mise.get())
    
    
def interface_accueil_main(info_joueur):
    #creation de la fenetre
    global window
    window = Tk()

    #personalisation
    window.title("Accueil")
    window.geometry("480x360")
    window.minsize(480,360)
    window.iconbitmap("Casino.ico")
    window.config(background = "grey")

    #creer une frame (boite)
    global frame
    frame = Frame(window , bg = "Grey", bd = 1 , relief = SUNKEN)
    #ajouter un premier texte
    label_title = Label(frame, text = f"Bienvenue à l'accueil {info_joueur[0][0]}", font = ("Arial", 15) , bg = "grey" , foreground = "white")
    label_title.pack()
    
    label_title2 = Label(frame, text = f"Vous possédez {info_joueur[0][1]} jetons", font = ("Arial", 20) , bg = "grey" , foreground = "white")
    label_title2.pack()
    
    

    
    label_texte = Label(frame, text = "Choisissez le jeu au quel vous souhaitez jouer", font = ("Arial", 15) , bg = "grey" , foreground = "white").pack()
    global choix_jeux
    choix_jeux = Spinbox(frame , values = ("Machine à sous" ,"Boites","BlackJack","Uno"), wrap = True)
    choix_jeux.pack()
    
    label_texte2 = Label(frame, text = "Choisissez le nombre de jetons à miser", font = ("Arial", 15) , bg = "grey" , foreground = "white").pack()
    global choix_mise
    choix_mise = Spinbox(frame , from_ = 1 , to = info_joueur[0][1], wrap = True )
    choix_mise.pack()
    valide_button = Button(frame , text = "Valider", font = ("Arial", 10) , bg = "white" , foreground = "grey", command = valide).pack()
    


    quit_button = Button(frame , text = "Sortir", font = ("Arial", 10) , bg = "white" , foreground = "grey", command = quitter)
    quit_button.pack(pady = 25)


    #ajouter le frame
    frame.pack(expand = YES)
    
    #affichage
    window.mainloop()
    
    
if __name__ == "__main__" :
    interface_accueil_main()