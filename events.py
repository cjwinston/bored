import requests
import json

# for Discovery API
discovery_apikey = 'dJICZjQMWJ6ZyTe9gXaTuTqQGETOqQOT'
discovery_base_url = 'https://app.ticketmaster.com/discovery/v2/'

def getData(keyword, city):
    api_key= 'dJICZjQMWJ6ZyTe9gXaTuTqQGETOqQOT'
    base_url = 'https://app.ticketmaster.com/discovery/v2/events'
    url = base_url + '?apikey=' + api_key + '&keyword=' + keyword +'&locale=*&page=1&city=' + city
    response = requests.get(url)
    r = response.json()
    return r

def main():
    keyword = 'music'
    city = 'atlanta'
    d = getData(keyword, city)
    createDict(d)

def createDict(response):
    eventsDict = {}
    for embedded in response['_embedded']['events']:
        eventsDict[embedded['id']] = {'name': embedded['name'],
                                      'url': embedded['url'],
                                      'image': embedded['images'][0]['url'],
                                      'date': embedded['dates']['start']['localDate'],
                                      'priceMin': embedded['priceRanges'][0]['min'],
                                      'priceMax': embedded['priceRanges'][0]['max']}
#         print(embedded['priceRanges'][0]['min'])
    print(eventsDict)

if __name__ == '__main__':
        main()
    
#     ['events']
#     name, images, url, dates?? (start, local date & time), price