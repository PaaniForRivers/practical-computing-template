import sys

# get the two filenames

file1 = sys.argv[1]
file2 = sys.argv[2]

# create the concatenated filename 
concat_filename = f"{file1.split('.')[0]}{file2.split('.')[0]}.txt"

# read the contents with with to ensure the files are closed properly
with open(file1, 'r') as f1:
    file1_contents = f1.read()

with open(file2, 'r') as f2:
    file2_contents = f2.read()


with open((concat_filename),"w")as f:
       f.write(file1_contents)
       f.write(file2_contents)

print("files concatenated")








