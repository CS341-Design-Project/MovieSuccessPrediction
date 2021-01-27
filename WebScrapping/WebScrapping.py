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