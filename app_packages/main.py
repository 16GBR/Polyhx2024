from .batiment import batiment
import numpy as np
import plotly.graph_objects as go

import math
from .gerener_quartier import centeredAngledElliptic
from .stats import diagramme_bande, pie_chart
from .gen_gltf import gen_gltf

#from dev.titine.gen_gltf import gen_gltf

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
    return inside

# Fonction pour creer forme de carre
def creer_carres(center, size):
    x = [center[0] - size / 2, center[0] + size / 2, center[0] + size / 2, center[0] - size / 2, center[0] - size / 2]
    y = [center[1] - size / 2, center[1] - size / 2, center[1] + size / 2, center[1] + size / 2, center[1] - size / 2]
    return x, y

def dist_mesure(lettre, row, col, map):
    dist_min = 1000
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            if map[i, j].afficher_lettre() == lettre:
                dist = abs(i-row)+abs(j-col)
                if dist<dist_min:
                    dist_min=dist
    return dist_min

def main(zoning):

    #Parametres de generation
    grid_size_x = zoning[0].shape[0]
    grid_size_y = zoning[0].shape[1]

    nb_maisons_type1_needed = zoning[7]
    nb_maisons_type2_needed = zoning[9]
    nb_epicerie_needed = zoning[3]
    nb_job_needed = zoning[5]
    nb_ecole_needed = zoning[1]
    nb_centre_loisir_needed = zoning[2]
    nb_boutique_needed = zoning[4]
    nb_retail_needed = zoning[6]

    etage_plex = zoning[8]
    etage_appart = zoning[10]

    target_population = zoning[11]

    #Creation de la map vide
    map = np.full((grid_size_x, grid_size_y), None, dtype=object)

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
    nb_park=0

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
                nb_park = nb_park+1




    print("Calcul du temps")
    #trouver le temps de deplacement pour chaque maison
    vit_moy=1.34 # m/s
    facteur_distance = 40 #m
    liste_temps_M1 = [] 
    liste_temps_M2 = []            
    for row in range(map.shape[0]):
        for col in range(map.shape[1]):
            if map[row, col].afficher_lettre() == "M1":
                temps = np.zeros(7)                           
                temps[0]=dist_mesure("P",row,col,map)/vit_moy*facteur_distance
                temps[1]=dist_mesure("J",row,col,map)/vit_moy*facteur_distance
                temps[2]=dist_mesure("Ec",row,col,map)/vit_moy*facteur_distance
                temps[3]=dist_mesure("C",row,col,map)/vit_moy*facteur_distance
                temps[4]=dist_mesure("Ep",row,col,map)/vit_moy*facteur_distance
                temps[5]=dist_mesure("B",row,col,map)/vit_moy*facteur_distance
                temps[6]=dist_mesure("R",row,col,map)/vit_moy*facteur_distance
                liste_temps_M1.append(temps)
            if map[row, col].afficher_lettre() == "M2":
                temps = np.zeros(7)                           
                temps[0]=dist_mesure("P",row,col,map)/vit_moy*facteur_distance
                temps[1]=dist_mesure("J",row,col,map)/vit_moy*facteur_distance
                temps[2]=dist_mesure("Ec",row,col,map)/vit_moy*facteur_distance
                temps[3]=dist_mesure("C",row,col,map)/vit_moy*facteur_distance
                temps[4]=dist_mesure("Ep",row,col,map)/vit_moy*facteur_distance
                temps[5]=dist_mesure("B",row,col,map)/vit_moy*facteur_distance
                temps[6]=dist_mesure("R",row,col,map)/vit_moy*facteur_distance
                liste_temps_M2.append(temps)

    #Calculer le social credit pour la map generee
    ratio=[2/7, 0/7, 5/7, 2/7, 1/7, .5/7, .5/7]
    den_ratio = 11/7

    #cas erreur pour pas crash
    if nb_maisons_type1_needed ==0:
        nb_maisons_type1_needed=1
    if nb_maisons_type2_needed ==0:
        nb_maisons_type2_needed=1
    if etage_plex ==0:
        etage_plex=1
    if etage_appart==0:
        etage_appart=1

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
                                fillcolor='orange',
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

    #generation array pour 3D
    grid_3D = np.empty((grid_size_x, grid_size_y), dtype='U10')

    for coord_x in range(map.shape[0]):
        for coord_y in range(map.shape[1]):
            grid_3D[coord_x, coord_y] = map[coord_x, coord_y].afficher_lettre()
    
    gen_gltf(grid_3D)


    #stats
    nbPlex = nb_maisons_type1_needed
    nbApparts = nb_maisons_type2_needed
    nbEpiceries = nb_epicerie_needed
    nbBureaux = nb_job_needed
    nbEcole = nb_ecole_needed
    nbLoisirs = nb_centre_loisir_needed
    nbBoutique = nb_boutique_needed
    nbRetail = nb_retail_needed
    etagesPlex = etage_plex
    etagesApparts = etage_appart
    nbPark = nb_park

    diagramme_bande(nbEcole, nbLoisirs, nbEpiceries, nbBoutique, nbBureaux, nbRetail, nbPlex, etagesPlex, nbApparts, etagesApparts,nbPark)
    pie_chart(nbEcole, nbLoisirs, nbEpiceries, nbBoutique, nbBureaux, nbRetail, nbPlex, etagesPlex, nbApparts, etagesApparts, nbPark)


    minutes, seconds = divmod(social_credit, 60)
    return f"{int(minutes)} min {int(seconds)} sec"