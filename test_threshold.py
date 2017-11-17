import unittest
import calibrate
import gradient 
import threshold as uut
import cv2

IMG_DIR="test_images"
TEST_OUT="unit_test"

class TestCalibrate(unittest.TestCase):
    


    def test_02_abs_sobel_thresh(self):
        imgs = uut.loadImagesHLS(IMG_DIR)
        for i,img in enumerate(imgs):
            img = uut.thresholdS(img,thresh=(160,255),value=255)
            cv2.imwrite(TEST_OUT+"/thresh_"+str(i)+".png",img)


if __name__ == '__main__':
    unittest.main()