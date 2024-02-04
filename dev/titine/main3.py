from batiment import batiment
from maison import maison
import numpy as np
import plotly.graph_objects as go

import math
from gerener_quartier import centeredAngledElliptic

# Fonction pour voir si point a l'interieur d'une certaine ellipse
def is_point_inside(x_point, y_point, x_shape, y_shape):
    inside = False
    #get_indexes = lambda x_shape, xs: [i for (y, i) in zip(xs, range(len(xs))) if x_shape == y]
    #print(get_indexes(x_point,x_shape))
    #indices_of_value = [index for index, value in enumerate(x_shape) if (value <= x_point+.1 and value >= x_point-.1)]
    indices_of_value=[1,1]
    
    if (y_point >= y_shape[indices_of_value[0]] and y_point <= y_shape[indices_of_value[1]]) or (y_point <= y_shape[indices_of_value[0]] and y_point >= y_shape[indices_of_value[1]]) :
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
nb_maisons_type1_needed = 5775
nb_maisons_type2_needed = 1890
nb_epicerie_needed = 300
nb_job_needed = 200
nb_ecole_needed = 80*6 #car bloc de 2x3
nb_centre_loisir_needed = 160*2 #car bloc de 1x2
nb_boutique_needed = 300
nb_retail_needed = 100*2

etage_plex = 3
etage_appart = 6

#Creation de la map vide
map = np.full((100, 100), None, dtype=object)

#Generer ellipse (quartier)
theta, eccentricite, superficie = 120, 0.95, 25
x_ellipse, y_ellipse, a, b, superficie = centeredAngledElliptic(theta, eccentricite, superficie)

nb_maisons_type1 = 0
nb_maisons_type2 = 0
nb_epicerie = 0
nb_job = 0
nb_ecole = 0
nb_centre_loisir = 0
nb_boutique = 0
nb_retail = 0

#ECOLE
while nb_ecole<nb_ecole_needed: 
    coord_x = int(np.floor(np.random.rand()*map.shape[0]))
    coord_y = int(np.floor(np.random.rand()*map.shape[1]))
    pile_face = np.random.rand()
    if pile_face<=.5 and coord_x+1<map.shape[0] and coord_y+2<map.shape[1] and map[coord_x, coord_y] == None and map[coord_x, coord_y+1] == None and map[coord_x, coord_y+2] == None and map[coord_x+1, coord_y] == None and map[coord_x+1, coord_y+1] and map[coord_x+1, coord_y+2] == None:#2x3
        map[coord_x, coord_y] = batiment(couleur="gold", lettre="Ec")
        map[coord_x, coord_y+1] = batiment(couleur="gold", lettre="Ec")
        map[coord_x, coord_y+2] = batiment(couleur="gold", lettre="Ec")
        map[coord_x+1, coord_y] = batiment(couleur="gold", lettre="Ec")
        map[coord_x+1, coord_y+1] = batiment(couleur="gold", lettre="Ec")
        map[coord_x+1, coord_y+2] = batiment(couleur="gold", lettre="Ec")
        nb_ecole=nb_ecole+6
    elif coord_x+2<map.shape[0] and coord_y+1<map.shape[1] and map[coord_x, coord_y]== None and map[coord_x+1, coord_y]== None and map[coord_x+2, coord_y]== None and map[coord_x, coord_y+1]== None and map[coord_x+1, coord_y+1]== None and map[coord_x+2, coord_y+1]== None: #3x2
        map[coord_x, coord_y] = batiment(couleur="gold", lettre="Ec")
        map[coord_x+1, coord_y] = batiment(couleur="gold", lettre="Ec")
        map[coord_x+2, coord_y] = batiment(couleur="gold", lettre="Ec")
        map[coord_x, coord_y+1] = batiment(couleur="gold", lettre="Ec")
        map[coord_x+1, coord_y+1] = batiment(couleur="gold", lettre="Ec")
        map[coord_x+2, coord_y+1] = batiment(couleur="gold", lettre="Ec")
        nb_ecole=nb_ecole+6

