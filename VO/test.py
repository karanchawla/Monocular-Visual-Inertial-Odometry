import numpy as np 
from glob import glob
import os
import os.path
import cv2

from visual_odometry import PinholeCamera, VisualOdometry


cam = PinholeCamera(752.0, 480.0, 458.654, 457.296, 367.215, 248.375)
vo = VisualOdometry(cam)

traj = np.zeros((600,600,3), dtype=np.uint8)

def rename_images():
#import os
#import os.path
#renames images for a dataset for easy import while maintaining the order
	img_types = ['.png']
	for dirpath, dirnames, fnames in os.walk(path):
		imgs = [f for f in fnames if os.path.splitext(f)[1] in img_types]
		imgs.sort()
		for j, im in enumerate(imgs):
			name, ext = os.path.splitext(im)
			os.rename(os.path.join(dirpath, im), os.path.join(dirpath,'{}.{}'.format(j, ext)))

def read_image():
	images = []
	img_mask = "/home/karan/datasets/mav0/cam0/data/*.png"
	for fn in glob(img_mask):
		img = cv2.imread(fn, -1)
		if img is not None:
			images.append(img)
	return images

for img_id in xrange(3000):
	#img = cv2.imread(str(img_id).zfill(6)+'.png', 0)
	img =cv2.imread('/home/karan/datasets/mav0/cam0/data/'+str(img_id)+"."+'.png', 0)
	if img is not None:
		vo.update(img, img_id)
	cur_t = vo.cur_t
	if(img_id > 2):
		x, y, z = cur_t[0], cur_t[1], cur_t[2]
	else:
		x, y, z = 0., 0., 0.
	draw_x, draw_y = int(x)+290, int(z)+90
	#true_x, true_y = int(vo.trueX)+290, int(vo.trueZ)+90

	cv2.circle(traj, (draw_x,draw_y), 1, (img_id*255/4540,255-img_id*255/4540,0), 1)
	#cv2.circle(traj, (true_x,true_y), 1, (0,0,255), 2)
	cv2.rectangle(traj, (10, 20), (600, 60), (0,0,0), -1)
	text = "Coordinates: x=%2fm y=%2fm z=%2fm"%(x,y,z)
	cv2.putText(traj, text, (20,40), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1, 8)

	cv2.imshow('Road facing camera', img)
	cv2.imshow('Trajectory', traj)
	cv2.waitKey(1)

cv2.imwrite('map.png', traj)
