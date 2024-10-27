import sys
# get the file name
file = sys.argv[1]
with open(file, 'r') as f1:
    file_contents = f1.readlines()
    for line in reversed(file_contents):
      print(line)
