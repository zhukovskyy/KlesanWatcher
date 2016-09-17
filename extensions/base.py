from flask import Blueprint, render_template

app = Blueprint(
    'db', __name__, template_folder='templates'
)


@app.route('/')
def index():
    return "Klassen Watcher"

@app.route('/help')
def help():
    return render_template('base/help.html')
