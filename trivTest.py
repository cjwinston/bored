import requests
import json

def getData(number, category, difficulty, types):
        if number =="0":
            number = ""
        if  category=="0":
            category=""
        url = 'https://opentdb.com/api.php?amount='+number+'&category='+category+'&difficulty='+difficulty+'&type='+types
        response = requests.get(url)
        r = response.json()
        print(r)
        
        # Store Infor in database
        # Hopefully it stores in a dataframe
