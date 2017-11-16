import unittest
import calibrate
import gradient as uut
import cv2

IMG_DIR="test_images"
TEST_OUT="unit_test"

class TestCalibrate(unittest.TestCase):
    
    def test_01_loadImg(self):
        imgs = uut.loadImages(IMG_DIR)
        self.assertEqual(8,len(imgs))
        self.assertEqual((720,1280,3),imgs[0].shape)

    def test_02_abs_sobel_thresh(self):
        imgs = uut.loadImages(IMG_DIR)
        for i,img in enumerate(imgs):
            img = uut.abs_sobel_thresh(img,thresh_min=30,thresh_max=170,value=255)
            cv2.imwrite(TEST_OUT+"/sobel_"+str(i)+".png",img)

    def test_02_dir_threshold(self):
        imgs = uut.loadImages(IMG_DIR)
        for i,img in enumerate(imgs):
            img = uut.abs_sobel_thresh(img,thresh_min=30,thresh_max=170,value=255)
            cv2.imwrite(TEST_OUT+"/sobel_"+str(i)+"_dir.png",img)     

if __name__ == '__main__':
    unittest.main()