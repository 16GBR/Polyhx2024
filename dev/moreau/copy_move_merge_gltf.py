import numpy as np
import pygltflib

def copy_and_modify_gltf(input_path, output_path, modification_function, x_size, y_size, positions_1, positions_2, grid_to_nodes):
    # Load the glTF file
    gltf = pygltflib.GLTF2().load(input_path)
    # gltf2 = pygltflib.GLTF2().load("../../3D_Models/Test_T.glb")
    

    # Premier object index
    object_index = 0

    # Translation du premier element et storage de la valeur de reference
    pygltflib.Node().from_dict(gltf.nodes[object_index].to_dict()).translation=[int(grid_to_nodes*positions_1[0,0]),int(grid_to_nodes*positions_1[0,1]),0]
    ref_position_x=positions_1[0,0]
    ref_position_y=positions_1[0,1]

    # Modification de la liste pour positions subséquentes
    positions_1=np.delete(positions_1,0,0)

    if len(positions_1)>0:
        # Loop itératif pour chacun des objets à dupliquer et placer
        copied_node= [None] * (len(positions_1))

        for i in range(len(positions_1)):
            print("i=",i)
            # Create a deep copy of the node
            copied_node[i] = pygltflib.Node().from_dict(gltf.nodes[object_index].to_dict())

            # Apply modifications to the copied node using the provided function
            modification_function(copied_node[i], positions_1, x_size, y_size, i, grid_to_nodes,ref_position_x,ref_position_y)

        for i in range(len(positions_1)):
            # Add the copied node to the list of nodes
            gltf.nodes.append(copied_node[i])

            # Update the scene to reference the new node
            gltf.scenes[0].nodes.append(len(gltf.nodes) - 1)

    # =========== 2e objet ============
    
    # Firsrt object index
    object_index = 1

    # Translation du premier element et storage de la valeur de reference
    pygltflib.Node().from_dict(gltf.nodes[object_index].to_dict()).translation=[int(grid_to_nodes*positions_2[0,0]),int(grid_to_nodes*positions_2[0,1]),0]
    ref_position_x=positions_2[0,0]
    ref_position_y=positions_2[0,1]

    # Modification de la liste pour positions subséquentes
    positions_2=np.delete(positions_2,0,0)

    if len(positions_2)>0:
        # Loop itératif pour chacun des objets à dupliquer et placer
        copied_node= [None] * (len(positions_1))

        for i in range(len(positions_2)):
            print("i=",i)
            # Create a deep copy of the node
            copied_node[i] = pygltflib.Node().from_dict(gltf.nodes[object_index].to_dict())

            # Apply modifications to the copied node using the provided function
            modification_function(copied_node[i], positions_2, x_size, y_size, i, grid_to_nodes,ref_position_x,ref_position_y)

        for i in range(len(positions_2)):
            # Add the copied node to the list of nodes
            gltf.nodes.append(copied_node[i])

            # Update the scene to reference the new node
            gltf.scenes[0].nodes.append(len(gltf.nodes) - 1)

    
    

    # print_var_test = pygltflib.Node().from_dict(gltf2.nodes[object_index].to_dict())
    # print(print_var_test)

    # modification_function(print_var_test,np.array([[5,5]]), 8,8,0,2,0,0)

    # gltf.nodes.append(print_var_test)
    # gltf.scenes[0].nodes.append(3)
    # print(gltf.scenes[0].nodes)

    # Save the modified glTF to a new file
    gltf.save(output_path)

def modify_function(node,positions,x_size,y_size,i,grid_to_nodes,ref_position_x,ref_position_y):
    # Modify the copied node as needed
    # node.name = "Copied_Object"
    # Add any other modifications here
    print("Modification i = ",i)
    if positions[i,0] >= x_size or positions[i,1] >= y_size :
        print("ERREUR position hors limite")
    else : 
        node.translation = [int(grid_to_nodes*(positions[i,0]-ref_position_x)),int(grid_to_nodes*(positions[i,1]-ref_position_y)),0]
        #node.scale=[2,2,1]

# def merge_gltf(input_list,output_path):

#     gltf_list=[None]*len(input_list)
#     # Load the glTF file
#     for i in range(len(input_list)):
#         gltf_list[i] = pygltflib.GLTF2().load(input_list[i])
    

#     gltf.save(output_path)

# def merge_gltf_files(input_paths, output_path):
#     # Create a new glTF file
#     merged_gltf = pygltflib.GLTF2()

#     # Load each input glTF file and append its elements to the merged glTF
#     for input_path in input_paths:
#         input_gltf = pygltflib.GLTF2().load(input_path)

#         # Append scenes
#         merged_gltf.scenes.extend(input_gltf.scenes)

#         # Append nodes
#         merged_gltf.nodes.extend(input_gltf.nodes)

#         # Append meshes
#         merged_gltf.meshes.extend(input_gltf.meshes)

#         # Append materials
#         merged_gltf.materials.extend(input_gltf.materials)

#         # Append images
#         merged_gltf.images.extend(input_gltf.images)

#         # Append textures
#         merged_gltf.textures.extend(input_gltf.textures)

#         # Append samplers
#         merged_gltf.samplers.extend(input_gltf.samplers)

#         # Append animations
#         merged_gltf.animations.extend(input_gltf.animations)

#         # Append cameras
#         merged_gltf.cameras.extend(input_gltf.cameras)

#     # Save the merged glTF to the output file
#     # merged_gltf.save(output_path)
#     print("Merged Scenes:", merged_gltf.scenes)
#     print("Merged Nodes:", merged_gltf.nodes)

#     try:
#         merged_gltf.save(output_path)
#     except Exception as e:
#         print(f"Error saving the merged glTF: {e}")

# import json
# import chardet
# import struct
# import base64


# def merge_gltf_binary_files(input_paths, output_path):
# # Load and merge each input GLB file
# gltf_list = []
# for input_path in input_paths:
# try:
#     gltf = pygltflib.GLTF2().load(input_path)
#     gltf_list.append(gltf)
# except Exception as e:
#     print(f"Error processing file '{input_path}': {e}")

# # Create a new GLTF object with merged scenes
# merged_gltf = pygltflib.GLTF2()
# for gltf in gltf_list:
# merged_gltf.scenes.extend(gltf.scenes)

# # Save the merged GLTF to the output path
# merged_gltf.save(output_path)


# # Example usage
# input_files = ["../../3D_Models/Test.glb","../../3D_Models/Test_T.glb" ]
# output_file = "../../merged_file.gltf"
# merge_gltf_binary_files(input_files, output_file)
