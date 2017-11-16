import unittest
import perspective 
import distorter
import gradient
import numpy as np
import cv2

IMG_DIR="test_images"
TEST_OUT="unit_test"

srcCoord = np.float32([[597,450],[684,450],[325,650],[986,650]])
dstCoord = np.float32([[0,0],[660,0],[0,660],[660,660]])

srcCoord = np.float32([[0, 673], [1207, 673], [0, 450], [1280, 450]])
dstCoord = np.float32([[569, 223], [711, 223], [0, 0], [1280, 0]])



class TestCalibrate(unittest.TestCase):
    

 

    def test_dap(self):
        imgs = gradient.loadImages(IMG_DIR)
        ds = distorter.Distorter()
        tr = perspective.PerspectiveTrafo(srcCoord,dstCoord,(200,1280))
        for i,img in enumerate(imgs):
            img = ds.distortx(img)
            img = tr.warp(img)    
            img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
            cv2.imwrite(TEST_OUT+"/dap"+str(i)+".png",img)


        

if __name__ == '__main__':
    unittest.main()