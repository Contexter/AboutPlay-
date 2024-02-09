import os

directory = '/Users/tadi/tada/the-four-stars'  # Replace with the path to your directory
output_file = 'merged.txt'       # Name of the output file

with open(output_file, 'w') as outfile:
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'r') as infile:
                outfile.write(infile.read())
                # Remove the line below to avoid adding an extra newline
                # outfile.write('\n')
