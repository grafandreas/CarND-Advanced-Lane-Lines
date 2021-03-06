import perspective
import distorter
import lanefinder
import gradient
import cv2
import curvature
import threshold
import numpy as np

class Pipeline:
    def __init__(self) :
        self.ds = distorter.Distorter()
        self.tr = perspective.PerspectiveTrafo(perspective.PerspectiveTrafo.DEFAULT_SRC,perspective.PerspectiveTrafo.DEFAULT_DST,(1280,720))
        self.lf = lanefinder.LaneFinder()

    def process(self,img) :
        limg = self.ds.distortx(img)
        limg = self.tr.warp(limg) 

        bw = gradient.abs_sobel_thresh(limg,thresh_min=30,thresh_max=170,value=255)
        bw2 = threshold.thresholdYellow(limg)

        bw = np.maximum(bw,bw2)

        res = self.lf.findLanes(bw)
        if(res != None) :
            (out,l,r,lcr,rcr) = res
            overlay(img,cv2.resize(out,(0,0),fx=0.25,fy=0.25),640,0)
            lanOv = self.lf.draw(out,l,r,self.tr)
            overlay(img,cv2.resize(lanOv,(0,0),fx=0.25,fy=0.25),960,0)
            img = cv2.addWeighted(img, 1, lanOv, 0.3, 0)
            (lcurve,rcurve) =  curvature.curvature(lcr,rcr)
            cv2.putText(img,"Curvature : "+'{:06.2f}'.format(lcurve)+" - "+ '{:06.2f}'.format(rcurve), (500,300), cv2.FONT_HERSHEY_SIMPLEX,1.0,[255,255,255])
            (ll,lr,coff) = curvature.lanepos(l,r)
            cv2.putText(img,"Pos : "+'{:06.2f}'.format(ll)+" - "+ '{:06.2f}'.format(lr)+" - "+ '{:06.2f}m'.format(coff), (500,340), cv2.FONT_HERSHEY_SIMPLEX,1.0,[255,255,255])
        else:
            print("Lane find was none")

        overlay(img,cv2.resize(limg,(0,0),fx=0.25,fy=0.25),0,0)
        bwrgb = cv2.cvtColor(bw,cv2.COLOR_GRAY2RGB)
        overlay(img,cv2.resize(bwrgb,(0,0),fx=0.25,fy=0.25),320,0)

        
        return img   


def overlay(l_img,s_img,x_offset,y_offset) :
    l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img