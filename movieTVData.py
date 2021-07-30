import requests
import json

def getFilmData(apikey, filmType, trendType):
        if filmType == 'Show':
            filmType = 'tv'
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
        while index < len(d):
            if d[0]['media_type'] == 'movie':
                dict[index] = {'name': d[index]['original_title'],
                              'overview': d[index]['overview'],
                              'image_url': url + d[index]['poster_path']
                             }
            else:
                dict[index] = {'name': d[index]['original_name'],
                              'overview': d[index]['overview'],
                              'image_url': url + d[index]['poster_path']
                             }
            index += 1
        return dict
            
     

def main():
    api_key = '25cd471bedf2ee053df9b1705494367d'
    filmType = 'Show'
    trendType = 'week'
    d = getFilmData(api_key, filmType, trendType)
    dict = parseData(d)
    print(dict)


if __name__ == '__main__':
    main()


# parsed data ex
{0: 
 {'name': 'F9', 
  'overview': "Dominic Toretto and his crew battle the most skilled assassin and high-performance driver they've ever encountered: his forsaken brother.", 
  'posterpath': '/bOFaAXmWWXC3Rbv4u4uM9ZSzRXP.jpg'
 }, 
 1: 
 {'name': 
  'Jungle Cruise', 
  'overview': 'Dr. Lily Houghton enlists the aid of wisecracking skipper Frank Wolff to take her down the Amazon in his dilapidated boat. Together, they search for an ancient tree that holds the power to heal.', 
  'posterpath': '/jFo94MnRCfkjFgvvT1vVbyudKGK.jpg'
 }, 
 2: 
 {'name': 'Le Dernier Mercenaire', 
  'overview': 'A mysterious former secret service agent must urgently return to France when his estranged son  is falsely accused of arms and drug trafficking by the government, following a blunder by an overzealous bureaucrat and a mafia operation.', 
  'posterpath': '/nlCQAkIj2pfUEjCbPw61EMNX5Sb.jpg'
 }, 
 3: 
 {'name': 'Black Widow', 
  'overview': 'Natasha Romanoff, also known as Black Widow, confronts the darker parts of her ledger when a dangerous conspiracy with ties to her past arises. Pursued by a force that will stop at nothing to bring her down, Natasha must deal with her history as a spy and the broken relationships left in her wake long before she became an Avenger.', 
  'posterpath': '/qAZ0pzat24kLdO3o8ejmbLxyOac.jpg'
 }, 
 4: 
 {'name': 'Jolt', 
  'overview': 'Lindy is an acid-tongued woman with rage issues who controls her temper by shocking herself with an electrode vest. One day she makes a connection with Justin, who gives her a glimmer of hope for a shock-free future, but when he’s murdered she launches herself on a revenge-fueled rampage in pursuit of his killer.', 
  'posterpath': '/gYZAHan5CHPFXORpQMvOjCTug4E.jpg'
 }, 
 5: 
 {'name': 
  'Resort to Love', 
  'overview': 'Aspiring pop star Erica ends up as the entertainment at her ex-fiancé’s wedding after reluctantly taking a gig at a luxurious island resort while in the wake of a music career meltdown.', 
  'posterpath': '/6TrkFcgCF8Vznk45rs3qvxxejiV.jpg'
 }, 
 6: 
 {'name': 'るろうに剣心 最終章 The Beginning', 
  'overview': 'Kenshin Himura goes up against mysterious weapons dealer Enishi. He controls the underworld of China. The secret of Kenshin Himura’s "Jujishou" is also revealed.', 
  'posterpath': '/rODS466qSdrwMlGdbUwPENhDN2c.jpg'
 }, 
 7: 
 {'name': 'Batman: The Long Halloween, Part Two', 
  'overview': "As Gotham City's young vigilante, the Batman, struggles to pursue a brutal serial killer, district attorney Harvey Dent gets caught in a feud involving the criminal family of the Falcones.", 
  'posterpath': '/5X1n5q08mZ7NpNpxehMFODxfNYq.jpg'
 }, 
 8: 
 {'name': 'Bartkowiak', 
  'overview': "After his brother dies in a car crash, a disgraced MMA fighter takes over the family nightclub — and soon learns his sibling's death wasn’t an accident.", 
  'posterpath': '/kOVko9u2CSwpU8zGj14Pzei6Eco.jpg'
 }, 
 9: 
 {'name': 
  'Blood Red Sky', 
  'overview': 'A woman with a mysterious illness is forced into action when a group of terrorists attempt to hijack a transatlantic overnight flight. In order to protect her son she will have to reveal a dark secret, and unleash the inner monster she has fought to hide.', 
  'posterpath': '/ky8Fua6PD7FyyOA7JACh3GDETli.jpg'
 }, 
 10: 
 {'name': '킹덤: 아신전', 
  'overview': 'Tragedy, betrayal and a mysterious discovery fuel a woman\'s vengeance for the loss of her tribe and family in this special episode of "Kingdom."', 
  'posterpath': '/piGZDwFW4urLYDWGiYJMrt6hdCS.jpg'
 }, 
 11: 
 {'name': 'Space Jam: A New Legacy', 
  'overview': "When LeBron and his young son Dom are trapped in a digital space by a rogue A.I., LeBron must get them home safe by leading Bugs, Lola Bunny and the whole gang of notoriously undisciplined Looney Tunes to victory over the A.I.'s digitized champions on the court. It's Tunes versus Goons in the highest-stakes challenge of his life.", 
  'posterpath': '/5bFK5d3mVTAvBCXi5NPWH0tYjKl.jpg'
 }, 
 12: 
 {'name': 'A Quiet Place Part II', 
  'overview': 'Following the events at home, the Abbott family now face the terrors of the outside world. Forced to venture into the unknown, they realize that the creatures that hunt by sound are not the only threats that lurk beyond the sand path.', 
  'posterpath': '/4q2hz2m8hubgvijz8Ez0T2Os2Yv.jpg'
 }, 
 13: 
 {'name': 'Fast & Furious 10', 
  'overview': 'The tenth installment in the Fast Saga.', 
  'posterpath': '/2DyEk84XnbJEdPlGF43crxfdtHH.jpg'
 }, 
 14: 
 {'name': 'Luca', 
  'overview': 'Luca and his best friend Alberto experience an unforgettable summer on the Italian Riviera. But all the fun is threatened by a deeply-held secret: they are sea monsters from another world just below the water’s surface.', 
  'posterpath': '/jTswp6KyDYKtvC52GbHagrZbGvD.jpg'
 }, 
 15: 
 {'name': 'The Suicide Squad', 
  'overview': 'Supervillains Harley Quinn, Bloodsport, Peacemaker and a collection of nutty cons at Belle Reve prison join the super-secret, super-shady Task Force X as they are dropped off at the remote, enemy-infused island of Corto Maltese.', 
  'posterpath': '/fQnNpfv1bssX9qoyGVF2coQXayS.jpg'
 }, 
 16: 
 {'name': 'The Forever Purge', 
  'overview': 'All the rules are broken as a sect of lawless marauders decides that the annual Purge does not stop at daybreak and instead should never end as they chase a group of immigrants who they want to punish because of their harsh historical past.', 
  'posterpath': '/uHA5COgDzcxjpYSHHulrKVl6ByL.jpg'
 }, 
 17: 
 {'name': "Hitman's Wife's Bodyguard", 
  'overview': "The world’s most lethal odd couple – bodyguard Michael Bryce and hitman Darius Kincaid – are back on another life-threatening mission. Still unlicensed and under scrutiny, Bryce is forced into action by Darius's even more volatile wife, the infamous international con artist Sonia Kincaid. As Bryce is driven over the edge by his two most dangerous protectees, the trio get in over their heads in a global plot and soon find that they are all that stand between Europe and a vengeful and powerful madman.", 
  'posterpath': '/6zwGWDpY8Zu0L6W4SYWERBR8Msw.jpg'
 }, 
 18: 
 {'name': 'The Boy Behind the Door', 
  'overview': 'After Bobby and his best friend Kevin are kidnapped and taken to a strange house in the middle of nowhere, Bobby manages to escape. But as he starts to make a break for it, he hears Kevin’s screams for help and realizes he can’t leave his friend behind.', 
  'posterpath': '/cd0T7Wv9ek03iwYY0wsnkgoqImq.jpg'
 }, 
 19: 
 {'name': 'Old', 
  'overview': 'A group of families on a tropical holiday discover that the secluded beach where they are staying is somehow causing them to age rapidly – reducing their entire lives into a single day.', 
  'posterpath': '/cGLL4SY6jFjjUZkz2eFxgtCtGgK.jpg'
 }
}


