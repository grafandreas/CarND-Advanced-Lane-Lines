import cv2
import glob
import numpy as np
import imageloader

CHESS=(9,6)

# The object point list
objp = np.zeros((9*6,3), np.float32)
objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)




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
        imgs = imageloader.loadImagesRGB(path)
        cML = []
        for img in imgs:
             ret, corners = findCorner(img)
             if(ret):
                 cML.append(corners)

        return calcCalibration(cML)