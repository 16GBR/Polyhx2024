import numpy as np
import pygltflib

def copy_and_modify_gltf(input_path, output_path, object_name, modification_function):
    # Load the glTF file
    gltf = pygltflib.GLTF2().load(input_path)

    # Find the index of the object to copy
    object_index = None
    for index, node in enumerate(gltf.nodes):
        if node.name == object_name:
            object_index = index
            break

    if object_index is None:
        print(f"Object with name '{object_name}' not found.")
        return

    # Create a deep copy of the node
    copied_node = pygltflib.Node().from_dict(gltf.nodes[object_index].to_dict())

    # Apply modifications to the copied node using the provided function
    modification_function(copied_node)

    # Add the copied node to the list of nodes
    gltf.nodes.append(copied_node)

    # Update the scene to reference the new node
    gltf.scenes[0].nodes.append(len(gltf.nodes) - 1)

    # Save the modified glTF to a new file
    gltf.save(output_path)

def modify_function(node):
    # Modify the copied node as needed
    node.name = "Copied_Object"
    # Add any other modifications here
    node.translation = [2,2,0]


# Example usage
input_gltf_path = "3D_Models/Test.glb"
output_gltf_path = "3D_Models/Test_modifie.glb"
object_to_copy = "Cube.002"

copy_and_modify_gltf(input_gltf_path, output_gltf_path, object_to_copy, modify_function)
