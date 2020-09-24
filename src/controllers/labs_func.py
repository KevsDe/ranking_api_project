import re
from src.database import db
from src.helpers.json_response import asJsonResponse
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime




def lab_already_in_db(labname):
    
    result = db.labs.find_one({"lab_name":labname})
    return result != None and len(result) > 0

def lab_already_in_col(labname):
    """Find out if the lab name is in the db"""
    projection = {'title':1}
    searchRE = re.compile(f"{labname}", re.IGNORECASE)
    foundlab = db["pull"].find_one(
        {"title": searchRE}, projection)

    return foundlab != None and len(foundlab) > 0


def insert_new_lab(labname):
    new_lab = {
        "lab_name": labname,
        "lab_name_pull": f"[{labname}]".replace(' ','-')
        }
    result = db.labs.insert_one(new_lab)
    return {"_id": str(result.inserted_id)}



def missing_pr(lab_id):
    all_students = []
    projection = {'user':1,'_id':0}
    for x in db.students.find({},projection):
        all_students.append(x.get('user'))
            
    not_delivered = []
    projection = {'users':1,'_id':0}
    for x in db.pull.find({'lab_id':ObjectId(f'{lab_id}')},projection):
        for student in x.get('users'):
            if student[1:] not in all_students:
                not_delivered.append(student)
    return not_delivered



def meme_pr(lab_id):
    memes = []
    projection = {'meme':1,'_id':0}
    for meme in db.pull.find({'lab_id':ObjectId(f'{lab_id}')},projection):
        if meme.get('meme') != None:
            memes.append(meme.get('meme'))
    memes = list(set(memes))
    return memes

def teacher_time(lab_id):
    juan_time = 0
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
    
        
    if felipe_time != 0 and amanda_time != 0 and juan_time != 0:
        amanda = f'{amanda_time/amanda_labs:.2f}'
        felipe = f'{felipe_time/felipe_labs:.2f}'
        juan =f'{juan_time/juan_labs:.2f}'
        return amanda,felipe,juan
    else: 
        amanda = f'{amanda_time/amanda_labs:.2f}'
        felipe = f'{felipe_time/felipe_labs:.2f}'
        juan = 0
        return amanda,felipe,juan,amanda_labs,felipe_labs,juan_labs
