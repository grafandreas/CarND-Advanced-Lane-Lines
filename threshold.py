import cv2
import glob
import numpy as np

def loadImagesHLS(path):
    image_list=[]
    for fn in glob.glob(path+"/*.jpg"):
        im = cv2.imread(fn)
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2HLS)
        image_list.append(gray)
    return image_list

def thresholdS(img,thresh=(0,255),value=1):
    S = img[:,:,2]
    binary = np.zeros_like(S)
    binary[(S >= thresh[0]) & (S <= thresh[1])] = value
    return binary

def thresholdRGB(img,thresh=(0,255),value=1):
    hls = cv2.cvtColor(img,cv2.COLOR_RGB2HLS)
    return thresholdS(hls,thresh,value)

def thresholdYellow(img) :
    imgHSV = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    res = cv2.inRange(imgHSV, np.array( [20, 100, 100]), np.array( [30, 255, 255] ) )
    return res