from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import requests

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

names = []

url = input('Enter - ')
count = input('Enter count: ')
position = input('Enter position: ')

print("Retrieving:", url)

counter = 0

while (counter < int(count)):
    counter+=1
    html = urlopen(url, context = ctx)
    soup = BeautifulSoup(html, "html.parser")
    a = soup.find_all('a')[int(position) - 1]["href"]
    print("Retrieving:",a)
    url = a