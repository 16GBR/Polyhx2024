from batiment import batiment
from maison import maison
import numpy as np
import plotly.graph_objects as go

import math
from gerener_quartier import centeredAngledElliptic

# Fonction pour voir si point a l'interieur d'une certaine ellipse
def is_point_inside(x_point, y_point, x_shape, y_shape):
    inside = False
    print("x point")
    print(x_point)
    print("y point")
    print(y_point)
    indices_of_value = [index for index, value in enumerate(x_shape) if (value <= x_point+.1 or value >= x_point-.1)]
    #print(indices_of_value)
    if (y_point >= y_shape[indices_of_value[0]] or y_point <= y_shape[indices_of_value[1]]) or (y_point <= y_shape[indices_of_value[0]] or y_point >= y_shape[indices_of_value[1]]) :
        inside = True
    else:
        inside = False
#    if x_point>=min(x_shape) and y_point>=min(y_shape) and x_point<=max(x_shape) and y_point<=max(y_shape):
#        inside = True
#    else:
#        inside = False
    return inside

# Fonction pour creer forme de carre
def creer_carres(center, size):
    x = [center[0] - size / 2, center[0] + size / 2, center[0] + size / 2, center[0] - size / 2, center[0] - size / 2]
    y = [center[1] - size / 2, center[1] - size / 2, center[1] + size / 2, center[1] + size / 2, center[1] - size / 2]
    return x, y

#Parametres de generation
nb_maisons_needed = 24

#Creation de la map vide
map = np.full((10, 10), None, dtype=object)

#Generer ellipse (quartier)
theta, eccentricite, superficie = 120, 0.95, 25
x_ellipse, y_ellipse, a, b, superficie = centeredAngledElliptic(theta, eccentricite, superficie)

nb_maisons = 0

for row in range(map.shape[0]):
    for col in range(map.shape[1]):
        if np.random.rand()>.8 and nb_maisons<nb_maisons_needed:
            map[row, col] = maison(couleur="red", nombre_chambres=3, superficie=150, lettre="M")
            nb_maisons=nb_maisons+1

# Creer des carres
squares = []
for i in range(map.shape[0]):
    for j in range(map.shape[1]):
        x, y = creer_carres(center=(i-map.shape[0]/2, j-map.shape[1]/2), size=1)
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
        if is_point_inside(x[0], y[0], x_ellipse, y_ellipse):
            square = go.Scatter(x=x, y=y, mode='lines',
                            line=dict(color='black'),
                            fill='toself',
                            fillcolor='yellow',
                            hoverinfo='skip')             
        squares.append(square)

# Creer fichier
fig = go.Figure(squares)

# Mettre a jour le layout
fig.update_layout(showlegend=False)

#ajouter l'ellipse au plot
#trace = go.Scatter(x=x, y=y, mode='lines')
x, y, a, b, superficie = centeredAngledElliptic(theta, eccentricite, superficie)
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Line 1'))

#montrer le plot
fig.show()




