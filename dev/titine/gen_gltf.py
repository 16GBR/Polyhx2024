import numpy as np
import pygltflib
from copy_move_merge_gltf import copy_and_modify_gltf, modify_function

def gen_gltf(map):
    #map : np.array(strings)

    x_size = 500
    y_size = 500
    positions_1 = np.array([[0,7],[0,10],[0,13]])
    positions_2 = np.array([[2,1],[2,2],[2,3],[2,4],[2,5],[2,6]])
    grid_to_nodes = 1

    input_gltf_path = "../../3D_Models/Models.gltf"
    output_gltf_path = "../../3D_Models/Map.gltf"
    rotations_1 = np.array([])
    rotations_2 = np.array([])

    liste_noms=["School_2x3","GStore_1x1"]
    liste_postitions=[positions_1,positions_2]
    liste_rotations=[rotations_1,rotations_2]



    copy_and_modify_gltf(input_gltf_path, output_gltf_path, liste_noms, liste_rotations, modify_function, x_size, y_size, liste_postitions, grid_to_nodes)

