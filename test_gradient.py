import unittest
import calibrate
import gradient as uut
import imageloader
import threshold
import cv2
import numpy as np

IMG_DIR="unit_test/pipe_01_dap"
TEST_OUT="unit_test/pipe_02_gradient"

class TestCalibrate(unittest.TestCase):
    
    def test_simple(self):
        imgs = imageloader.loadImagesRGB(IMG_DIR)
        for i,img in enumerate(imgs):
            imageloader.saveRGB(img,TEST_OUT+"/a_"+str(i)+".png")

    def test_02_abs_sobel_thresh(self):
        imgs = imageloader.loadImagesRGB(IMG_DIR)
        for i,img in enumerate(imgs):
            img = uut.abs_sobel_thresh(img,thresh_min=30,thresh_max=170,value=255)
            imageloader.saveGray(img,TEST_OUT+"/sobel_"+str(i)+".png")

    def test_02_dir_threshold(self):
        imgs = imageloader.loadImagesRGB(IMG_DIR)
        for i,img in enumerate(imgs):
            img = uut.dir_threshold(img)
            imageloader.saveGray(img,TEST_OUT+"/sobel_dir_"+str(i)+".png")    

    def test_02_hls_threshold(self):
        imgs = imageloader.loadImagesRGB(IMG_DIR)
        for i,img in enumerate(imgs):
            img = threshold.thresholdRGB(img,thresh=(180,255),value=255)
            imageloader.saveGray(img,TEST_OUT+"/thresh_"+str(i)+".png")     

    def test_02_hsv_yellow(self):
        imgs = imageloader.loadImagesRGB(IMG_DIR)
        for i,img in enumerate(imgs):
            img = threshold.thresholdYellow(img)
            imageloader.saveGray(img,TEST_OUT+"/yellow_"+str(i)+".png")   

    def test_02_zcombine(self):
        imgs = imageloader.loadImagesRGB(IMG_DIR)
        for i,img in enumerate(imgs):
            img1 = uut.abs_sobel_thresh(img,thresh_min=30,thresh_max=170,value=255)
            img2 = threshold.thresholdYellow(img)
            print("!")
            print(img1.shape)
            print(img2.shape)
            mimg = np.maximum(img1,img2)
            print(mimg.shape)
            imageloader.saveGray(mimg,TEST_OUT+"/zcombine_"+str(i)+".png")     

if __name__ == '__main__':
    unittest.main()