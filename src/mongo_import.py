from pymongo import MongoClient
from config import DBURL
from bson.objectid import ObjectId
from datetime import datetime

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

    projection = {'id':1,'lab_name':1 }
    for x in db.labs.find({},projection):
        myquery = {'lab_id':x['lab_name']}
        newvalues = {'$set':{'lab_id':x['_id']}}

        db.pull.update_many(myquery,newvalues)  
    



"""all_students = ['Daniel-GarciaGarcia', 'grundius1', 'VanessaMacC', 'FDELTA', 'Joycelili', 'Jav1-Mart1nez', 'marta-zavala', 'PaulaNuno', 'jorge-alamillos', 'laura290', 'KevsDe', 'miguelgimenezgimenez', 'AnaMA96', 'gontzalm', 'charliesket', 'IreneLopezLujan', 'silviaherf', 'Davidlazarog', 'rfminguez', 'jmena23', 'bmedm', 'DiegoCaulonga', 'CarlosSanzDGP', 'Diegon8']

not_delivered = []
projection = {'users':1,'_id':0}
for x in db.pull.find({'lab_id':ObjectId('5f6cf5f9730aa5fbbe42cac9')},projection):
    for student in x.get('users'):
        if student[1:] not in all_students:
            not_delivered.append(student)
print (not_delivered)
print(len(not_delivered))"""


"""memes = []
projection = {'meme':1,'_id':0}
for meme in db.pull.find({'lab_id':ObjectId('5f6cf5f9730aa5fbbe42cac9')},projection):
    if meme.get('meme') != None:
        memes.append(meme.get('meme'))
memes = list(set(memes))
print(memes)"""


"""juan_time = 0
amanda_time = 0
felipe_time = 0
juan_labs = 0
amanda_labs = 0
felipe_labs = 0
projection = {'teacher':1,'_id':0, 'last_commit':1, 'closed_at':1}
for x in db.pull.find({'$and':[ {'lab_id':ObjectId('5f6cf5f9730aa5fbbe42cac9')} , {'state':'closed'} ]},projection):
    close_time = datetime.strptime(x.get('closed_at'), "%Y-%m-%dT%H:%M:%SZ")
    open_time = datetime.strptime(x.get('last_commit'), "%Y-%m-%dT%H:%M:%SZ")
    queue_time = (close_time-open_time).total_seconds()/3600

    if x.get('teacher') == 'ferrero-felipe':
        felipe_labs+=1
        felipe_time+=queue_time
    elif x.get('teacher') == 'agalvezcorell':
        amanda_labs+=1
        amanda_time+=queue_time
    elif x.get('teacher') == 'WHYTEWYLL':
        juan_labs+=1
        juan_time+=queue_time
        
if felipe_time != 0:
    print(f'{felipe_time/felipe_labs:.2f}')
if amanda_time != 0:
    print(f'{amanda_time/amanda_labs:.2f}')
if juan_time != 0:
    print(f'{juan_time/juan_labs:.2f}')"""