#CENTRE LOISIR
while nb_centre_loisir<nb_centre_loisir_needed: 
    coord_x = int(np.floor(np.random.rand()*map.shape[0]))
    coord_y = int(np.floor(np.random.rand()*map.shape[1]))
    pile_face = np.random.rand()
    if pile_face<=.5 and coord_x+1<map.shape[0] and coord_y+1<map.shape[1] and map[coord_x, coord_y] == None and map[coord_x+1, coord_y] == None and map[coord_x, coord_y+1] == None:#2x1
        map[coord_x, coord_y] = batiment(couleur="blue", lettre="C")
        map[coord_x+1, coord_y] = batiment(couleur="blue", lettre="C")
        nb_centre_loisir=nb_centre_loisir+2 
    elif coord_y+1<map.shape[1] and coord_x+1<map.shape[0] and map[coord_x, coord_y] == None and map[coord_x+1, coord_y] == None and map[coord_x, coord_y+1] == None: #1x2
        map[coord_x, coord_y] = batiment(couleur="blue", lettre="C")
        map[coord_x, coord_y+1] = batiment(couleur="blue", lettre="C")
        nb_centre_loisir=nb_centre_loisir+2 

#RETAIL
while nb_retail<nb_retail_needed: 
    coord_x = int(np.floor(np.random.rand()*map.shape[0]))
    coord_y = int(np.floor(np.random.rand()*map.shape[1]))
    pile_face = np.random.rand()
    if pile_face<=.5 and (coord_x+1)<map.shape[0] and coord_y+1<map.shape[1] and map[coord_x, coord_y] == None and map[coord_x+1, coord_y] == None and map[coord_x, coord_y+1] == None:#2x1
        map[coord_x, coord_y] = batiment(couleur="black", lettre="R")
        map[coord_x+1, coord_y] = batiment(couleur="black", lettre="R")
        nb_retail=nb_retail+2 
    elif coord_y+1<map.shape[1] and coord_x+1<map.shape[0] and map[coord_x, coord_y] == None and map[coord_x+1, coord_y] == None and map[coord_x, coord_y+1] == None: #1x2
        map[coord_x, coord_y] = batiment(couleur="black", lettre="R")
        map[coord_x, coord_y+1] = batiment(couleur="black", lettre="R")
        nb_retail=nb_retail+2 

#BOUTIQUE
while nb_boutique<nb_boutique_needed: 
    coord_x = int(np.floor(np.random.rand()*map.shape[0]))
    coord_y = int(np.floor(np.random.rand()*map.shape[1]))
    if map[coord_x, coord_y] == None:
        map[coord_x, coord_y] = batiment(couleur="darkgray", lettre="B")
        nb_boutique=nb_boutique+1 

#JOB
while nb_job<nb_job_needed: 
    coord_x = int(np.floor(np.random.rand()*map.shape[0]))
    coord_y = int(np.floor(np.random.rand()*map.shape[1]))
    if map[coord_x, coord_y] == None:
        map[coord_x, coord_y] = batiment(couleur="magenta", lettre="J")
        nb_job=nb_job+1 

#EPICERIE
while nb_epicerie<nb_epicerie_needed: 
    coord_x = int(np.floor(np.random.rand()*map.shape[0]))
    coord_y = int(np.floor(np.random.rand()*map.shape[1]))
    if map[coord_x, coord_y] == None:
        map[coord_x, coord_y] = batiment(couleur="brown", lettre="Ep")
        nb_epicerie=nb_epicerie+1 

#MAISONS TYPE 2
while nb_maisons_type2<nb_maisons_type2_needed: 
    coord_x = int(np.floor(np.random.rand()*map.shape[0]))
    coord_y = int(np.floor(np.random.rand()*map.shape[1]))
    if map[coord_x, coord_y] == None:
        map[coord_x, coord_y] = batiment(couleur="salmon", lettre="M2")
        nb_maisons_type2=nb_maisons_type2+1 

