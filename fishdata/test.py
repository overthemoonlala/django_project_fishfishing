# -*- coding: utf-8 -*-

# 시작
import numpy as np
import pandas as pd
import tensorflow as tf
import glob as glob

all_data = np.array(glob.glob('./img/*/*.jpg',recursive=True))
len(all_data) # 총 사진수? 382
all_data[:5]


# all_data 정보를 csv 파일로 저장
def check_n(name):
    labels = np.zeros(15,)

   # name(물고기이름) 설정
    if(name == "독가시치"):
        labels[0] = 1
    elif(name == "미역치"):
        labels[1] = 1
    elif(name == "쏠종개"):
        labels[2] =1
    elif(name == "쏨뱅이"):
        labels[3] = 1
    elif(name == "쑤기미"):
        labels[4] = 1
    elif(name == "돌상어"):
        labels[5] = 1
    elif(name == "입실납자루"):
        labels[6] =1
    elif(name == "좀수수치"):
        labels[7] = 1
    elif(name == "퉁사리"):
        labels[8] = 1
    elif(name == "흰수마자"):
        labels[9] = 1
    elif(name == "가다랑어"):
        labels[10] = 1
    elif(name == "가숭어"):
        labels[11] = 1
    elif(name == "갈치"):
        labels[12] = 1
    elif(name == "고등어"):
        labels[13] = 1
    elif(name == "농어"):
        labels[14] = 1    
    return labels

# all_data.shape[0] : 행의수
fish_type = {"poison":["독가시치","미역치","쏠종개","쏨뱅이","쑤기미"],
             "extinct":["임실납자루","좀수수치","통사리","흰수마자","돌상어"]}

all_labels = np.empty((all_data.shape[0],15))
all_labels.shape  # (382, 15)
all_data[0] 

for i, data in enumerate(all_data):
    kind_and_name = all_data[i].split('\\')[1]
    name = kind_and_name  
    labels = check_n(name)
    all_labels[i] = labels;     

print(all_labels[10:20])               


# 훈련, 검증, 테스트 분리
# 훈련,테스트 분리
from sklearn.model_selection import train_test_split

train_x, test_x, train_y, test_y = train_test_split\
    (all_data, all_labels, shuffle = True, test_size =0.3, random_state=99)
train_x.shape # 결과: (267,)
test_x.shape # 결과:  (115,)

# 훈련, 검증 분리
train_x, val_x, train_y, val_y = train_test_split\
    (train_x, train_y, shuffle = True, test_size=0.3, random_state=99)
train_x.shape # 결과: (186,)
val_x.shape  # 결과: (81,)

# csv 파일 생성을 위한 DataFrame 객체 생성

train_df = pd.DataFrame(
    {'image':all_data, 
     '독가시치':all_labels[:,0], '미역치':all_labels[:,1], '쏠종개':all_labels[:,2],
     '쏨뱅이':all_labels[:,3], '쑤기미':all_labels[:,4], '돌상어':all_labels[:,5],
     '입실납자루':all_labels[:,6], '좀수수치':all_labels[:,7], '퉁사리':all_labels[:,8],
     '흰수마자':all_labels[:,9], '가다랑어:':all_labels[:,10], '가숭어':all_labels[:,11],
     '갈치':all_labels[:,12], '고등어':all_labels[:,13], '농어':all_labels[:,14]
     })
train_df.info()
train_df.head()
train_df = train_df.sample(frac=1)


val_df = pd.DataFrame(
    {'image':val_x,
     '독가시치':val_y[:,0], '미역치':val_y[:,1], '쏠종개':val_y[:,2],
     '쏨뱅이':val_y[:,3], '쑤기미':val_y[:,4], '돌상어':val_y[:,5],
     '입실납자루':val_y[:,6], '좀수수치':val_y[:,7], '퉁사리':val_y[:,8],
     '흰수마자':val_y[:,9], '가다랑어:':val_y[:,10], '가숭어':val_y[:,11],
     '갈치':val_y[:,12], '고등어':val_y[:,13], '농어':val_y[:,14]
     })
val_df.info()
val_df.head()