# movie ex
{'page': 1, 
 'results': [
     {'original_language': 'en', 
      'original_title': 'F9', 
      'poster_path': '/bOFaAXmWWXC3Rbv4u4uM9ZSzRXP.jpg', 
      'video': False, 
      'title': 'F9', 
      'overview': "Dominic Toretto and his crew battle the most skilled assassin and high-performance driver they've ever encountered: his forsaken brother.", 
      'release_date': '2021-05-19', 
      'vote_count': 1064, 
      'vote_average': 7.8, 
      'adult': False, 
      'backdrop_path': '/4epzcO9HGbfc8BUJT0oNkL3rmCO.jpg', 
      'id': 385128, 
      'genre_ids': [28, 80, 53], 
      'popularity': 2135.78, 
      'media_type': 'movie'
     }, 
     {'id': 497698, 
      'genre_ids': [28, 12, 53, 878], 
      'original_language': 'en', 
      'original_title': 'Black Widow', 
      'poster_path': '/qAZ0pzat24kLdO3o8ejmbLxyOac.jpg', 
      'video': False, 
      'vote_average': 7.9, 
      'overview': 'Natasha Romanoff, also known as Black Widow, confronts the darker parts of her ledger when a dangerous conspiracy with ties to her past arises. Pursued by a force that will stop at nothing to bring her down, Natasha must deal with her history as a spy and the broken relationships left in her wake long before she became an Avenger.', 
      'release_date': '2021-07-07', 
      'vote_count': 3490, 
      'title': 'Black Widow', 
      'adult': False, 
      'backdrop_path': '/keIxh0wPr2Ymj0Btjh4gW7JJ89e.jpg', 
      'popularity': 4123.574, 
      'media_type': 'movie'
     }, 
     {'id': 631843, 
      'overview': 'A group of families on a tropical holiday discover that the secluded beach where they are staying is somehow causing them to age rapidly – reducing their entire lives into a single day.', 
      'release_date': '2021-07-21', 
      'adult': False, 
      'backdrop_path': '/q2mtFwvQQbun4nM9p16gA3Hqb0H.jpg', 
      'genre_ids': [9648, 53], 
      'vote_count': 179, 
      'original_language': 'en', 
      'original_title': 'Old', 
      'poster_path': '/cGLL4SY6jFjjUZkz2eFxgtCtGgK.jpg', 
      'title': 'Old', 
      'video': False, 
      'vote_average': 6.6, 
      'popularity': 521.164, 
      'media_type': 'movie'
     }
 ], 
 'total_pages': 1000, 'total_results': 20000
}