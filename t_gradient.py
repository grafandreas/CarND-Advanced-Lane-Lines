import unittest
import calibrate
import gradient as uut
import imageloader
import cv2

IMG_DIR="unit_test/pipe_01_dap"
TEST_OUT="unit_test/pipe_02_gradient"

class TestCalibrate(unittest.TestCase):
    


    def test_02_abs_sobel_thresh(self):
        imgs = imageloader.loadImagesRGB(IMG_DIR)
        for i,img in enumerate(imgs):
            img = uut.abs_sobel_thresh(img,thresh_min=30,thresh_max=170,value=255)
            imageloader.saveGray(img,TEST_OUT+"/sobel_"+str(i)+".png")

    def test_02_dir_threshold(self):
        imgs = imageloader.loadImagesRGB(IMG_DIR)
        for i,img in enumerate(imgs):
            img = uut.abs_sobel_thresh(img,thresh_min=30,thresh_max=170,value=255)
            imageloader.saveGray(img,TEST_OUT+"/sobel_"+str(i)+"_dir.png")     

if __name__ == '__main__':
    unittest.main()