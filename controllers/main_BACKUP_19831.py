<<<<<<< HEAD
from flask import *

from extensions import connect_to_database

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def main_route():
    return render_template("files.php")

@main.route('/hello')
def main_hello():
    db = connect_to_database()
    cur = db.cursor()
    cur.execute('SELECT id, name FROM test_tbl')
    results = cur.fetchall()
    print(results)
    print_str = "<table>"
    for result in results:
        print_str += "<tr><td>%s</td><td>%s</td><tr>" % (result['id'], result['name'])
    print_str += "</table>"
    return print_str
=======
from flask import *
from extensions import connect_to_database

main = Blueprint('main', __name__, template_folder='templates')
@main.route('/')
def main_route():
    name_list=['sportslover','traveler','spacejunkie']

    return render_template("index.html",name_list=name_list)

@main.route('/hello')
def main_hello():
    db = connect_to_database()
    cur = db.cursor()
    cur.execute('SELECT id, name FROM test_tbl')
    results = cur.fetchall()
    print(results)
    print_str = "<table>"
    for result in results:
        print_str += "<tr><td>%s</td><td>%s</td><tr>" % (result['id'], result['name'])
    print_str += "</table>"
    return print_str
>>>>>>> af9bde7b6e9f55bcab9cef29a6f4bfda084adaa3
