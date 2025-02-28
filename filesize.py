import os
import pandas as pd

# Function to get file sizes
def get_file_sizes(directory):
    file_data = []
    
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if it's a file
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)  # Get file size in bytes
            file_data.append({'Filename': filename, 'Filesize': file_size})
    
    # Create a DataFrame
    df = pd.DataFrame(file_data)
    
    return df

# Example usage: Change 'your_directory_path' to an actual directory path
directory_path = "/workspaces/tmt/PointCloudStreaming-main/PointCloudServer/media/ply_input"  # Replace with the actual path
df_files = get_file_sizes(directory_path)

# Display the DataFrame
df_files.to_csv('ply_size.csv', index=0)
df_files.to_excel('ply_sizexlsx.xlsx', index=0)
