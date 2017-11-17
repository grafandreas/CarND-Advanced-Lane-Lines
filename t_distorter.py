import unittest
import calibrate as uut
import cv2
import pickle
import distorter
import imageloader
CAMERA_CAL="camera_cal"
TEST_OUT="unit_test"

class TestCalibrate(unittest.TestCase):
    


    # def test_01_distort(self):
    #     imgs = uut.loadImages(CAMERA_CAL)
    #     dstrtr = distorter.Distorter()
    #     for i,img in enumerate(imgs):
    #         dimg = dstrtr.distortx(img)
    #         cv2.imwrite(TEST_OUT+"/distort"+str(i)+".png",dimg)

    def test_02_distort(self):
        imgs = imageloader.loadImagesRGB("test_images")
        dstrtr = distorter.Distorter()
        for i,img in enumerate(imgs):
            dimg = dstrtr.distortx(img)
            imageloader.saveRGB(dimg,TEST_OUT+"/distort"+str(i)+"dc.png")

if __name__ == '__main__':
    unittest.main()