import cv2
import numpy as np
import glob


class PerspectiveTrafo:
    M= []

    def __init__(self, src,dst,img_size=(1300,1300)):
        self.M = cv2.getPerspectiveTransform(src,dst)
        self.Minv = cv2.getPerspectiveTransform(dst,src)
        self.img_size = img_size

    def warp(self,img) :
        return cv2.warpPerspective(img, self.M, self.img_size, flags=cv2.INTER_LINEAR)

    def warpInv(self,img) :
        return cv2.warpPerspective(img, self.M)#, img_size, flags=cv2.INTER_LINEAR)
