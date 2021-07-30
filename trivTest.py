import requests
import json


def getData(number, category, difficulty, types):
    url = 'https://opentdb.com/api.php?amount=' + number + \
        '&difficulty=' + difficulty + '&type=' + types
    response = requests.get(url)
    r = response.json()
    print(r)