test_df = pd.DataFrame(
    {'image':test_x,
     '독가시치':test_y[:,0], '미역치':test_y[:,1], '쏠종개':test_y[:,2],
     '쏨뱅이':test_y[:,3], '쑤기미':test_y[:,4], '돌상어':test_y[:,5],
     '입실납자루':test_y[:,6], '좀수수치':test_y[:,7], '퉁사리':test_y[:,8],
     '흰수마자':test_y[:,9], '가다랑어:':test_y[:,10], '가숭어':test_y[:,11],
     '갈치':test_y[:,12], '고등어':test_y[:,13], '농어':test_y[:,14]
     })
test_df.info()
test_df.head()

train_df.to_csv('./img/train.csv', index=None)
val_df.to_csv('./img/val.csv', index=None)
test_df.to_csv('./img/test.csv', index=None)

train_df.head()
val_df.head()
test_df.head()

train_df.info()
val_df.info()
train_df.head()

# 저장된 csv 파일에서 읽어서 데이터 분석하기
import pandas as pd
train_df = pd.read_csv("./img/train.csv")
val_df = pd.read_csv("./img/val.csv")
test_df = pd.read_csv("./img/test.csv")


# 원본이미지 크기 출력하기 >> 이미지크기가 각각 다르다
import matplotlib.pyplot as plt
img1 = plt.imread(train_df["image"][0])
img1.shape # 결과: (125, 400, 3)
img2 = plt.imread(train_df["image"][31])
img2.shape # 결과: (332, 500, 3)

# 1. 분석을 위한 이미지 크기를 동일하게 설정
# 2. ...건의 이미지를 메모리에 로드하여 분석하기 어려움
# >> 이미지 제너레이터 방식 이용함
from tensorflow.keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)

# 모델 생성
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten,Conv2D, MaxPool2D, Dropout

model = Sequential([
    Conv2D(input_shape=(112,112,3), kernel_size=(3,3),
           filters=32, padding='same', activation='relu'),
    Conv2D(kernel_size=(3,3), filters=64, padding='same', activation='relu'),
    MaxPool2D(pool_size=(2,2)), # 특징맵을 반으로 줄임
    Dropout(rate=0.5),
    Conv2D(kernel_size=(3,3), filters=128, padding='same',activation='relu'),
    Conv2D(kernel_size=(3,3), filters=256, padding='valid', activation='relu'),
    MaxPool2D(pool_size=(2,2)),
    Dropout(rate=0.5),
    Flatten(), # 1차원형태의 배열로 변경, 평탄화층, 평탄화레이어
    Dense(units=512, activation='relu'),
    Dropout(rate=0.5),
    Dense(units=256, activation='relu'),
    Dropout(rate=0.5),
    Dense(units=15, activation='softmax')
    ])

model.summary()

model.compile(optimizer='adam', 
              loss='categorical_crossentropy', metrics = ['acc'])

class_col = list(train_df.columns[1:])
class_col

batch_size=32

# 1. 분석을 위한 이미지 크기를 동일하게 설정
# 2. 5578건의 이미지를 메모리에 로드하여 분석하기 어려움
# >> 이미지 제너레이터 방식 이용함
# DtataFrame에 설정된 데이터로 부터 훈련데이터를 설정
train_generator = train_datagen.flow_from_dataframe(
    dataframe=train_df, # dataFrame 객체 설정
    directory=None, # 폴더명, 여기에서는 image데이터에 포함, 설정안함
    x_col = 'image', # 이미지데이터, 분석데이터, image컬럼명
    y_col = class_col, # 레이블데이터, train_df컬럼명
    target_size = (112,112), # 생성될 이미지의 크기 설정
    color_mode='rgb', # 색상지정
    class_mode='raw', # 
    batch_size=batch_size,
    shuffle = True,
    seed=42
    )
# 결과 : Found 382 validated image filenames.

val_generator = val_datagen.flow_from_dataframe(
    dataframe=val_df,
    directory=None,
    x_col ='image',
    y_col = class_col,
    target_size = (112,112),
    color_mode='rgb',
    class_mode='raw',
    batch_size=batch_size,
    shuffle=True)
# 결과 : Found 81 validated image filenames.

