import sys
import requests

lookup_word = sys.argv[1]

url = "https://api.dictionaryapi.dev/api/v2/entries/en/{lookup_word}"

data = requests.get(url)
print(data)
