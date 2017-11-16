import pickle
import cv2

class Distorter:
    FILE = "distort.p"

    def __init__(self) :
        self.mtx,self.dist = pickle.load(open(Distorter.FILE,"rb"))

    def distortx(self,img) :
        return cv2.undistort(img,self.mtx,self.dist)
