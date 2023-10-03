import gzip

file_path = "evasiva.als"
with gzip.open(file_path, "rb") as gzipped_file:
    # Read the contents of the file
    file_contents = gzipped_file.read()

file_path = "evasiva.xml"
with open(file_path, "wb") as output_file:
    output_file.write(file_contents)
