from tkinter import *




def quitter():
    window.destroy()
    

    
    
    
    
def interface_erreur_main(message):
    #creation de la fenetre
    global window
    window = Tk()

    #personalisation
    window.title("Erreur")
    window.geometry("480x360")
    window.minsize(480,360)
    window.iconbitmap("Casino.ico")
    window.config(background = "grey")

    #creer une frame (boite)
    global frame
    frame = Frame(window , bg = "Grey")

    #ajouter un premier texte
    label_title = Label(frame, text = message , font = ("Arial", 20) , bg = "grey" , foreground = "white")
    label_title.pack(expand = "yes")


    quit_button = Button(frame , text = "Quitter", font = ("Arial", 10) , bg = "white" , foreground = "grey", command = quitter)
    quit_button.pack(pady = 25)




    #ajouter le frame
    frame.pack(expand = YES)
    
    #affichage
    window.mainloop()
    
    
if __name__ == "__main__" :
    interface_erreur_main("Erreur")

