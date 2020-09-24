import re
from src.database import db
from src.helpers.json_response import asJsonResponse




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