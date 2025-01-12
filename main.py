import tkinter as tk
from bataille import BatailleNavaleApp

class main:  
    # Lancement de l'application
    if __name__ == "__main__":
        root = tk.Tk()
        app = BatailleNavaleApp(root)
        app.afficher_menu_accueil()  # Affiche le menu d'accueil
        root.mainloop()