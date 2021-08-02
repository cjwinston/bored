import requests
import json
import pandas as pd
import html
import random


def getData(number, category, difficulty, types):
    url = 'https://opentdb.com/api.php?amount=' + number + '&category=' + \
        category + '&difficulty=' + difficulty + '&type=' + types
    response = requests.get(url)
    r = response.json()
    return r


def createTrivia(r):
    questionsDict = {}
    questionNum = 1
    for questions in r['results']:
        if questions['type'] == 'boolean':
            questionsDict[questionNum] = {
                'question': html.unescape(
                    questions['question']),
                'type': questions['type'],
                'correct answer': questions['correct_answer'],
                'options': [
                    'True',
                    'False']}
        else:
            options = questions['incorrect_answers']
            options.append(questions['correct_answer'])
            random.shuffle(options)
            for index in range(len(options)):
                options[index] = html.unescape(options[index])
            questionsDict[questionNum] = {
                'question': html.unescape(
                    questions['question']),
                'type': questions['type'],
                'correct answer': html.unescape(
                    questions['correct_answer']),
                'options': options}
        questionNum += 1
    return questionsDict


r = getData('5', '26', '0', 'multiple')
print(r)
dict = createTrivia(r)
print(dict)

