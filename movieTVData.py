import requests
import json

def getData(filmType):
        url = 'https://opentdb.com/api.php?amount='+number+'&difficulty='+difficulty+'&type='+types
        response = requests.get(url)
        r = response.json()
        print(r)
