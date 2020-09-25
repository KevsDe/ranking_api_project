from src.app import app
from flask import request, Response
import src.controllers.labs_func as lfu
from src.database import db
from pymongo import MongoClient
from bson.objectid import ObjectId
from src.helpers.json_response import asJsonResponse
from random import choice

@app.route("/lab/create/<lab_name>")
@asJsonResponse
def create_lab(lab_name):
    """Check if the lab is parf of ironhack datama0820 and if the lab has been add or not"""

    if lfu.lab_already_in_db(lab_name):
        return f"{lab_name} already exist in the data."

        
    if lfu.lab_already_in_col(lab_name):
        return lfu.insert_new_lab(lab_name)
    else:
        return f"The {lab_name} has not been part of Ironhack Datamad0820."


@app.route("/lab/<lab_id>/search")
@asJsonResponse
def lab_analysis(lab_id):
    amanda, felipe, juan, al, fl, jl= lfu.teacher_time(lab_id)

    return {
        "Number of open PR": db.pull.count_documents({'$and':[ {'lab_id':ObjectId(f'{lab_id}')}, {'state':'open'} ]}),
        "Number of closed PR":db.pull.count_documents({'$and':[ {'lab_id':ObjectId(f'{lab_id}')} , {'state':'closed'} ]}),
        "Percentage of completeness": float(f"{(db.pull.count_documents({'$and':[ {'lab_id':ObjectId(f'{lab_id}')}, {'state':'closed'} ]})/(db.pull.count_documents({'$and':[ {'lab_id':ObjectId(f'{lab_id}')}, {'state':'open'} ]})+db.pull.count_documents({'$and':[ {'lab_id':ObjectId(f'{lab_id}')} , {'state':'closed'} ]}))*100):.2f}"),
        "Students who have not delivered the pull request":lfu.missing_pr(lab_id),
        "Number of students who have not delivered the pull request":len(lfu.missing_pr(lab_id)),
        "List of unique memes used for the lab":lfu.meme_pr(lab_id),
        "Amanda grade time in hours":f'It took Amanda {amanda} hours to correct {al} labs',
        "Felipe grade time in hours":f'It took Felipe {felipe} hours to correct {fl} labs',
        "Juan grade time in hours":f'It took Juan {juan} hours to correct {jl} labs'
    }



@app.route("/lab/memeranking")
@asJsonResponse
def memeranking():
    return lfu.ranking_meme()



@app.route("/lab/<lab_id>/meme")
@asJsonResponse
def random_meme(lab_id):
    x = choice(lfu.meme_pr(lab_id))
    return f'The Ironhack staff worked very hard selecting this meme, enjoy it {x}'


