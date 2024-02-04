import json

def merge_gltf_files(input_names, output_name):
    # Initialize an empty glTF object
    merged_gltf = {
        "asset": {
            "version": "2.0",
            "generator": "Your Merge Script"
        },
        "scenes": [],
        "nodes": [],
        "meshes": [],
        "materials": [],
        "buffers": [],
        "bufferViews": [],
        "accessors": []
    }

    buffer_offset = 0  # Keep track of the offset for each buffer

    # Loop through each input glTF file
    for input_name in input_names:
        with open(input_name, 'r', encoding='utf-8-sig') as file:  # or encoding='latin-1'
            gltf_data = json.load(file)

            # Merge scenes, nodes, meshes, materials, buffers, etc.
            merged_gltf["scenes"].extend(gltf_data.get("scenes", []))
            merged_gltf["nodes"].extend(gltf_data.get("nodes", []))
            merged_gltf["meshes"].extend(gltf_data.get("meshes", []))
            merged_gltf["materials"].extend(gltf_data.get("materials", []))

            # Merge buffers and update buffer views
            for buffer in gltf_data.get("buffers", []):
                buffer["uri"] = f"{input_name}#/{buffer['uri']}"  # Add input file path to buffer URI
                merged_gltf["buffers"].append(buffer)

            for bufferView in gltf_data.get("bufferViews", []):
                bufferView["buffer"] += buffer_offset
                merged_gltf["bufferViews"].append(bufferView)

            # Update accessors to point to the correct buffer view
            for accessor in gltf_data.get("accessors", []):
                accessor["bufferView"] += buffer_offset
                merged_gltf["accessors"].append(accessor)

            # Update buffer offset for the next file
            buffer_offset += len(gltf_data.get("buffers", []))

    # Write the merged glTF to the output file
    with open(output_name, 'w') as output_file:
        json.dump(merged_gltf, output_file, indent=2)

# Example usage
input_files = ["../../3D_Models/Test.glb", "../../3D_Models/Test_serie.glb", "../../3D_Models/Test_T.glb"]
output_file = "../../merged_file.gltf"
merge_gltf_files(input_files, output_file)