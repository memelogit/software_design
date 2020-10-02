import requests
import urllib3
urllib3.disable_warnings()

endpoint = 'http://api.plos.org/search?q=title:DNA'

response = requests.get(endpoint, verify=False)
content = response.json()
docs = content['response']['docs']

for doc in docs:
    if 'Anna Ivanova' in doc['author_display']:
        print(doc['id'])
    
    for key, value in doc.items():
        print(key, value)