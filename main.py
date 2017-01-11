from flask import *

from extensions import connect_to_database

main = Blueprint('main', __name__, template_folder='templates')
##YAYA
@main.route('/')
def main_route():
    return render_template("index.html")

@main.route('/hello')
def main_hello():
    db = connect_to_database()
    cur = db.cursor()
    cur.execute('SELECT id, name FROM test')
    results = cur.fetchall()
    print(results)
    print_str = "<table>"
    for result in results:
        print_str += "<tr><td>%s</td><td>%s</td><tr>" % (result['id'], result['name'])
    print_str += "</table>"
    return print_str

from flask import *
import os
import hashlib
pic = Blueprint('pic', __name__, template_folder='templates')


@main.route('/pic')
def main_pic():
    return render_template("pic.html")
    """
    image_names = [ filename for filename in os.listdir('..\static\images\pa1_images\images')]
    pre_id="file:///C:/Users/user/Desktop/485/p1-starter-code-master/p1-starter-code-master/static/images/pa1_images/images/"+image_names[0]
    cur_id="file:///C:/Users/user/Desktop/485/p1-starter-code-master/p1-starter-code-master/static/images/pa1_images/images/"+image_names[1]
    next_id="file:///C:/Users/user/Desktop/485/p1-starter-code-master/p1-starter-code-master/static/images/pa1_images/images/"+image_names[2]
    return render_template("pic.html", **options,pre_id=pre_id,cur_id=cur_id,next_id=next_id)
    """