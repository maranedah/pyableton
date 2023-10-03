import dawtool

filename = "evasiva.als"


import gzip
file_path = "evasiva.als"
with gzip.open(file_path, 'rb') as gzipped_file:
    # Read the contents of the file
    file_contents = gzipped_file.read()
    
file_path = "evasiva.xml"
with open(file_path, 'wb') as output_file:
    output_file.write(file_contents)
breakpoint()


with open(filename, 'rb') as f:
    # Load project based on file extension
    proj = dawtool.load_project(filename, f)
    # Parse project, recompute time markers
    proj.parse()
    breakpoint()
    # Access project data
    for marker in proj.markers:
        print(marker.time, marker.text)