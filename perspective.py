import cv2
import numpy as np
import glob


class PerspectiveTrafo:
    M= []

    def __init__(self, src,dst,img_size=(300,300)):
        self.M = cv2.getPerspectiveTransform(src,dst)
        self.Minv = cv2.getPerspectiveTransform(dst,src)

    def warp(self,img) :
        img_size = (img.shape[1],img.shape[0])
        return cv2.warpPerspective(img, self.M, img_size, flags=cv2.INTER_LINEAR)

    def warpInv(self,img) :
        return cv2.warpPerspective(img, self.M)#, img_size, flags=cv2.INTER_LINEAR)
