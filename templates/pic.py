from flask import *
import os
import hashlib
pic = Blueprint('pic', __name__, template_folder='templates')

image_names = [ filename for filename in os.listdir('..\static\images\pa1_images\images')]
@pic.route('/pic')
def pic_route():
	#return render_template("pic.html")
	pre_id="file:///C:/Users/user/Desktop/485/p1-starter-code-master/p1-starter-code-master/static/images/pa1_images/images/"+image_names[0]
	cur_id="file:///C:/Users/user/Desktop/485/p1-starter-code-master/p1-starter-code-master/static/images/pa1_images/images/"+image_names[1]
	next_id="file:///C:/Users/user/Desktop/485/p1-starter-code-master/p1-starter-code-master/static/images/pa1_images/images/"+image_names[2]
	return render_template("pic.html", **options,pre_id=pre_id,cur_id=cur_id,next_id=next_id)