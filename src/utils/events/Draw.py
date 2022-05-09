# utility for drawing things
import cv2
import dog
import os
from src.utils.DirUtils import DirUtils


def draw_img(imgpath, outputpath):
    img = cv2.imread(imgpath)

    # convert to gray
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # invert
    invert_img = cv2.bitwise_not(grey_img)

    # blur image
    blur_img = cv2.GaussianBlur(invert_img, (111, 111), 0)

    # inverted blur image
    invblur_img = cv2.bitwise_not(blur_img)

    # sketch
    sketch_img = cv2.divide(grey_img, invblur_img, scale=256.0)

    # write
    cv2.imwrite(outputpath, sketch_img)


def draw_dog(path='', filename='doggo'):
    du = DirUtils()
    dog_dir = 'temp_dog'
    dog.getDog(filename=os.path.join(du.get_media_dir(), dog_dir))
    temp_path = os.path.join(du.get_media_dir(), dog_dir + '.jpg')

    # check if output path exists
    print(os.path.join(path, filename + '.jpg'))
    while os.path.exists(os.path.join(path, filename + '.jpg')):
        filename += '_'

    draw_img(temp_path, os.path.join(path, filename + '.jpg'))
