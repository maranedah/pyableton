import gzip

file_path = ".\\test\\test.als"
with gzip.open(file_path, "rb") as gzipped_file:
    # Read the contents of the file
    file_contents = gzipped_file.read()

file_path = "test.xml"
with open(file_path, "wb") as output_file:
    output_file.write(file_contents)
