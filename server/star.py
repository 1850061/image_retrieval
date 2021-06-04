import os
import matplotlib.image as mpimg
from tensorflow.python.platform import gfile

basePath = os.getcwd()


def getTagName(filename):
    fir = filename.split('\\')[-1]
    end = fir.split('/')[-1]
    return end


def add_star(imageStar):
    baseFile = 'static\\result'
    for filepath, dirnames, filenames in os.walk(baseFile):
        for filename in filenames:
            if getTagName(filename) == getTagName(imageStar):
                starBase = 'static/star'
                if not gfile.Exists(starBase):
                    os.mkdir(starBase)

                readFile = basePath + '\\' + os.path.join(filepath, filename)
                writeFile = basePath + '\\' + os.path.join(starBase, filename)
                print(writeFile)
                image = mpimg.imread(readFile)
                mpimg.imsave(writeFile, image)
    return True


def del_star(imageDel):
    baseFile = 'static\\star'
    for filepath, dirnames, filenames in os.walk(baseFile):
        for filename in filenames:
            if getTagName(filename) == getTagName(imageDel):
                starBase = 'static/star'
                if not gfile.Exists(starBase):
                    os.mkdir(starBase)

                delFile = basePath + '\\' + os.path.join(filepath, filename)
                print(delFile)
                os.remove(delFile)
    return True


def get_star_list():
    imageList = []
    baseFile = 'static\\star'
    for filepath, dirnames, filenames in os.walk(baseFile):
        for filename in filenames:
            imageList.append('star\\' + filename)
    return imageList
