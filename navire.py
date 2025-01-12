class Navire:
    def __init__(self, nom, taille):
        """
        Initialise un navire avec un nom, une taille, et garde en mémoire ses positions.
        """
        self.nom = nom
        self.taille = taille
        self.positions = []  # Positions occupées par le navire
        self.touchees = []  # Positions touchées
        self.est_coule_flag = False  # État du navire (coulé ou non)

    def ajouter_positions(self, positions):
        """
        Définit les positions du navire.
        """
        self.positions = positions
        print(f"[LOG] Navire {self.nom} placé aux positions : {self.positions}")

    def est_touche(self, position):
        """
        Marque une position comme touchée.
        """
        if position in self.positions and position not in self.touchees:
            self.touchees.append(position)
            print(f"[LOG] Navire {self.nom} touché à la position : {position}")
        else:
            print(f"[LOG] Navire {self.nom} déjà touché ou position invalide : {position}")

    def verifier_etat(self):
        """
        Vérifie si le navire est complètement coulé.
        """
        if all(position in self.touchees for position in self.positions):
            self.est_coule_flag = True
            print(f"[LOG] Navire {self.nom} est maintenant coulé avec succès.")
            return True
        return False
