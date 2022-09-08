from tensorflow import keras
import numpy as np

class Fish(object) :
    def __init__(self):
        self.model = model

    def predict(self,img):
        return self.model.predict(np.expand_dims(img, axis=0))

from keras.models import load_model
model = load_model('fish_model.h5') 


from pathlib import Path
from tensorflow.keras.preprocessing.image  import load_img, img_to_array, ImageDataGenerator
import cv2
import numpy as np


if __name__ == '__main__' :
    class_col  = ['독가시치','미역치','쏠종개','쏨뱅이','쑤기미','돌상어','입실납자루',\
                  '좀수수치','퉁사리','흰수마자','가다랑어:','가숭어','갈치','고등어','농어']
    imgdir = "C:/Users/pyjwk/python/fish/config/file/picture/309.jpg"
    img = cv2.imread(imgdir)
    img.shape
    img1 = cv2.resize(img, dsize=(112,112), interpolation=cv2.INTER_CUBIC)
    img1 = img1/255
    img1.shape
    model = load_model('C:/Users/pyjwk/python/fish/config/fish_model.h5') 
    image = img1.reshape((1,)+img1.shape)
    image.shape
    predictions = model.predict(image)
    print(predictions)
    maxno = np.argmax(predictions[0])
    maxno
    print(maxno,"물고기이름:",class_col[maxno])
