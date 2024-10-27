import sys

# get the filename
filename = sys.argv[1]

# read the contents of the file
contents = open(filename).read()

# print them in uppercase
print(contents.upper())
