import random
import urllib.request

def imagedownloader(url):
    number = random.randrange(1, 500)
    name = str(number) + ".jpg"
    urllib.request.urlretrieve(url, name)

imageurl = input("Enter the url :")
imageurl,_ = imageurl.split(" ")

imagedownloader(str(imageurl))
