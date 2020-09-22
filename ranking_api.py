import src.api_extraction as ape
import src.webscraping as sws
from pymongo import MongoClient


#Get information from the last pull request.
num_last_pr = ape.get_github("/repos/ironhack-datalabs/datamad0820/pulls",query_params={"state":"all", "page":"1","per_page":"1"})

last_page, last_p = ape.last_pull(num_last_pr[0])

print(last_page)
print(last_p)

#Get a dictionary with all the pull request
lista_estudiante = ape.get_all_pulls(last_page)

#print(lista_estudiante[4])

#ape.get_github("/repos/ironhack-datalabs/datamad0820/issues/comments",query_params={"state": "all", "page": "1", "per_page": "2", "sort":"created"})

sws.meme_lst(lista_estudiante)

print(lista_estudiante[4])


client = MongoClient(port=27017)
db=client.datamad0820
for x in range(0,5):
    result = db.pull.insert_one(lista_estudiante[x])


