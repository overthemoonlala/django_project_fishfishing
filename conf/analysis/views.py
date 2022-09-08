from django.shortcuts import render
import numpy as np
import cv2
from pathlib import Path
from . import fish as fi
from tensorflow.keras.preprocessing.image  import load_img, img_to_array, ImageDataGenerator
from fishlist.models import Nomal, Poison, Extinct


# ▶ 사진업로드
def picture(request):
    if request.method != 'POST':
        return render(request,"analysis/pictureform.html")    
    else:
        fname = request.FILES['picture'].name
        handle_upload(request.FILES['picture'])
        return render(request, 'analysis/picture.html',{"fname":fname})
    
    
def handle_upload(f):
    with open("file/picture/" + f.name, 'wb+') as destination:
        for ch in f.chunks():
            destination.write(ch)
    
            
    
            
# ▶ 사진 분석 결과
def result(request) :
    class_col  = ['독가시치','미역치','쏠종개','쏨뱅이','쑤기미','돌상어','입실납자루',\
                  '좀수수치','퉁사리','흰수마자','가다랑어','가숭어','갈치','고등어','농어']
    fishimg = request.FILES['fish'].name
    handle_upload(request.FILES['fish'])

    file_dir = Path(__file__).resolve().parent.parent
    file_dir = str(file_dir).replace("\\","/")+"/file/picture/"
    imgdir = file_dir + fishimg
    img = cv2.imread(imgdir)
    img1 = cv2.resize(img, dsize=(112,112), interpolation=cv2.INTER_CUBIC)
    img1 = img1/255
    img1.shape
    model = fi.Fish()
#    image = img1.reshape((1,)+img1.shape)
#    predictions = model.predict(image)
    predictions = model.predict(img1)
    maxno = np.argmax(predictions[0])
#    return render(request, 'analysis/pictureform.html', {'fish': "결과:"+class_col[maxno],"fname":fishimg})



    plist = ['독가시치','미역치','쏠종개','쏨뱅이','쑤기미']
    elist = ['돌상어','입실납자루','좀수수치','퉁사리','흰수마자']
    
    if class_col[maxno] in plist:
        context = {'msg': "독성어류입니다. 먹거나 잡지마세요!!", 'url':'/analysis/pictureform/'}
 #       return render(request, 'alert.html', context)
    elif class_col[maxno] in elist:
        context = {'msg': "멸종위기어류입니다. 놓아주세요!!", 'url':'/analysis/pictureform/'}
#        return render(request, 'alert.html', context)
    else:
        context =  {'msg': "일반어류입니다. 잘 낚으셨네요!!", 'url':'/analysis/pictureform/'}
        

    return render(request, 'analysis/pictureform.html', {'fish': "결과:"+class_col[maxno],"fname":fishimg,"msg":context})











