from batiment import batiment

class maison(batiment):
    def __init__(self, couleur, nombre_chambres, superficie, lettre):
        super().__init__(couleur, nombre_chambres, superficie, lettre)
