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