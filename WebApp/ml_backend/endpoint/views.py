
from django.shortcuts import render
from .models import Director, Producer, Narrative, Hero, Actor, Song

import tensorflow as tf
from tensorflow import keras
import numpy as np

# Create your views here.

def home(request) :
    context = { 
        'directors' : Director.objects.all(),
        'producers' : Producer.objects.all(),
        'narratives' : Narrative.objects.all(),
        'heroes' : Hero.objects.all(),
        'actors' : Actor.objects.all(),
        'songs' : Song.objects.all()
    }
    return render(request,'index.html',context)

def result(request) :
    
    director = Director.objects.get(name=request.GET['director']).rating

    producer = Producer.objects.get(name=request.GET['producer']).rating
    
    narrative1 = Narrative.objects.get(name=request.GET['narrative1']).rating
    narrative2 = Narrative.objects.get(name=request.GET['narrative2']).rating
    narrative = (narrative1+narrative2)/2;
    
    hero1 = Hero.objects.get(name=request.GET['hero1']).rating
    hero2 = Hero.objects.get(name=request.GET['hero2']).rating
    hero3 = Hero.objects.get(name=request.GET['hero3']).rating
    hero = (hero1+hero2+hero3)/3;
    
    actor1 = Actor.objects.get(name=request.GET['actor1']).rating
    actor2 = Actor.objects.get(name=request.GET['actor2']).rating
    actor3 = Actor.objects.get(name=request.GET['actor3']).rating
    actor4 = Actor.objects.get(name=request.GET['actor4']).rating
    actor = (actor1+actor2+actor3+actor4)/4;

    song = Song.objects.get(name=request.GET['song']).rating

    model = tf.keras.models.load_model('C:/Users/ROWAN K BABY/Desktop/Movie Success Prediction/model')
    print(model.summary())

    data = [[director,producer,narrative,hero,actor,song]]
    data = np.array(data[:1])
    print(data)

    context = {
        'result' : int(model.predict(data)[0][0])
    }
    
    return render(request, 'result.html', context)
