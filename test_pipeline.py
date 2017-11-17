import unittest
import perspective 
import distorter
import imageloader
import numpy as np
import cv2
import pipeline

IMG_DIR="test_images"
TEST_OUT="unit_test/pipeline"

class TestCalibrate(unittest.TestCase):

    def test_pipe(self) :
        p = pipeline.Pipeline()
        imgs = imageloader.loadImagesRGB(IMG_DIR)
        for i,img in enumerate(imgs):
            img = p.process(img)    
            imageloader.saveRGB(img,TEST_OUT+"/piped"+str(i)+"*.jpg")

if __name__ == '__main__':
    unittest.main()