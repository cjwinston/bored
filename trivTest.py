import requests
import json

url = 'https://opentdb.com/api.php?amount=10&difficulty=easy&type=multiple'
response = requests.get(url)
r = response.json()
print(r)