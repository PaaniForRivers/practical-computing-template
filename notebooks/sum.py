import sys
# intialize sum as '0'
sum = 0
# there are variable number of arguments, so use the [1:]
for arg in sys.argv[1:]:
    num = int(arg)
    sum = sum + int(num)
print(sum)
