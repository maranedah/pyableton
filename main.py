import gzip


def compress_file(input_file, output_file):
    with open(input_file, "rb") as f_in, gzip.open(output_file, "wb") as f_out:
        f_out.writelines(f_in)


input_filename = ".\\test\\evasiva.xml"
output_filename = ".\\test\\test.als"

compress_file(input_filename, output_filename)
