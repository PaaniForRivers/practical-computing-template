import sys
from PIL import Image 
filename = sys.argv[1]
thumb_filename = filename.replace(".jpg","-thumbnail.jpg")
image = Image.open(filename)
image.thumbnail((100,100))
image.save(thumb_filename)
print("created thumbnail", thumb_filename)
