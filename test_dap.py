import unittest
import perspective 
import distorter
import imageloader
import numpy as np
import cv2

IMG_DIR="test_images"
TEST_OUT="unit_test/pipe_01_dap"

srcCoord = np.float32([[597,450],[684,450],[325,650],[986,650]])
dstCoord = np.float32([[0,0],[660,0],[0,660],[660,660]])

srcCoord = np.float32([[0, 673], [1207, 673], [0, 450], [1280, 450]])
dstCoord = np.float32([[569, 223], [711, 223], [0, 0], [1280, 0]])

srcCoord = np.float32(
    [[120, 720],
        [550, 470],
        [700, 470],
        [1160, 720]])

dstCoord = np.float32(
    [[200,720],
        [200,0],
        [1080,0],
        [1080,720]])

class TestCalibrate(unittest.TestCase):
    

 

    def test_dap(self):
        imgs = imageloader.loadImagesRGB(IMG_DIR)
        ds = distorter.Distorter()
        tr = perspective.PerspectiveTrafo(srcCoord,dstCoord,(1280,640))
        for i,img in enumerate(imgs):
            img = ds.distortx(img)
            img = tr.warp(img)    
            imageloader.saveRGB(img,TEST_OUT+"/dap"+str(i)+".jpg")


        

if __name__ == '__main__':
    unittest.main()