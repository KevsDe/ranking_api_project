from src.app import app
from flask import request, Response
import src.controllers.students_func as sfu
from src.database import db

@app.route("/student/create/<student_name>")
def create_student(student_name):
    """Check if the user is parf of ironhack datama0820 and if the user has been add or not"""
    collection = db.students
 
    if sfu.user_already_in_db(collection, student_name):
        return f"{student_name} ya existe en la base de datos."

        
    if sfu.user_already_in_col(student_name):
        return sfu.insert_new_student(collection, student_name)
    else:
        return f"El usuario {student_name} no es parte de Ironhack Datamad0820."

