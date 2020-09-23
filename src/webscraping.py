import requests
import bs4
import re
import itertools
import time

def get_meme(url):
    """Web scraping for github comment page to extract the instructor comment meme"""
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    try:
        img = soup.select('.edit-comment-hide')[1].select('img')[0].get('src')
        return img
    except:
        return None


def get_github_users(url):
    """Web scraping for github comment page to get the students github user"""
    teachers = ['@ferrero', '@WHYTEWYLL', '@agalvezcorell', '@github']
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    user_github = re.findall("@\w*", str(soup))
    user_github = list(set(user_github))
    for teacher in teachers:
        if teacher in user_github:
            user_github.remove(teacher)

    return user_github


   


def meme_lst(lista):
    """Insert the meme url and students github users from the comment poge to the dictionary with the info extracted from the github api"""
    for x in range(0,(len(lista))):
        print(x)
        lista[x]['users'] = get_github_users(lista[x]['html_url'])
        print(get_github_users(lista[x]['html_url']))
        lista[x]['meme'] = get_meme(lista[x]['html_url'])
        time.sleep(3)

