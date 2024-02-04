import numpy as np
import pygltflib
from .copy_move_merge_gltf import copy_and_modify_gltf, modify_function

def gen_gltf(map):
    print(map)
    #map : np.array(strings)

    x_size = int(map.shape[0])
    y_size = int(map.shape[1])

    grid_to_nodes = 1

    input_gltf_path = "3D_Models/Models.gltf"
    output_gltf_path = "static/model/output.glb"

    nb_M1 = np.count_nonzero(map=="M1")
    positions_M1 = np.zeros([nb_M1,2])
    index_M1 = 0

    nb_M2 = np.count_nonzero(map=="M2")
    positions_M2 = np.zeros([nb_M2,2])
    index_M2 = 0
    
    nb_B = np.count_nonzero(map=="B")
    positions_B = np.zeros([nb_B,2])
    index_B = 0
    
    nb_J = np.count_nonzero(map=="J")
    positions_J = np.zeros([nb_J,2])
    index_J = 0
    
    nb_Ep = np.count_nonzero(map=="Ep")
    positions_Ep = np.zeros([nb_Ep,2])
    index_Ep = 0

    nb_P = int(np.count_nonzero(map=="P"))
    positions_P = np.zeros([nb_P,2])
    index_P = 0

    nb_Ec = int(np.count_nonzero(map=="Ec")/6)
    positions_Ec = np.zeros([nb_Ec,2])
    index_Ec = 0

    # Centres communautaires
    nb_C1=0
    nb_C2=0

    map_temp=np.copy(map)

    for i in range(map_temp.shape[0]):
        for j in range(map_temp.shape[1]):
            if map_temp[i,j] == "C":
                if i+1<=map_temp.shape[0]-1:
                    if map_temp[i+1,j]=="C":
                        map_temp[i+1,j]="0"
                        nb_C1+=1
                    else:
                        map_temp[i,j+1]="0"
                        nb_C2+=1

    #nb_C1 = int(np.count_nonzero(map=="C")/2)
    positions_C1 = np.zeros([nb_C1,2])
    index_C1 = 0

    positions_C2 = np.zeros([nb_C2,2])
    index_C2 = 0
    
    #Retail
    nb_R1=0
    nb_R2=0

    map_temp=np.copy(map)

    for i in range(map_temp.shape[0]):
        for j in range(map_temp.shape[1]):
            if map_temp[i,j] == "R":
                if i+1<=map_temp.shape[0]-1:
                    if map_temp[i+1,j]=="R":
                        map_temp[i+1,j]="0"
                        nb_R1+=1
                    else:
                        map_temp[i,j+1]="0"
                        nb_R2+=1

    positions_R1 = np.zeros([nb_R1,2])
    index_R1 = 0

    positions_R2 = np.zeros([nb_R2,2])
    index_R2 = 0


    liste_lettres=["M1, M2, B, J, Ep, P, Ec, C, R"]
    liste_noms=["APlex_1x1","ABloc_1x1","BStore_1x1" ,"Work_1x1","GStore_1x1", "Park_1x1", "School_2x3", "SCenter_2x1", "SCenter_1x2", "RStore_2x1", "RStore_1x2"]
    liste_postitions=[positions_M1, positions_M2, positions_B, positions_J, positions_Ep, positions_P, positions_Ec, positions_C1, positions_C2, positions_R1, positions_R2]

    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            if map[i,j]=="M1":
                positions_M1[index_M1,0]=i
                positions_M1[index_M1,1]=j
                index_M1+=1
            elif map[i,j]=="M2":
                positions_M2[index_M2,0]=i
                positions_M2[index_M2,1]=j
                index_M2+=1
            elif map[i,j]=="B":
                positions_B[index_B,0]=i
                positions_B[index_B,1]=j
                index_B+=1
            elif map[i,j]=="J":
                positions_J[index_J,0]=i
                positions_J[index_J,1]=j
                index_J+=1            
            elif map[i,j]=="Ep":
                positions_Ep[index_Ep,0]=i
                positions_Ep[index_Ep,1]=j
                index_Ep+=1
            elif map[i,j]=="P":
                positions_P[index_P,0]=i
                positions_P[index_P,1]=j
                index_P+=1
            elif map[i,j]=="Ec":
                if i+2<= map.shape[0]-1 and j+1 <= map.shape[1]-1:
                    if map[i+2, j+1]=="Ec":
                        map[i+1,j]="0"
                        map[i+2,j]="0"
                        map[i+1,j+1]="0"
                        map[i+2,j+1]="0"
                        map[i,j+1]="0"
                        positions_Ec[index_Ec,0]=i
                        positions_Ec[index_Ec,1]=j
                        index_Ec+=1
                else: 
                    print("ERREUR ORIENTATION ECOLE INTROUVEE")
            elif map[i,j] == "C":
                if i+1<=map.shape[0]-1:
                    if map[i+1,j]=="C":
                        map[i+1,j]="0"
                        positions_C1[index_C1,0]=i
                        positions_C1[index_C1,1]=j
                        index_C1+=1
                    else:
                        map[i,j+1]="0"
                        positions_C2[index_C2,0]=i
                        positions_C2[index_C2,1]=j
                        index_C2+=1

            elif map[i,j] == "R":
                if i+1<=map.shape[0]-1:
                    if map[i+1,j]=="R":
                        map[i+1,j]="0"
                        positions_R1[index_R1,0]=i
                        positions_R1[index_R1,1]=j
                        index_R1+=1
                    else:
                        map[i,j+1]="0"
                        positions_R2[index_R2,0]=i
                        positions_R2[index_R2,1]=j
                        index_R2+=1



                

    copy_and_modify_gltf(input_gltf_path, output_gltf_path, liste_noms, modify_function, x_size, y_size, liste_postitions, grid_to_nodes)

