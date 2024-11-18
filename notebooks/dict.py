import sys
import requests


lookup_word = sys.argv[1]

url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{lookup_word}"
print(url)

data = requests.get(url).json()
data
