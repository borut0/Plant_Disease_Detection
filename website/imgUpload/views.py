from django.shortcuts import render
from .models import Files
from pathlib import Path
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img,img_to_array
import numpy as np
import json

BASE_DIR = Path(__file__).resolve().parent.parent

#datagen_for_test = ImageDataGenerator(rescale = 1./255)
leaf_name = ['Apple','Corn','Peach','Cherry','Pepper','Potato','Grape','Strawberry']

def gime_label():
    label_path = 'label/label.json'
    label_file = open(label_path)
    label_file = json.loads(label_file.read())
    return list(label_file.keys())

def open_the_file(file_name):
    with open(os.path.join('cure_disease',file_name),'r') as f:
        return f.read() 

def handling_404(req,exception):
    return render(req,'404_page.html',{})

def home(req):
    background_images_list = []
    background_images_path = '/static/images'
    for i in os.listdir(os.path.join(BASE_DIR,'imgUpload','static','images')):
        background_images_list.append(os.path.join(background_images_path,i))
    leaf_name_nd_images = zip(background_images_list,leaf_name)
    return render(req, 'home.html',{'leaf_name_nd_images':leaf_name_nd_images})

def plant(req,pk):
    if not pk in leaf_name:
        return render(req,'404_page.html')
    if req.method == "POST":
        model_path = 'models/best_model.h5'
        img_path = 'media/file/'
        model = load_model(os.path.join(BASE_DIR,model_path))
        img_path = os.path.join(BASE_DIR,img_path)

        files = req.FILES.getlist('imgs')
        imgs =Files.objects.all()
        for i in os.listdir(img_path):
            os.remove(os.path.join(img_path,i))
        for i in imgs:
            i.delete()
        for img in files:
            if img.name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                new_file = Files(
                    imgs = img
                )
                new_file.save()
            else:
                return "not allowed"
                #return render(req,'index.html',{'display':'flex','pk':pk})
        imgs = Files.objects.all()
        acc = []
        label = []
        cure_list = []

        for img in imgs:
            uploaded_img = np.expand_dims(img_to_array(load_img(str(BASE_DIR)+img.imgs.url,target_size=(256,256))),axis=0)
            uploaded_img /= 255 
            prediction = model.predict(uploaded_img)
            acc.append(np.max(prediction*100))
            label_file = gime_label()
            predicted_label = label_file[np.argmax(prediction)]
            try:
                cure_list.append(open_the_file(predicted_label+'.txt'))
            except:
                cure_list.append('Healthy')
            label.append(predicted_label)
        all_data = zip(acc,label,imgs,cure_list)
        return render(req,'index.html',{'data':all_data,'pk':pk})
    else:
        return render(req, 'index.html',dict({'pk':pk}))
