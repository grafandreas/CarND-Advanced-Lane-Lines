import unittest
import videoprocess as uut
import numpy as np
import cv2
import pipeline
import cProfile
from pstats import Stats

IMG_DIR="challenge_video.mp4"
TEST_OUT="unit_test"

class TestVideo(unittest.TestCase):
    
 

    def setUp(self):
        """init each test"""
        self.pr = cProfile.Profile()
        self.pr.enable()
      

    def tearDown(self):
        """finish any test"""
        p = Stats (self.pr)
        p.strip_dirs()
        p.sort_stats ('cumtime')
        p.print_stats ()
       

    def test_pipe(self):
        p = pipeline.Pipeline()
        uut.process(IMG_DIR,TEST_OUT+"/L"+IMG_DIR,p.process,subC=(1,2))

    # def test_contrast1(self):
    #     p = pipeline.Pipeline()
    #     uut.process(IMG_DIR,TEST_OUT+"/C1"+IMG_DIR,p.process,subC=(21,24))

    # def test_contrast2(self):
    #     p = pipeline.Pipeline()
    #     uut.process(IMG_DIR,TEST_OUT+"/C2"+IMG_DIR,p.process,subC=(39,41))    

def cb(img) :
    return img    

    
if __name__ == '__main__':
    unittest.main()