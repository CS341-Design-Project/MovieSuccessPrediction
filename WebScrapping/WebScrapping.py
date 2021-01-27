import urllib.request, urllib.parse, urllib.error
import re
import ssl
import requests
from bs4 import BeautifulSoup
import time
import itertools
from tqdm import tqdm

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def rating_google(title) :
  try :
    url = "https://www.google.com/search?q="+title
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    google = soup.find_all('div', attrs={'class':'srBp4 Vrkhme'})
    imdb = soup.find_all('span', attrs={'class':'gsrt IZACzd'})

    if len(google) :
      rating = google[0].contents[0][0:2]

    elif len(imdb):
        if (imdb[0].contents[0][1] != '/'):
          rating = float(imdb[0].contents[0][0:3])*10
        else :
          rating = float(imdb[0].contents[0][0])*10
    
    else :
      rating = 0
    
    time.sleep(2)

    return int(rating)

  except :
    print("Couldn't fetch rating for " + title)
    rating = 0
    return int(rating)
