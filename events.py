import requests
import json

# for Discovery API
discovery_apikey = 'dJICZjQMWJ6ZyTe9gXaTuTqQGETOqQOT'
discovery_base_url = 'https://app.ticketmaster.com/discovery/v2/'


def getEventData(keyword, city):
    api_key = 'dJICZjQMWJ6ZyTe9gXaTuTqQGETOqQOT'
    base_url = 'https://app.ticketmaster.com/discovery/v2/events'
    url = base_url + '?apikey=' + api_key + '&keyword=' + \
        keyword + '&locale=*&sort=date,asc&page=1&city=' + city
    response = requests.get(url)
    r = response.json()
    return r


def createDict(response):
    eventsDict = {}
    key = 'localDate'
    for embedded in response['_embedded']['events']:
        eventsDict[embedded['id']] = {'name': embedded['name'],
                                      'url': embedded['url'],
                                      'image': embedded['images'][0]['url'],
                                      'date': embedded['dates']['start'][key]}
    return eventsDict
