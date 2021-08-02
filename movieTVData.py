import requests
import json


def getFilmData(apikey, filmType, trendType):
    #         if filmType == 'show':
    #             filmType = 'tv'
    base_url = 'https://api.themoviedb.org/3/trending/'
    url = base_url + filmType + '/' + trendType + '?api_key=' + apikey
    response = requests.get(url)
    r = response.json()
    return r


def parseData(r):
    url = 'https://image.tmdb.org/t/p/w500/'
    d = r['results']
    dict = {}
    index = 0
    for movie in d:
        if movie['media_type'] == 'movie':
            dict[index + 1] = {'name': movie['original_title'],
                               'overview': movie['overview'],
                               'image_url': url + movie['poster_path']
                               }
        else:
            dict[index + 1] = {'name': movie['original_name'],
                               'overview': movie['overview'],
                               'image_url': url + movie['poster_path']
                               }
        index += 1
    return dict


# def main():
#     api_key = '25cd471bedf2ee053df9b1705494367d'
#     filmType = 'show'
#     trendType = 'week'
#     d = getFilmData(api_key, filmType, trendType)
#     dict = parseData(d)
#     print(dict)


# if __name__ == '__main__':
#     main()
