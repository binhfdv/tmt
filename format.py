import os
from plyfile import PlyData, PlyElement
import numpy as np

def process_ply_file(input_path, output_path): 
    # Load the binary PLY file
    ply_data = PlyData.read(input_path)
    
    # Extract vertex data
    vertex_data = ply_data["vertex"]
    
    # Convert double (float64) to float32
    xyz = np.column_stack((vertex_data["x"], vertex_data["y"], vertex_data["z"])).astype(np.float32)
    
    # Keep colors as uchar (0-255)
    colors = np.column_stack((vertex_data["red"], vertex_data["green"], vertex_data["blue"])).astype(np.uint8)
    
    # Create new PLY element
    vertex_array = np.empty(len(xyz), dtype=[("x", "f4"), ("y", "f4"), ("z", "f4"),
                                             ("red", "u1"), ("green", "u1"), ("blue", "u1")])
    vertex_array["x"], vertex_array["y"], vertex_array["z"] = xyz[:, 0], xyz[:, 1], xyz[:, 2]
    vertex_array["red"], vertex_array["green"], vertex_array["blue"] = colors[:, 0], colors[:, 1], colors[:, 2]
    
    # Create new PLY file
    vertex_element = PlyElement.describe(vertex_array, "vertex")
    new_ply = PlyData([vertex_element], text=False)
    
    # Save the fixed binary PLY file
    new_ply.write(output_path)
    print(f"Fixed PLY saved as: {output_path}")

def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".ply"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            process_ply_file(input_path, output_path)

# Set folder paths
input_folder = "/workspaces/tmt/occupancymap"
output_folder = "/workspaces/tmt/float_occupancymap"

# Process all PLY files in folder1 and save to folder2
process_folder(input_folder, output_folder)
