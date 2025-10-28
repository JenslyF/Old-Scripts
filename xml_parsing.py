import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

nums = []

url = input('Enter URL - ')

xml = urllib.request.urlopen(url, context = ctx).read()

tree = ET.fromstring(xml)

parsing = tree.findall('comments/comment')

for item in parsing:
    nums.append(int(item.find('count').text))

print(sum(nums))