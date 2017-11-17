import cv2
import glob

def loadImagesGray(path):
    image_list=[]
    for fn in glob.glob(path+"/*.jpg"):
        im = cv2.imread(fn)
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        image_list.append(gray)

    for fn in glob.glob(path+"/*.png"):
        im = cv2.imread(fn)
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        image_list.append(gray)

    return image_list

def loadImagesRGB(path):
    image_list=[]
    for fn in glob.glob(path+"/*.jpg"):
        im = cv2.imread(fn)
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
        image_list.append(gray)

    for fn in glob.glob(path+"/*.png"):
        im = cv2.imread(fn)
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
        image_list.append(gray)

    return image_list

def saveRGB(img,path) :
    img =  cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    cv2.imwrite(path,img)

def saveGray(img,path) :
    img =  cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    cv2.imwrite(path,img)