class Plateau:
    def __init__(self, taille=10):
        """
        Initialise un plateau de jeu avec une grille.
        """
        self.taille = taille
        self.grille = [[None for _ in range(taille)] for _ in range(taille)]
        self.navires = []  # Liste des navires placés

    def est_position_valide(self, positions):
        """
        Vérifie si toutes les positions sont valides (dans la grille et libres).
        """
        for x, y in positions:
            if not (0 <= x < self.taille and 0 <= y < self.taille) or self.grille[x][y] is not None:
                return False
        return True

    def placer_navire(self, navire, positions):
        """
        Place un navire sur le plateau.
        """
        if self.est_position_valide(positions):
            for x, y in positions:
                self.grille[x][y] = navire
            navire.ajouter_positions(positions)
            self.navires.append(navire)
            return True
        return False

    def tirer(self, position):
        """
        Tente un tir sur une position.
        """
        x, y = position
        if not (0 <= x < self.taille and 0 <= y < self.taille):
            print(f"[LOG] Position {position} invalide pour un tir.")
            return "invalide"

        if self.grille[x][y] is None:
            print(f"[LOG] Tir à la position {position} manqué.")
            return "manqué"
        else:
            navire = self.grille[x][y]
            navire.est_touche(position)
            print(f"[LOG] Positions du navire {navire.nom} : {navire.positions}")
            print(f"[LOG] Positions touchées : {navire.touchees}")

            if navire.verifier_etat():
                print(f"[LOG] Navire {navire.nom} coulé avec succès.")
                return "coulé"
            print(f"[LOG] Tir à la position {position} a touché le navire {navire.nom}.")
            return "touché"