from tkinter import *
from interface_inscription import *




def quitter():
    global infos_connexion
    infos_connexion = ["quitter" ]
    window.destroy()
    
    
def connexion():
    global infos_connexion
    infos_connexion = ["connexion" , entry1.get(), entry2.get()]
    window.destroy()
    
def inscription():
    global infos_connexion
    window.destroy()
    infos_connexion = interface_inscription_main()
    
    
    
def interface_connexion_main():
    #creation de la fenetre
    global window
    window = Tk()

    #personalisation
    window.title("Connexion")
    window.geometry("480x360")
    window.minsize(480,360)
    window.iconbitmap("Casino.ico")
    window.config(background = "grey")

    #creer une frame (boite)
    global frame
    frame = Frame(window , bg = "Grey", bd = 1 , relief = SUNKEN)

    #ajouter un premier texte
    label_title = Label(frame, text = "Bienvenue au casino", font = ("Arial", 20) , bg = "grey" , foreground = "white")
    label_title.pack()


    #entry
    label_title = Label(frame, text = "Username", font = ("Arial", 10) , bg = "grey" , foreground = "white")
    label_title.pack()
    
    global entry1
    entry1 = Entry(frame , width = 20)
    entry1.pack()

    label_title = Label(frame, text = "Mot de Passe", font = ("Arial", 10) , bg = "grey" , foreground = "white")
    label_title.pack()
    
    global entry2
    entry2 = Entry(frame , width = 20, show = "*")
    entry2.pack()

    connexion_button = Button (frame , text = "Connexion", font = ("Arial" ,10) , bg = "White" , fg = "grey" , command = connexion)
    connexion_button.pack(pady = 10)
    
    inscription_button = Button (frame , text = "Inscription", font = ("Arial" ,10) , bg = "White" , fg = "grey" , command = inscription)
    inscription_button.pack(pady = 10)

    #ajouter un premier bouton
    quit_button = Button(frame , text = "Quitter", font = ("Arial", 10) , bg = "white" , foreground = "grey", command = quitter)
    quit_button.pack(pady = 25)




    #ajouter le frame
    frame.pack(expand = YES)
    
    #affichage
    window.mainloop()
    return infos_connexion
    
    
if __name__ == "__main__" :
    interface_connexion_main()
