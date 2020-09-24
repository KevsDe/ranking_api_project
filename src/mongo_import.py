from pymongo import MongoClient
from config import DBURL
def mongo_import(lista):
    """Upload the info extractred from github to mongodb"""
    client = MongoClient(port=27017)
    db=client.datamad0820
    for x in range(0,len(lista)):
        result = db.pull.insert_one(lista[x])
    print(f'finished creating {len(lista)} pull requests')


client = MongoClient(port=27017)
db=client.datamad0820



def mongo_lab_id_update():
    myquery = {'lab_name_pull':'[lab-api-scavenger-game]'}
    newvalues = {'$set':{'lab_name_pull':'cambiado'}}

    db.labs.update_many(myquery,newvalues)

    projection = projection = {'id':1,'lab_name':1 }
    for x in db.labs.find({},projection):
        myquery = {'lab_id':x['lab_name']}
        newvalues = {'$set':{'lab_id':x['_id']}}

        db.pull.update_many(myquery,newvalues)  
    

 
