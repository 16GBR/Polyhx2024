import numpy as np
import pygltflib

def copy_and_modify_gltf(input_path, output_path, liste_noms, modification_function, x_size, y_size, liste_postitions, grid_to_nodes):
    # Load the glTF file
    gltf = pygltflib.GLTF2().load(input_path)

    for i in range(len(liste_noms)):
        nom=liste_noms[i]
        positions=liste_postitions[i]
        
        for idx, node in enumerate(gltf.nodes):
            if node.name == nom:
                object_index = idx
                break


        # Translation du premier element et storage de la valeur de reference
        pygltflib.Node().from_dict(gltf.nodes[object_index].to_dict()).translation=[int(grid_to_nodes*positions[0,0]),0,int(grid_to_nodes*positions[0,1])]
        ref_position_x=positions[0,0]
        ref_position_y=positions[0,1]

        # Modification de la liste pour positions subséquentes
        positions=np.delete(positions,0,0)

        if len(positions)>0:
            # Loop itératif pour chacun des objets à dupliquer et placer
            copied_node= [None] * (len(positions))

            for i in range(len(positions)):
                print("i=",i)
                # Create a deep copy of the node
                copied_node[i] = pygltflib.Node().from_dict(gltf.nodes[object_index].to_dict())

                # Apply modifications to the copied node using the provided function
                modification_function(copied_node[i], positions, x_size, y_size, i, grid_to_nodes,ref_position_x,ref_position_y)

            for i in range(len(positions)):
                # Add the copied node to the list of nodes
                gltf.nodes.append(copied_node[i])

                # Update the scene to reference the new node
                gltf.scenes[0].nodes.append(len(gltf.nodes) - 1)

    
    gltf.save(output_path)

def modify_function(node,positions,x_size,y_size,i,grid_to_nodes,ref_position_x,ref_position_y):
    # Modify the copied node as needed
    # node.name = "Copied_Object"
    # Add any other modifications here
    print("Modification i = ",i)
    if positions[i,0] >= x_size or positions[i,1] >= y_size :
        print("ERREUR position hors limite")
    else : 
        node.translation = [int(grid_to_nodes*(positions[i,0]-ref_position_y)),0,int(grid_to_nodes*(positions[i,1]-ref_position_x))]
        #node.scale=[2,2,1]
