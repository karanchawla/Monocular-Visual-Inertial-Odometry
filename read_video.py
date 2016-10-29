import numpy as np 
import cv2
from glob import glob
import os

'''cap = cv2.VideoCapture(1)

while(True):
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()'''
'''
images = []
img_mask = "/home/karan/datasets/mav0/cam0/data/*.png"
for fn in glob(img_mask):
	img = cv2.imread(fn, -1)
	if img is not None:
	    images.append(img)'''

path = '/home/karan/datasets/mav0/cam0/data/'

import os
import os.path
img_types = ['.png']
for dirpath, dirnames, fnames in os.walk(path):
    imgs = [f for f in fnames if os.path.splitext(f)[1] in img_types]
    imgs.sort()
    for j, im in enumerate(imgs):
        name, ext = os.path.splitext(im)
        os.rename(os.path.join(dirpath, im), os.path.join(dirpath,'{}.{}'.format(j, ext)))

