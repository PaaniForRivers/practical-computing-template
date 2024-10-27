import random
quotes = open("fortune.txt").read().split('%')
print(random.choice(quotes))
