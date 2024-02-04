import numpy as np
import pygltflib
from copy_move_merge_gltf import copy_and_modify_gltf, modify_function

x_size = 50
y_size = 50
positions_1 = np.array([[0,1],[1,0],[1,1]])
positions_2 = np.array([[3,3],[4,5]])
#positions = np.array([[3,2]])
grid_to_nodes = 2

input_gltf_path = "../../3D_Models/CombinedYEEEE.gltf"
output_gltf_path = "../../3D_Models/MergedFTW.gltf"

copy_and_modify_gltf(input_gltf_path, output_gltf_path, modify_function, x_size, y_size, positions_1, positions_2, grid_to_nodes)
