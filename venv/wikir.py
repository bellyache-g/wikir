import random
import time
import requests
from bs4 import BeautifulSoup

# empty list to hold pairs of titles and URL of the random wiki page
wikisHere = []

# variable to store zero so we can track what iteration we're on in the loop below
startNumber = 0

# loop to get 10 random wiki pages and their URLs and store them in wikisHere
for x in range(10):
    # storage for the random URL link copied from wikipedia
    randomurl = 'https://en.wikipedia.org/wiki/Special:Random'

    # GET request to download the html file of the link stored in randomurl
    url = requests.get(randomurl)

    # variable to apply encoding to html page downloaded in previous step
    r = url.content

    # variable to get actual URL of the page that was randomly selected using the random site
    # wiki link
    linktourl = url.url

    # variable to create datastructure that we can use bs4 to parse and retrieve data from
    soup = BeautifulSoup(r, 'html.parser')

    # variable to store the title of each page
    title = (soup.find("h1"))

    # links = soup.find("href")
    wikisHere.append({title.text:linktourl})
    startNumber += 1
    print(str(startNumber) + ' added ' + str(title.text) + ' ' + str(linktourl))

print('list built, picking random page')

for z in range(1):
    randomWiki = random.choice(wikisHere)

print(randomWiki)

