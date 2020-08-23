import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = address
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read()

    tree = ET.fromstring(data)
    comments = tree.findall('comments/comment')
    sum = 0
    for c in comments:
        print(c.find('name').text)
        print(c.find('count').text)
        sum += int(c.find('count').text)
    break
print("SUM = ",sum)




