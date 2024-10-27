import requests
import sys

place_name = sys.argv[1]
url = "https://nominatim.openstreetmap.org/search"

params = {"q": place_name, "format": "json"}


data = requests.get(url,params=params).json()
print(data)
