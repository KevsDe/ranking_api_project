import requests
from dotenv import load_dotenv
import math
import itertools
import os
load_dotenv()


def get_github(endpoint, apiKey=os.getenv("GITHUB_APIKEY"), query_params={}):
    """
    Get data from github using query parameters and passing a custom apikey header
    """

    # Compose the endpoint url
    baseUrl = "https://api.github.com"
    url = f"{baseUrl}{endpoint}"

    # Create the headers
    headers = {
        "Authorization": f"Bearer {apiKey}"
    }
    # make the request and get the response using HTTP GET verb
    res = requests.get(url, params=query_params, headers=headers)

    print(f"Request data to {res.url} status_code:{res.status_code}")
    data = res.json()

    if res.status_code != 200:
        raise ValueError(f'Invalid github api call: {data["message"]}')

    return data


def last_pull(data):

    """Create a dictionary with the number of the last pull request in a repository"""
    num = int(data['number'])
    page = math.ceil(num/100)
    return (page,num)


def api_extraction(data):

    """Create a dictionary with the selected information received from the github api"""
    dictionary=[]
    for x in range(0,len(data)):

        name={'number':data[x]['number'],
        'title':data[x]['title'],
        'user':data[x]['user']['login'],
        'state':data[x]['state'],
        'created_at':data[x]['created_at'],
        'updated_at':data[x]['updated_at'],
        'closed_at':data[x]['closed_at'],
        'html_url':data[x]['html_url']
        }
        dictionary.append(name)

    return dictionary


def get_all_pulls(last_page):
    """Get the information from all the github issues pages from a selected repository"""
    pull = []
    for page in range(1, last_page + 1):
        pull.append(api_extraction(get_github(f"/repos/ironhack-datalabs/datamad0820/issues",query_params={"state": "all", "page": {page}, "per_page": "100"})))
    merged = list(itertools.chain.from_iterable(pull))
    return merged