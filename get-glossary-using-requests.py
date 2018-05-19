
import json

from bs4 import BeautifulSoup
import requests

url = 'https://docs.python.org/3/glossary.html'

response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'lxml')

dts = soup.find_all('dt')
dds = soup.find_all('dd')

results = []
for term, gloss in list(zip(dts, dds)):

    results.append( {'term'  : term.get_text(),
                     'gloss' : gloss.get_text() } )

with open('python-glossary-requests.json', 'w') as glossaryfile:
    json.dump(results, glossaryfile, indent=4, ensure_ascii = False)

