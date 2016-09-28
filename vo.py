import numpy as np
import cv2
import linecache
from matplotlib import pyplot as plt

mtx = np.mat('621.11352456 0. 327.39163094; 0. 620.88453231 232.87088353; 0. 0. 1.') 
dist = np.array([ 0.13589782, -0.4714084,  -0.00517676,  0.00815842,  1.22439717])

MAX_FRAME = 1000
MIN_NUM_FEAT = 2000

def undistort(img, dist, mtx): #undistorstion routine
	h,  w = img.shape[:2]
	newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
	dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
	x,y,w,h = roi
	dst = dst[y:y+h, x:x+w]
	return dst

#testing undistort function 
img = cv2.imread("test.jpg",0)
#dst = undistort(img,dist,mtx)
#cv2.imwrite('undistor_test.png',dst)

def feature_detection(img1, points1): 
	fast = cv2.FastFeatureDetector(20)		#sets the threshold
	fast.setBool('nonmaxSuppression',1)		#makes nonmaxsupresison true 
	kp = fast.detect(img1,None) 
	cd_x=np.array([k.pt[0] for k in kp])
	cd_y=np.array([k.pt[1] for k in kp])
	for i in range(len(cd_x)):
		points1.append([cd_x[i],cd_y[i]])
	#img1 = cv2.drawKeypoints(img1,kp,img1)		#for testing keypoint generation
	#cv2.imwrite('kp_test.png',img1)

#test feature detection 
#points1= []
#feature_detection(img,points1)
#print points1

'''def feature_tracking(img1,img2, points1,points2): #get reid of outliers wand track matching features

def main():
	scale = 1.
	retval1, img_1 = cv2.imread("",0) #read images and convert to grayscale
	retval2, img_2 = cv2.imread("",0)
	if (retval1 or retval2 == 0):
		print "Reading image failed. Please try again"
		return -1
    points1 = [] #lists to store feature points 
    points2 = [] 
    feature_detection(img1,points1)'''
    

