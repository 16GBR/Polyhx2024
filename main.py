from batiment import batiment
from maison import maison
import numpy as np

# Création d'une instance de la classe Maison
ma_maison = maison(couleur="Bleue", nombre_chambres=3, superficie=150, lettre="M")

map = np.full((10, 10), None, dtype=object)

for row in range(map.shape[0]):
    for col in range(map.shape[1]):
        map[row, col] = maison(couleur="Bleue", nombre_chambres=3, superficie=150, lettre="M")

def affichage_map_avec_lettres(map):
    for ligne in map:
        for element in ligne:
            print(element.afficher_lettre(), end=' ')
        print()

# Call the function to print the matrix
affichage_map_avec_lettres(map)