import unittest
import videoprocess as uut
import numpy as np
import cv2

IMG_DIR="project_video.mp4"
TEST_OUT="unit_test"

class TestCalibrate(unittest.TestCase):
    
 

    def test_ident(self):
        uut.process(IMG_DIR,TEST_OUT+"/"+IMG_DIR,cb,subC=(3,6))


def cb(img) :
    return img    

if __name__ == '__main__':
    unittest.main()