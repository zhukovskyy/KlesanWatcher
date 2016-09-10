from flask import Blueprint

app = Blueprint(
    'db', __name__, template_folder='templates'
)


@app.route('/')
def index():
    return "Klassen Watcher"
