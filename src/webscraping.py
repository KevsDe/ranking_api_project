import requests
import bs4
import re
import itertools

def get_meme(url):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    try:
        img = soup.select('.edit-comment-hide')[1].select('img')[0].get('src')
        return img
    except:
        return None


def get_github_users(url):
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
    """Insert the meme url from the comment poge"""
    for x in range(0,len(lista)):
        print(x)
        lista[x]['users'] = get_github_users(lista[x]['html_url'])
        lista[x]['meme'] = get_meme(lista[x]['html_url'])

