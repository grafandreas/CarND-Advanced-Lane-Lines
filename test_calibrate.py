import unittest
import calibrate as uut
import cv2
import pickle
import distorter
import imageloader

CAMERA_CAL="camera_cal"
TEST_OUT="unit_test"

class TestCalibrate(unittest.TestCase):
    

    def test_01_load(self):
        imgs = imageloader.loadImagesRGB(CAMERA_CAL)
        self.assertEqual(20,len(imgs))
        print(imgs[0].shape)

    def itest_find(self):
        imgs = imageloader.loadImagesRGB(CAMERA_CAL)
        for i,img in enumerate(imgs):
            cv2.imwrite(TEST_OUT+"/"+str(i)+".png",img)
            ret, corners = uut.findCorner(img)
            if(ret) :
                img = cv2.drawChessboardCorners(img, (8,6), corners, ret)
                cv2.imwrite(TEST_OUT+"/"+str(i)+"c.png",img)

    def itest_02_calibrate(self):
        ret, mtx, dist, rvecs, tvecs = uut.calibrateFromDir(CAMERA_CAL)
        print(ret)
        print(mtx)
        print(dist)
        pickle.dump((mtx,dist),open(distorter.Distorter.FILE,"wb"))

    def test_03_distort(self):
        imgs = imageloader.loadImagesRGB(CAMERA_CAL)
        ret, mtx, dist, rvecs, tvecs = uut.calibrateFromDir(CAMERA_CAL)
        dstrtr = distorter.Distorter()
        for i,img in enumerate(imgs):
            dimg = cv2.undistort(img,mtx,dist)
            cv2.imwrite(TEST_OUT+"/"+str(i)+"d.png",dimg)
            dimg = dstrtr.distortx(img)
            cv2.imwrite(TEST_OUT+"/"+str(i)+"dc.png",dimg)

if __name__ == '__main__':
    unittest.main()