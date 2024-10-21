import sys
## Get the filename 
filename = sys.argv[1]
## read the lines
lines = open(filename).readlines()

## Take first five lines 
first_five = lines[:5]
## print each line and end with the first five lines
for line in first_five:
   print(line.strip("\n"))
   
   
