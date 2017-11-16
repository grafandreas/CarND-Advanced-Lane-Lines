import unittest
import calibrate as uut
import cv2
import pickle
import distorter

CAMERA_CAL="camera_cal"
TEST_OUT="unit_test"

class TestCalibrate(unittest.TestCase):
    


    def test_01_distort(self):
        imgs = uut.loadImages(CAMERA_CAL)
        dstrtr = distorter.Distorter()
        for i,img in enumerate(imgs):
            dimg = dstrtr.distortx(img)
            cv2.imwrite(TEST_OUT+"/"+str(i)+"dc.png",dimg)

if __name__ == '__main__':
    unittest.main()