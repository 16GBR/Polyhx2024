import numpy as np 
from pygltflib import GLTF2

a=np.array([1,2])
print(a)

filename1 = "3D Models/Test.glb"
objet1 = GLTF2().load(filename1)

#objet1['nodes'][][]=[1,2,0]

