import requests
from bs4 import BeautifulSoup
import json
import sys

if len(sys.argv) < 3:
    print('Usage: python imgur-soup.py album_url output_file_path')
    sys.exit(1)

album = sys.argv[1]
file = sys.argv[2]

res = requests.get(album)
soup = BeautifulSoup(res.text, 'html.parser')

# output is in test.html
# we need to get the json from the <script>window.postDataJSON objct
postDataJSON = (soup.find('script', text=lambda t: t.startswith('window.postDataJSON')).text).split('=')[1]
postDataJSON = json.loads(postDataJSON)
stuff = json.loads(postDataJSON)

urls = []
for image in stuff['media']:
    link = image['url']
    urls.append(link)
    print(link)

with open(file, 'w') as f:
    f.write('\n'.join(urls))