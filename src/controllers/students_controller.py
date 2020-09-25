from src.app import app
from flask import request, Response
import src.controllers.students_func as sfu
from src.helpers.json_response import asJsonResponse
from src.database import db

@app.route("/student/create/<student_name>")
@asJsonResponse
def create_student(student_name):
    """Check if the user is parf of ironhack datama0820 and if the user has been add or not"""
 
    if sfu.user_already_in_db(student_name):
        return f"{student_name} ya existe en la base de datos."

        
    if sfu.user_already_in_col(student_name):
        return sfu.insert_new_student(student_name)
    else:
        return f"El usuario {student_name} no es parte de Ironhack Datamad0820."


@app.route("/student/all")
@asJsonResponse

def search_students():
    """display all Ironhack students from datamad0820"""

    students = db.students.find({}, {'_id': 0})

    return students