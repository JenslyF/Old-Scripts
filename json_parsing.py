from urllib.request import urlopen
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

nums = []

url = input('Enter URL:')

data = urlopen(url, context=ctx).read()

info = json.loads(data)

for item in info['comments']:
    nums.append(item.get('count'))
print(sum(nums))