import pandas as pd
import matplotlib.pyplot as plt
import re

# Define a function to parse the log file
def parse_log_to_dataframe(file_path):
    # Create an empty list to store the parsed data
    data = []

    # Open and read the log file
    with open(file_path, 'r') as file:
        for line in file:
            print(f"Processing line: {line.strip()}")  # Debug: Show each line processed
            # Adjusted regular expression to match the timestamp with microseconds
            match = re.match(r"Start Time: (\S+ \S+) - End Time: (\S+ \S+) - File: (\S+) --- Compression time: (\d+) milliseconds", line)
            if match:
                # Extract matched data into variables
                start_time = match.group(1)
                end_time = match.group(2)
                file_name = match.group(3)
                compression_time = int(match.group(4))

                # Append the data to the list
                data.append([start_time, end_time, file_name, compression_time])
            else:
                print("No match for line.")  # Debug: Print when no match is found

    # Convert the list into a pandas DataFrame
    df = pd.DataFrame(data, columns=["Start Time", "End Time", "File", "Compression Time (ms)"])
    return df

# Use the function to parse your log file
log_file_path = '/workspaces/tmt/compression.log'  # Update with the actual path to your .log file
df = parse_log_to_dataframe(log_file_path)

df.to_csv('./compression.csv', index=0)
df.to_excel('./compression_xlsx.xlsx', index=False)
# Print the DataFrame to check the result
# print(df.head())


plt.figure(figsize=(10, 6))
plt.plot(df.index + 1, df['Compression Time (ms)'], marker='o', linestyle='-', color='b')

# Labeling the axes and title
plt.xlabel('Index')
plt.ylabel('Compression Time (ms)')
plt.title('Compression Time vs Index')

# Show the plot
plt.grid(True)
plt.show()