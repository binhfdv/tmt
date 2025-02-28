#!/bin/bash

# Directories
folder1="/workspaces/tmt/occupancymap"
folder2="/workspaces/tmt/PointCloudStreaming-main/PointCloudServer/media/ply_input"

# Delay in milliseconds (19ms)
sleep_duration=0.019

# Counter for filenames
counter=1

# Start time (current time in seconds)
start_time=$(date +%s)

# Infinite loop that runs until 1 second has passed
while true; do
  # Get the current time in seconds
  current_time=$(date +%s)
  
  # Check if 1 second has passed
  if ((current_time - start_time >= 2)); then
    break
  fi

  # Loop through files in folder1
  for file in "$folder1"/*.ply; do
    # Wait for the specified time
    sleep $sleep_duration
    
    # Generate new filename with index
    new_filename="$folder2/$(basename "$file" .ply)_$counter.ply"
    
    # Copy file to folder2 with new name
    cp "$file" "$new_filename"
    
    # Increment counter
    ((counter++))
  done
done