import src.api_extraction as ape
import src.webscraping as sws
import src.mongo_import as mip
import requests


#Get information from the last pull request.
num_last_pr = ape.get_github("/repos/ironhack-datalabs/datamad0820/pulls",query_params={"state":"all", "page":"1","per_page":"1"})

last_page, last_p = ape.last_pull(num_last_pr[0])

print(last_page)
print(last_p)

#Get a dictionary with all the pull request
lista_estudiantes = ape.get_all_pulls(last_page)

#Create a collection with all the lab titles
lista_titutlos = []
for x in range (0,len(lista_estudiantes)):
    lista_titutlos.append(lista_estudiantes[x].get('title'))


for name in list(set(lista_titutlos)):
    url_api = "http://0.0.0.0:3000//lab/create/"
    endpoint_api = name
    requests.get(url_api+endpoint_api)



#Create a collection with all the lab titles
lista_est = []
for x in range (0,len(lista_estudiantes)):
    lista_est.append(lista_estudiantes[x].get('users'))

for name in list(set(lista_est)):
    url_api = "http://0.0.0.0:3000/student/create/"
    endpoint_api = name
    requests.get(url_api+endpoint_api)

#Update de "pull" collection with the "labs" collection

mip.mongo_lab_id_update()