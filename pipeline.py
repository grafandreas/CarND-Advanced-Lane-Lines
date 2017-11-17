import perspective
import distorter
import lanefinder
import gradient
import cv2

class Pipeline:
    def __init__(self) :
        self.ds = distorter.Distorter()
        self.tr = perspective.PerspectiveTrafo(perspective.PerspectiveTrafo.DEFAULT_SRC,perspective.PerspectiveTrafo.DEFAULT_DST,(1280,720))
        self.lf = lanefinder.LaneFinder()

    def process(self,img) :
        limg = self.ds.distortx(img)
        limg = self.tr.warp(limg) 
        bw = gradient.abs_sobel_thresh(limg,thresh_min=30,thresh_max=170,value=255)
      
        res = self.lf.findLanes(bw)
        if(res != None) :
            (out,l,r) = res
            overlay(img,cv2.resize(out,(0,0),fx=0.25,fy=0.25),640,0)
            lanOv = self.lf.draw(out,l,r,self.tr)
            overlay(img,cv2.resize(lanOv,(0,0),fx=0.25,fy=0.25),960,0)
            img = cv2.addWeighted(img, 1, lanOv, 0.3, 0)
        else:
            print("Lane find was none")

        overlay(img,cv2.resize(limg,(0,0),fx=0.25,fy=0.25),0,0)
        bwrgb = cv2.cvtColor(bw,cv2.COLOR_GRAY2RGB)
        overlay(img,cv2.resize(bwrgb,(0,0),fx=0.25,fy=0.25),320,0)
        return img   


def overlay(l_img,s_img,x_offset,y_offset) :
    l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img