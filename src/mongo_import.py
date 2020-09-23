from pymongo import MongoClient

def mongo_import(lista):
    """Upload the info extractred from github to mongodb"""
    client = MongoClient(port=27017)
    db=client.datamad0820
    for x in range(0,len(lista)):
        result = db.pull.insert_one(lista[x])
    print(f'finished creating {len(lista)} pull requests')