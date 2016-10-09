from flask import Blueprint, render_template
from sms import send

app = Blueprint(
    'db', __name__, template_folder='templates'
)


@app.route('/')
def index():
    return "Klassen Watcher"


@app.route('/help')
def help():
    return render_template('base/help.html')


@app.route('/sms_test/phone_num/msg', methods=['POST'])
def sms_test(phone_number, msg):
    return str(send(phone_number, msg))
