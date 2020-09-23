import re
from src.database import db
from src.helpers.json_response import asJsonResponse




def user_already_in_db(username):
    
    result = db.students.find_one({"user": username})
    return result != None and len(result) > 0

def user_already_in_col(username):
    # Search a company in mongodb database
    projection = {'users':1}
    searchRE = re.compile(f"{username}", re.IGNORECASE)
    founduser = db["pull"].find_one(
        {"users": searchRE}, projection)

    return founduser != None and len(founduser) > 0


def insert_new_student(name):
    new_student = {
        "user": name
    }
    result = db.students.insert_one(new_student)
    return {"_id": str(result.inserted_id)}