from batiment import batiment
from maison import maison
import numpy as np

#Parametres de generation
nb_maisons_needed = 24

#Creation de la map vide
map = np.full((10, 10), None, dtype=object)

nb_maisons = 0

for row in range(map.shape[0]):
    for col in range(map.shape[1]):
        if np.random.rand()>.5 and nb_maisons<nb_maisons_needed:
            map[row, col] = maison(couleur="Bleue", nombre_chambres=3, superficie=150, lettre="M")
            nb_maisons=nb_maisons+1

def affichage_map_avec_lettres(map):
    for ligne in map:
        for element in ligne:
            if element != None:
                print(element.afficher_lettre(), end=' ')
            else:
                print("R", end=' ')
        print()

# Call the function to print the matrix
affichage_map_avec_lettres(map)