import cv2
import numpy as np
import os
import argparse

#imname = args.file#'test.png'
def saveSegments(imname,savedir,pad=4):
	# Load the image
	img = cv2.imread(imname)

	# convert to grayscale
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	# smooth the image to avoid noises
	gray = cv2.medianBlur(gray,5)

	# Apply adaptive threshold
	thresh = cv2.adaptiveThreshold(gray,255,1,1,11,3)
	thresh_color = cv2.cvtColor(thresh,cv2.COLOR_GRAY2BGR)

	# apply some dilation and erosion to join the gaps
	thresh = cv2.dilate(thresh,None,iterations = 1)
	thresh = cv2.erode(thresh,None,iterations = 1)

	# Find the contours
	contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

	idx = 0
	if not os.path.exists("images"):
		os.mkdir("images")

	fn = "images/"+savedir
	if not os.path.exists(fn):
		os.mkdir(fn)

	# For each contour, find the bounding rectangle and draw it
	for cnt in contours:
	    x,y,w,h = cv2.boundingRect(cnt)
	    #if y >5 and x > 5:
	    try:
		    tmp = img[y-pad:y+h+pad,x-pad:x+w+pad]
		    cv2.imwrite(fn+"/"+str(idx)+".png",tmp)
		    idx+=1
	    except:
			print("oops")

imgs = os.listdir("pdfimgs")
for img in imgs:
	try:
		saveSegments("pdfimgs/"+img,img)
	except:
		print("oops")
