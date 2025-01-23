from django.shortcuts import render
import requests
import json



# Create your views here.

def home(request):

    if request.GET.get('q',False):
        city = request.GET.get('q')
        key = '02f9f2351e2023f47891742800aa573f'
        URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'
        try:
            data = requests.get(url=URL)
            weather = data.json()['name']
            main = data.json()['main']
            context={
                'weather':weather,
                'cel':main.get('temp'),
                'hum':main.get('humidity'),
                'air':main.get('pressure'),
            }
            return render(request,'home.html',context)
        except:
            return render(request,'home.html',{'error':'City not found!!'})

    return render(request,'home.html')
