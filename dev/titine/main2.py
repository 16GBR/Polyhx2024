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

def check_tout_est_place(nb_maisons_type1, nb_maisons_type2, nb_epicerie, nb_job, nb_ecole, nb_centre_loisir, nb_boutique, nb_retail):
    everything_is_there = True

    if nb_maisons_type1<nb_maisons_type1_needed:
        everything_is_there = False
    if nb_maisons_type2<nb_maisons_type2_needed:
        everything_is_there = False
    if nb_epicerie<nb_epicerie_needed:
        everything_is_there = False
    if nb_job<nb_job_needed:
        everything_is_there = False
    if nb_ecole<nb_ecole_needed:
        everything_is_there = False
    if nb_centre_loisir<nb_centre_loisir_needed:
        everything_is_there = False
    if nb_boutique<nb_boutique_needed:
        everything_is_there = False
    if nb_retail<nb_retail_needed:
        everything_is_there = False

    return everything_is_there

#Parametres de generation
nb_maisons_type1_needed = 224
nb_maisons_type2_needed = 100
nb_epicerie_needed = 20
nb_job_needed = 15
nb_ecole_needed = 4*6 #car bloc de 2x3
nb_centre_loisir_needed = 5
nb_boutique_needed = 5
nb_retail_needed = 5

#Creation de la map vide
map = np.full((20, 20), None, dtype=object)

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

while check_tout_est_place(nb_maisons_type1, nb_maisons_type2, nb_epicerie, nb_job, nb_ecole, nb_centre_loisir, nb_boutique, nb_retail) == False:
    for row in range(map.shape[0]):
        for col in range(map.shape[1]):
            #numb = np.floor(np.random.rand()*10)
            numb = np.random.rand()*10
            if numb <=6 and nb_maisons_type1<nb_maisons_type1_needed and map[row, col] == None:
                map[row, col] = batiment(couleur="red", lettre="M1")
                nb_maisons_type1=nb_maisons_type1+1   
            elif numb <=9 and nb_maisons_type2<nb_maisons_type2_needed and map[row, col] == None:
                map[row, col] = batiment(couleur="salmon", lettre="M2")
                nb_maisons_type2=nb_maisons_type2+1    
            elif numb <=9.1 and nb_epicerie<nb_epicerie_needed and map[row, col] == None:
                map[row, col] = batiment(couleur="brown", lettre="Ep")
                nb_epicerie=nb_epicerie+1  
            elif numb <=9.3 and nb_job<nb_job_needed and map[row, col] == None:
                map[row, col] = batiment(couleur="magenta", lettre="J")
                nb_job=nb_job+1  
            elif numb <=9.4 and nb_ecole<nb_ecole_needed and map[row, col] == None:
                pile_face = np.random.rand()
                if pile_face<=.5 and row+1<map.shape[0] and col+2<map.shape[1]:#2x3
                    map[row, col] = batiment(couleur="gold", lettre="Ec")
                    map[row, col+1] = batiment(couleur="gold", lettre="Ec")
                    map[row, col+2] = batiment(couleur="gold", lettre="Ec")
                    map[row+1, col] = batiment(couleur="gold", lettre="Ec")
                    map[row+1, col+1] = batiment(couleur="gold", lettre="Ec")
                    map[row+1, col+2] = batiment(couleur="gold", lettre="Ec")
                    nb_ecole=nb_ecole+6
                elif row+2<map.shape[0] and col+1<map.shape[1]: #3x2
                    map[row, col] = batiment(couleur="gold", lettre="Ec")
                    map[row+1, col] = batiment(couleur="gold", lettre="Ec")
                    map[row+2, col] = batiment(couleur="gold", lettre="Ec")
                    map[row, col+1] = batiment(couleur="gold", lettre="Ec")
                    map[row+1, col+1] = batiment(couleur="gold", lettre="Ec")
                    map[row+2, col+1] = batiment(couleur="gold", lettre="Ec")
                    nb_ecole=nb_ecole+6
            elif numb <=9.5 and nb_centre_loisir<nb_centre_loisir_needed and map[row, col] == None:
                map[row, col] = batiment(couleur="khaki", lettre="C")
                nb_centre_loisir=nb_centre_loisir+1  
            elif numb <= 9.6 and nb_boutique<nb_boutique_needed and map[row, col] == None:
                map[row, col] = batiment(couleur="darkgray", lettre="B")
                nb_boutique=nb_boutique+1  
            elif numb <=9.7 and nb_retail<nb_retail_needed and map[row, col] == None:
                map[row, col] = batiment(couleur="black", lettre="R")
                nb_retail=nb_retail+1  

#fill les trous de parc
for row in range(map.shape[0]):
    for col in range(map.shape[1]):
        if map[row, col] == None:
            map[row, col] = batiment(couleur="green", lettre="P")


def dist_mesure(lettre):
    dist_min = 1000
    for i in range(map.shape[0]):
                for j in range(map.shape[1]):
                    if map[i, j].afficher_lettre() == lettre:
                        dist = abs(i-row)+abs(j-col)
                        if dist<dist_min:
                            dist_min=dist
    return dist_min

#trouver le temps de deplacement pour chaque maison
vit_moy=1.5 # m/s
facteur_distance = 40 #m
liste_temps_M1 = [] 
liste_temps_M2 = []            
for row in range(map.shape[0]):
    for col in range(map.shape[1]):
        if map[row, col].afficher_lettre() == "M1":
            temps = np.zeros(7)                           
            temps[0]=dist_mesure("P")*vit_moy*facteur_distance
            temps[1]=dist_mesure("J")*vit_moy*facteur_distance
            temps[2]=dist_mesure("Ec")*vit_moy*facteur_distance
            temps[3]=dist_mesure("C")*vit_moy*facteur_distance
            temps[4]=dist_mesure("Ep")*vit_moy*facteur_distance
            temps[5]=dist_mesure("B")*vit_moy*facteur_distance
            temps[6]=dist_mesure("R")*vit_moy*facteur_distance
            liste_temps_M1.append(temps)
        if map[row, col].afficher_lettre() == "M2":
            temps = np.zeros(7)                           
            temps[0]=dist_mesure("P")*vit_moy*facteur_distance
            temps[1]=dist_mesure("J")*vit_moy*facteur_distance
            temps[2]=dist_mesure("Ec")*vit_moy*facteur_distance
            temps[3]=dist_mesure("C")*vit_moy*facteur_distance
            temps[4]=dist_mesure("Ep")*vit_moy*facteur_distance
            temps[5]=dist_mesure("B")*vit_moy*facteur_distance
            temps[6]=dist_mesure("R")*vit_moy*facteur_distance
            liste_temps_M2.append(temps)

#Calculer le social credit pour la map generee
ratio=[2/7, 5/7, 5/7, 2/7, 1/7, .5/7, .5/7]
ratio = ratio
den_ratio = 16/7

social_credit = 0
sum_all_house = 0
for liste in liste_temps_M1:
    sum = 0
    for i in range(liste.shape[0]):
        sum = sum+temps[i]*ratio[i]
    sum_all_house = sum_all_house+sum/den_ratio

for liste in liste_temps_M2:
    sum = 0
    for i in range(liste.shape[0]):
        sum = sum+temps[i]*ratio[i]
    sum_all_house = sum_all_house+sum/den_ratio

social_credit = sum_all_house/(nb_maisons_type1_needed + nb_maisons_type2_needed)
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