#MAISONS TYPE 1
while nb_maisons_type1<nb_maisons_type1_needed: 
    coord_x = int(np.floor(np.random.rand()*map.shape[0]))
    coord_y = int(np.floor(np.random.rand()*map.shape[1]))
    if map[coord_x, coord_y] == None:
        map[coord_x, coord_y] = batiment(couleur="red", lettre="M1")
        nb_maisons_type1=nb_maisons_type1+1    


#fill les trous de parc
for coord_x in range(map.shape[0]):
    for coord_y in range(map.shape[1]):
        if map[coord_x, coord_y] == None:
            map[coord_x, coord_y] = batiment(couleur="green", lettre="P")
         
            
def dist_mesure(lettre):
    dist_min = 1000
    for i in range(map.shape[0]):
                for j in range(map.shape[1]):
                    if map[i, j].afficher_lettre() == lettre:
                        dist = abs(i-coord_x)+abs(j-coord_y)
                        if dist<dist_min:
                            dist_min=dist
    return dist_min

print("Calcul du temps")
#trouver le temps de deplacement pour chaque maison
vit_moy=1.5 # m/s
facteur_distance = 40 #m
liste_temps_M1 = [] 
liste_temps_M2 = []            
for row in range(map.shape[0]):
    for col in range(map.shape[1]):
        if map[row, col].afficher_lettre() == "M1":
            temps = np.zeros(7)                           
            temps[0]=dist_mesure("P")/vit_moy*facteur_distance
            temps[1]=dist_mesure("J")/vit_moy*facteur_distance
            temps[2]=dist_mesure("Ec")/vit_moy*facteur_distance
            temps[3]=dist_mesure("C")/vit_moy*facteur_distance
            temps[4]=dist_mesure("Ep")/vit_moy*facteur_distance
            temps[5]=dist_mesure("B")/vit_moy*facteur_distance
            temps[6]=dist_mesure("R")/vit_moy*facteur_distance
            liste_temps_M1.append(temps)
        if map[row, col].afficher_lettre() == "M2":
            temps = np.zeros(7)                           
            temps[0]=dist_mesure("P")/vit_moy*facteur_distance
            temps[1]=dist_mesure("J")/vit_moy*facteur_distance
            temps[2]=dist_mesure("Ec")/vit_moy*facteur_distance
            temps[3]=dist_mesure("C")/vit_moy*facteur_distance
            temps[4]=dist_mesure("Ep")/vit_moy*facteur_distance
            temps[5]=dist_mesure("B")/vit_moy*facteur_distance
            temps[6]=dist_mesure("R")/vit_moy*facteur_distance
            liste_temps_M2.append(temps)

#Calculer le social credit pour la map generee
ratio=[2/7, 5/7, 5/7, 2/7, 1/7, .5/7, .5/7]
den_ratio = 16/7

print("Calcul du social credit")
social_credit = 0
sum_all_house = 0
for liste in liste_temps_M1:
    sum = 0
    for i in range(liste.shape[0]):
        sum = sum+temps[i]*ratio[i]
    sum_all_house = sum_all_house+sum/den_ratio*10*etage_plex

for liste in liste_temps_M2:
    sum = 0
    for i in range(liste.shape[0]):
        sum = sum+temps[i]*ratio[i]
    sum_all_house = sum_all_house+sum/den_ratio*(20*etage_appart)

social_credit = sum_all_house/(nb_maisons_type1_needed*10*etage_plex + nb_maisons_type2_needed*(20*etage_appart))
print(social_credit)

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
#x, y, a, b, superficie = centeredAngledElliptic(theta, eccentricite, superficie)
#fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Line 1'))

#montrer le plot
fig.show()