import numpy as np
import pygltflib
from copy_move_merge_gltf import copy_and_modify_gltf, modify_function

x_size = 50
y_size = 50
positions_1 = np.array([[0,0],[0,0],[0,3],[0,6]])
positions_2 = np.array([[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6]])
grid_to_nodes = 1

input_gltf_path = "../../3D_Models/Models.gltf"
output_gltf_path = "../../3D_Models/Map.gltf"

liste_noms=["School_2x3"]
liste_postitions=[positions_1]


copy_and_modify_gltf(input_gltf_path, output_gltf_path, liste_noms, modify_function, x_size, y_size, liste_postitions, grid_to_nodes)

