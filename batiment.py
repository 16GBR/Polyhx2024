class batiment:
    def __init__(self, couleur, nombre_chambres, superficie, lettre):
        self.couleur = couleur
        self.nombre_chambres = nombre_chambres
        self.superficie = superficie
        self.lettre = lettre

    def afficher_details(self):
        print(f"Couleur: {self.couleur}, Chambres: {self.nombre_chambres}, Superficie: {self.superficie} m²")

    def afficher_lettre(self):
        return self.lettre
    
    def get_couleur(self):
        return self.couleur