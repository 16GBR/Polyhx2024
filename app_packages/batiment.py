class batiment:
    def __init__(self, couleur, lettre):
        self.couleur = couleur
        self.lettre = lettre

    def afficher_details(self):
        print(f"Couleur: {self.couleur}")

    def afficher_lettre(self):
        return self.lettre
    
    def get_couleur(self):
        return self.couleur