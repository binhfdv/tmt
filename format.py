# import open3d as o3d
# import numpy as np

# # Load the failing binary PLY
# ply_path = "/workspaces/tmt/orobotstate/robot_20250223_131946.ply"
# pcd = o3d.io.read_point_cloud(ply_path)

# # Convert double (float64) to float32
# xyz = np.asarray(pcd.points, dtype=np.float32)
# colors = np.asarray(pcd.colors, dtype=np.float32)  # Normalize if necessary

# # Create new point cloud with float32 precision
# new_pcd = o3d.geometry.PointCloud()
# new_pcd.points = o3d.utility.Vector3dVector(xyz)
# new_pcd.colors = o3d.utility.Vector3dVector(colors / 255.0)  # Normalize colors

# # Save as a new binary PLY with `float`
# o3d.io.write_point_cloud("fixed_output_binary.ply", new_pcd, write_ascii=False)

# # Save as ASCII for debugging
# o3d.io.write_point_cloud("fixed_output_ascii.ply", new_pcd, write_ascii=True)

from plyfile import PlyData, PlyElement
import numpy as np

# Load the binary PLY file
ply_path = "/workspaces/tmt/orobotstate/robot_20250223_131946.ply"
ply_data = PlyData.read(ply_path)

# Extract vertex data
vertex_data = ply_data["vertex"]

# Convert double (float64) to float32
xyz = np.column_stack((vertex_data["x"], vertex_data["y"], vertex_data["z"])).astype(np.float64)

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
fixed_ply_path = "fixed_output_binary.ply"
new_ply.write(fixed_ply_path)

print(f"Fixed PLY saved as: {fixed_ply_path}")

