import numpy as np 
import matplotlib.pyplot as plt 
import imageloader
import unittest

IMG_DIR="unit_test/pipe_02_gradient"
TEST_OUT="unit_test/pipe_02_gradient"

class TestCalibrate(unittest.TestCase):
    
    

 

    def test_histogram(self):
        imgs = imageloader.loadImagesGray(IMG_DIR)
        for i,img in enumerate(imgs):
            histogram = np.sum(img[img.shape[0]//2:,:], axis=0)
            fig = plt.plot(histogram)  
            plt.savefig(TEST_OUT+"/histo"+str(i)+".png")
            


        

if __name__ == '__main__':
    unittest.main()