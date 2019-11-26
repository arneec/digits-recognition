"""v2.0 main.py for digits recognition

config: in config.py
change TEST_IMAGE in config.py to change image file to test.

>>> cd code
>>> python main.py"""

import os

from sklearn import datasets
from sklearn.svm import SVC
from skimage.io import imread
from skimage.exposure import rescale_intensity
from skimage.transform import resize

from config import IMAGE_DIR, TEST_IMAGE


if __name__ == '__main__':
    digits = datasets.load_digits()
    features, labels = digits.data, digits.target
    
    clf = SVC(gamma = 0.001)
    clf.fit(features, labels)

    img = resize(imread(os.path.join(IMAGE_DIR, TEST_IMAGE)), (8,8))
    img = rescale_intensity(img, out_range=(0, 16))

    x_test = [sum(pixel)/3.0 for row in img for pixel in row]
    print("The predicted digit is {}".format(clf.predict([x_test])))
