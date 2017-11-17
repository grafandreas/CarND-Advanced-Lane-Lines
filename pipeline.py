import perspective
import distorter
import lanefinder
import gradient

class Pipeline:
    def __init__(self) :
        self.ds = distorter.Distorter()
        self.tr = perspective.PerspectiveTrafo(perspective.PerspectiveTrafo.DEFAULT_SRC,perspective.PerspectiveTrafo.DEFAULT_DST,(1280,640))
        self.lf = lanefinder.LaneFinder()

    def process(self,img) :
        img = self.ds.distortx(img)
        img = self.tr.warp(img) 
        bw = gradient.abs_sobel_thresh(img,thresh_min=30,thresh_max=170,value=255)
        (out,l,r) = self.lf.findLanes(bw)

        return img   