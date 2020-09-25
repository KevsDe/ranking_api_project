from src.app import app
import src.controllers.students_controller
import src.controllers.labs_controller
from config import PORT

app.run("0.0.0.0", PORT, debug=True)
