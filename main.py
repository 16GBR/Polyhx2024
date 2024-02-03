from batiment import batiment
from maison import maison

# Création d'une instance de la classe Maison
ma_maison = maison(couleur="Bleue", nombre_chambres=3, superficie=150, lettre="M")

# Appel de la méthode pour afficher les détails
#ma_maison.afficher_details()
print(ma_maison.afficher_lettre())