def get_steps(num_samples, batch_size):
    if(num_samples % batch_size) > 0:
        return (num_samples // batch_size) + 1
    else:
        return num_samples // batch_size
    
history = model.fit(train_generator,
                    steps_per_epoch=get_steps(len(train_df), batch_size),
                    validation_data = val_generator,
                    validation_steps=get_steps(len(val_df), batch_size),
                    epochs = 100)



'''
import matplotlib.pyplot as plt
plt.rc("font",family="Malgun Gothic")
image = plt.imread(test_df["image"][0])
plt.imshow(image)
fish_type
plt.figure()
for i, pred in enumerate(do_preds):
    plt.subplot(2,4,i+1)
    prob = zip(class_col, list(pred))
    prob = sorted(list(prob), key=lambda z : z[1], reverse=True)[0]
    print("i=",i,prob)
    image = plt.imread(test_df["image"][i+off])
    plt.imshow(image)
    ftype=""
    if  prob[1][0] in  fish_type["poison"]: 
        ftype = "poison"
       
#    plt.title\
#        (f'{prob[0][0]}:{round(prob[0][1] * 100,2)} %\n {prob[1][0]}:{round(prob[1][1] * 100,2)}%\n{ftype}')
#    plt.tight_layout()
plt.show()
'''
# 테스트 데이터를 이용하여 예측하기
test_datagen = ImageDataGenerator(rescale = 1./255)
test_generator = test_datagen.flow_from_dataframe(
    dataframe = test_df,
    directory=None,
    x_col='image',
    y_col=None,
    target_size=(112,112), 
    color_mode='rgb',
    class_mode=None,
    batch_size=batch_size,
    shuffle=False
    )

# 예측하기
preds = model.predict(test_generator, steps =32)
preds.shape
preds[0]
off = 0
do_preds = preds[off:off+8]
do_preds
do_preds.shape

arg_results = np.argmax(do_preds,axis=-1)
arg_results
arg_results[1]

import matplotlib.pyplot as plt
plt.rc("font",family="Malgun Gothic")
plt.figure()
for i, pred in enumerate(arg_results):
    plt.subplot(2,4,i+1)
    prob = (class_col[pred], pred)
#    prob = sorted(list(prob), key=lambda z : z[1], reverse=True)[0]
    print("i=",i,prob)
    image = plt.imread(test_df["image"][i+off])
    plt.imshow(image)
    ftype=""
    if  prob[0] in  fish_type["poison"]: 
        ftype = "poison"
    elif  prob[0] in fish_type["extinct"]:
        ftype ="extinct"   
    elif prob[0]:
        ftype = "nomal"
    plt.title('Pred:%s\nlabel:%s\n%s' % \
              (class_col[prob[1]],class_col[np.argmax(test_y[i],axis=-1)],ftype),fontsize=10)
    #plt.tight_layout()
plt.show()



# 모델 저장하기
model.save('fish_model.h5')

# 저장된 파일로 실행------------------------------------------------------------
from keras.models import load_model
model = load_model('fish_model.h5')
model.summary()
import pandas as pd

train_df = pd.read_csv("./img/train.csv")
val_df = pd.read_csv("./img/val.csv")
test_df = pd.read_csv("./img/test.csv")
test_df.info()

from tensorflow.keras.preprocessing.image import ImageDataGenerator

class_col = list(train_df.columns[1:])
class_col
batch_size =32


test_datagen = ImageDataGenerator(rescale = 1./255)
test_generator = test_datagen.flow_from_dataframe(
    dataframe = test_df,
    directory = None,
    x_col = 'image',
    y_col = None,
    target_size = (112,112),
    color_mode ='rgb',
    class_mode = None,
    batch_size = batch_size,
    shuffle = False
    )

# 결과 : Found 81 validated image filenames.

# 예측하기
preds = model.predict(test_generator, steps = 32)
preds

preds.shape
preds[0]
off = 0
do_preds = preds[off:off+8]
do_preds.shape
import matplotlib.pyplot as plt
plt.rc("font",family="Malgun Gothic")
image = plt.imread(test_df["image"][0])
plt.imshow(image)

plt.figure()
for i, pred in enumerate(do_preds):
    plt.subplot(2,4,i+1)
    prob = zip(class_col, list(pred))
    prob = sorted(list(prob), key=lambda z : z[1], reverse=True)[:2]
    print("i=",i,prob)
    image = plt.imread(test_df["image"][i+off])
    plt.imshow(image)
    plt.title\
        (f'{prob[0][0]}:{round(prob[0][1] * 100,2)} %\n {prob[1][0]}:{round(prob[1][1] * 100,2)}%')
#    plt.tight_layout()
plt.show()