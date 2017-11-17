import numpy as np 
import matplotlib.pyplot as plt 
import imageloader
import unittest
import lanefinder

IMG_DIR="unit_test/pipe_02_gradient"
TEST_OUT="unit_test/pipe_03_lanefinder"

class TestCalibrate(unittest.TestCase):

    def test_lanefinder(self):
        imgs = imageloader.loadImagesGray(IMG_DIR)
        for i,img in enumerate(imgs):
            lf = lanefinder.LaneFinder()
            (o,l,r) = lf.findLanes(img)
            imageloader.saveRGB(o,TEST_OUT+"/lane"+str(i)+".jpg")
            o = lf.findLanes(img)
            if(not o!= None):
                print("F")

if __name__ == '__main__':
    unittest.main()