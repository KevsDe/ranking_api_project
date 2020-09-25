import re
from src.database import db
from src.helpers.json_response import asJsonResponse




def user_already_in_db(username):
    """Check if an student has been add to the database"""
    result = db.students.find_one({"user": username})
    return result != None

def user_already_in_col(username):
    """Check if an student has been add to the database"""
    projection = {'users':1}
    searchRE = re.compile(f"{username}", re.IGNORECASE)
    founduser = db["pull"].find_one(
        {"users": searchRE}, projection)

    return founduser != None


def insert_new_student(name):
    """Add a new student to the database"""
    new_student = {
        "user": name
    }
    result = db.students.insert_one(new_student)
    return {"_id": str(result.inserted_id)}