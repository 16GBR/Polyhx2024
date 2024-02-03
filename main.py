from batiment import batiment
from maison import maison
import numpy as np
import plotly.graph_objects as go

#Parametres de generation
nb_maisons_needed = 24

#Creation de la map vide
map = np.full((10, 10), None, dtype=object)

nb_maisons = 0

for row in range(map.shape[0]):
    for col in range(map.shape[1]):
        if np.random.rand()>.8 and nb_maisons<nb_maisons_needed:
            map[row, col] = maison(couleur="red", nombre_chambres=3, superficie=150, lettre="M")
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

# Fonction pour creer forme de carre
def creer_carres(center, size):
    x = [center[0] - size / 2, center[0] + size / 2, center[0] + size / 2, center[0] - size / 2, center[0] - size / 2]
    y = [center[1] - size / 2, center[1] - size / 2, center[1] + size / 2, center[1] + size / 2, center[1] - size / 2]
    return x, y

# Creer des carres
squares = []
for i in range(map.shape[0]):
    for j in range(map.shape[1]):
        x, y = creer_carres(center=(i, j), size=1)
        if map[i, j] != None:
            square = go.Scatter(x=x, y=y, mode='lines',
                            line=dict(color='black'),
                            fill='toself',
                            fillcolor=map[i, j].get_couleur(),
                            hoverinfo='skip')
        else:
            square = go.Scatter(x=x, y=y, mode='lines',
                            line=dict(color='black'),
                            fill='toself',
                            fillcolor='lightblue',
                            hoverinfo='skip')            
        squares.append(square)

# Creer fichier
fig = go.Figure(squares)

# Mettre a jour le layout
fig.update_layout(showlegend=False)

# Montrer la figure
fig.show()
