from flask import *
import os
import hashlib
from extensions import connect_to_database
pic = Blueprint('pic', __name__, template_folder='templates')

image_names = [ filename for filename in os.listdir('static/image_hash')]

@pic.route('/pic')
def pic_route():
	db = connect_to_database()
	cur = db.cursor()
	cur.execute('SELECT * FROM Contain ;')
	results = cur.fetchall()


	image_list = [ result['picid'] for result in results]
	#image_list = [ filename for filename in os.listdir('static/image_hash')]

	pic_name=request.args.get("picid")
	#albumid=request.args.get("albumid")
	#albumid=1
	pic_num=image_list.index(pic_name)
	return render_template("pic.html",total_list=results,image_list=image_list,i=pic_num,len=len(image_list))
'''
if __name__ == '__main__':
	main():
		print (cur_id)
'''