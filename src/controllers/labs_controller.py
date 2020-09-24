from src.app import app
from flask import request, Response
import src.controllers.labs_func as lfu
from src.helpers.json_response import asJsonResponse
from src.database import db

@app.route("/lab/create/<lab_name>")
def create_lab(lab_name):
    """Check if the lab is parf of ironhack datama0820 and if the lab has been add or not"""

    if lfu.lab_already_in_db(lab_name):
        return f"{lab_name} ya existe en la base de datos."

        
    if lfu.lab_already_in_col(lab_name):
        return lfu.insert_new_lab(lab_name)
    else:
        return f"El lab {lab_name} no ha sido parte de Ironhack Datamad0820."


@app.route("/lab/<lab_id>/search")