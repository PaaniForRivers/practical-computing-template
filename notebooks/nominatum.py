import requests
import sys

place_name = sys.argv[1]
url = "https://nominatim.openstreetmap.org/search.php"

params = {"q": place_name, "format": "jsonv2"}


data = requests.get(url,params=params).text
print(data)
