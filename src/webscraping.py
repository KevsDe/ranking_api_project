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
        return 'Not meme available'


def get_github_users(url):
    teachers = ['@ferrero','@WHYTEWYLL','@agalvezcorell']
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    user_github = [re.findall("@\w*",str(soup.find("div", {"id": "partial-users-participants"}).findAll('img')[e])) for e in range(0,len(soup.find("div", {"id": "partial-users-participants"}).findAll('img')))]
    merged = list(itertools.chain.from_iterable(user_github))
    for x in teachers:
        if x in merged:
            merged.remove(x)

    return merged