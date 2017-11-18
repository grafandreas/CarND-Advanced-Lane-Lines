import unittest
import videoprocess as uut
import numpy as np
import cv2
import pipeline

IMG_DIR="project_video.mp4"
TEST_OUT="unit_test"

class TestVideo(unittest.TestCase):
    
 

    def test_ident(self):
        uut.process(IMG_DIR,TEST_OUT+"/"+IMG_DIR,cb,subC=(3,6))

    def test_pipe(self):
        p = pipeline.Pipeline()
        uut.process(IMG_DIR,TEST_OUT+"/L"+IMG_DIR,p.process)#),subC=(0,5))

    def test_contrast1(self):
        p = pipeline.Pipeline()
        uut.process(IMG_DIR,TEST_OUT+"/C1"+IMG_DIR,p.process,subC=(21,24))

    def test_contrast2(self):
        p = pipeline.Pipeline()
        uut.process(IMG_DIR,TEST_OUT+"/C2"+IMG_DIR,p.process,subC=(39,41))    

def cb(img) :
    return img    

    
if __name__ == '__main__':
    unittest.main()