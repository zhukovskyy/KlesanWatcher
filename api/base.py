from flask import Blueprint, render_template

app = Blueprint(
    'db', __name__, template_folder='templates'
)
route = lambda x: app.route('/' + __name__.replace('.', '/') + x)


@app.route('/')
def index():
    return render_template('base/home.html')


@route('/version')
def version():
    return "Production pre-alpha"

