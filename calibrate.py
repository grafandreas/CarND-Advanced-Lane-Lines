import cv2
import glob
import numpy as np

CHESS=(9,6)

# The object point list
objp = np.zeros((9*6,3), np.float32)
objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)


def loadImages(path):
    image_list=[]
    for fn in glob.glob(path+"/*.jpg"):
        im = cv2.imread(fn)
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        image_list.append(gray)
    return image_list

def findCorner(img) :
    ret, corners = cv2.findChessboardCorners(img, CHESS, None)
    return ret,corners

def calcCalibration(coL):
    objpoints = [] # 3d point in real world space
    imgpoints = [] 

    for c in coL:
        objpoints.append(objp)
        imgpoints.append(c)

    #
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, (720,1280),None,None)
    return ret, mtx, dist, rvecs, tvecs

def calibrateFromDir(path):
        imgs = loadImages(path)
        cML = []
        for img in imgs:
             ret, corners = findCorner(img)
             if(ret):
                 cML.append(corners)

        return calcCalibration(cML)