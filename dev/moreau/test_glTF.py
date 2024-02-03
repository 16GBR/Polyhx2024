import numpy as np 
#from pygltflib import GLTF2
import pygltflib

a=np.array([1,2])
print(a)

entree = "3D_Models/Test.glb"
#objet1 = GLTF2().load(filename1)

objet1 = pygltflib.GLTF2().load(entree)

#objet1['nodes'][0]['translation']=[1,2,0]

# Assume you want to translate the first node in the scene
node_index_to_translate = 0

# Specify the translation vector (e.g., translate by (1, 2, 3) units)
translation_vector = [100.0, 200.0, 300.0]

# Update the translation of the specified node
objet1.nodes[node_index_to_translate].translation = translation_vector
objet1.nodes[0].scale=[1,5,2]
objet1.nodes[0].scale=[1,5,5]
objet2=objet1
objet2.nodes[0].translation=[-100,-200,-300]
objet2.nodes[0].scale=[1,0.2,0.5]

#scene_tot=pygltflib.Scene()
#scene_tot.nodes.extend(objet1.scenes[0].nodes)
#scene_tot.nodes.extend(objet2.scenes[0].nodes)
#objet_tot=pygltflib.GLTF2(scenes=[scene_tot])

# def merge_gltf(gltf1, gltf2):
#     # Create a new GLTF object
#     merged_gltf = pygltflib.GLTF2()

#     # Merge scenes
#     merged_gltf.scenes.extend(gltf1.scenes)
#     merged_gltf.scenes.extend(gltf2.scenes)

#     # Merge nodes
#     merged_gltf.nodes.extend(gltf1.nodes)
#     merged_gltf.nodes.extend(gltf2.nodes)

#     # Update the node's scene index based on the scene index it belongs to
#     for node in merged_gltf.nodes:
#         if hasattr(node, 'scene') and node.scene is not None:
#             node.scene += len(gltf1.scenes)

#     # Merge buffers and buffer views
#     if gltf1.buffers and gltf1.bufferViews:
#         merged_gltf.buffers.extend(gltf1.buffers)
#         merged_gltf.bufferViews.extend(gltf1.bufferViews)

#     if gltf2.buffers and gltf2.bufferViews:
#         merged_gltf.buffers.extend(gltf2.buffers)
#         merged_gltf.bufferViews.extend(gltf2.bufferViews)

#     # Merge accessors
#     if gltf1.accessors:
#         merged_gltf.accessors.extend(gltf1.accessors)
#     if gltf2.accessors:
#         merged_gltf.accessors.extend(gltf2.accessors)

#     return merged_gltf




#fusion = merge_gltf(objet1, objet2)

sortie1 = "3D_Models/test_1.glb"
objet1.save(sortie1)

sortie2 = "3D_Models/test_2.glb"
objet2.save(sortie2)





