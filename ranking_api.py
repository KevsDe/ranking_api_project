import src.api_extraction as ape
import src.webscraping as sws


#Get information from the last pull request.
num_last_pr = ape.get_github("/repos/ironhack-datalabs/datamad0820/pulls",query_params={"state":"all", "page":"1","per_page":"1"})

last_page, last_p = ape.last_pull(num_last_pr[0])

print(last_page)
print(last_p)

#Get a dictionary with all the pull request
lista_estudiante = ape.get_all_pulls(last_page)

print(lista_estudiante[8])


print(sws.get_github_users(lista_estudiante[8]['html_url']))



lista_estudiante[10]['meme'] = sws.get_meme(lista_estudiante[10]['html_url'])

print(lista_estudiante[10])

