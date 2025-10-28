from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

nums = []

url = input('Enter - ')
html = urlopen(url, context = ctx)
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')

for tag in tags:
    nums.append(int(tag.contents[0]))

print(sum(nums))
