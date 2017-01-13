# parse_data.py
import hashlib
import os
import datetime
import time
import shutil 
# User - username, firstname, lastname, password, email
def user():
	user = []
	user.append(['sportslover','Paul','Walker','paulpass93','sportslover@hotmail.com'])
	user.append(['traveler','Rebecca','Travolta','rebeccapass15','rebt@explorer.org'])
	user.append(['spacejunkie','Bob','Spacey','bob1pass','bspace@spacejunkies.net'])
	return user

# album - albumid, title, created, lastupdated, username
def album():
	album = []
	st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	st="TIMESTAMP '"+st+"'" 
	album.append(['1','I love sports',st,st,'sportslover'])
	album.append(['2','I love football',st,st,'sportslover'])
	album.append(['3','Around The World',st,st,'traveler'])
	album.append(['4','Cool Space Shots',st,st,'spacejunkie'])
	return album

# Contain - sequencenum, albumid, picid, caption

def contain():
    image_names = [ filename for filename in os.listdir('static/images')]

    src = 'images'
    target = 'image_hash'
    if not os.path.isdir(target):
        os.mkdir(target)

    albumid_lst = [2]*4 + [4]*5 + [1]*8 +[3]*13
    contain =[];
    for i,im_name in enumerate(image_names):
        albumid = albumid_lst[i]
        ptype = im_name.split('.')[1]
        m = hashlib.md5((str(albumid) + im_name).encode('utf-8'))
        contain.append([i,albumid,m.hexdigest(),''])

        new_name = (m.hexdigest() + '.' + ptype)
        shutil.copy(os.path.join(src,im_name),os.path.join(target,new_name))
        #print i, albumid, im_name
    return contain


# Photo - picid, format, date
def photo():
	image_names = [ filename for filename in os.listdir('static/images')]
	albumid_lst = [2]*4 + [4]*5 + [1]*8 +[3]*13
	photo =[];
	for i,im_name in enumerate(image_names):
		albumid = albumid_lst[i]
		ptype = im_name.split('.')[1]
		m = hashlib.md5((str(albumid) + im_name).encode('utf-8'))
		#date
		st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
		st="TIMESTAMP '"+st+"'" 
		photo.append([m.hexdigest(),ptype,st])
		#print i, albumid, im_name
	return photo