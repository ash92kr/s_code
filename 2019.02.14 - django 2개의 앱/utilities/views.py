from django.shortcuts import render
from datetime import datetime
import requests
import os


# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')

def bye(request):
    result = datetime(2019, 2, 28) - datetime.now()
    return render(request, 'utilities/bye.html', {'result': result})
    
def graduation(request):
    farewell = datetime(2019, 5, 28) - datetime.now()
    return render(request, 'utilities/graduation.html', {'farewell': farewell})

def imagepick(request):
    return render(request, 'utilities/imagepick.html')
    
def today(request):
    weather_key = os.getenv("WEATHER_KEY")
    req = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=daejeon,kr&lang=kr&APPID={weather_key}')
    html = req.json()   # text는 인덱싱이 불가능하므로 json으로 바꿔야 한다
    weather = html["weather"][0]["description"]
    temp = html["main"]["temp"] - 273.15
    min_temp = html["main"]["temp_min"] - 273.15
    max_temp = html["main"]["temp_max"] - 273.15
    return render(request, 'utilities/today.html',
                {'weather': weather, 'temp': round(temp, 1),
                'min_temp': round(min_temp, 1),
                'max_temp': round(max_temp, 1)
                })


def ascii_new(request):
    return render(request, 'utilities/ascii_new.html')

def ascii_make(request):
    text = request.POST.get('text')
    font = request.POST.get('font')
    url = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}').text
    return render(request, 'utilities/ascii_make.html',
                {'text': text, 'font': font, 'url': url})


def original(request):
    return render(request, 'utilities/original.html')

def translated(request):
    
    text = request.POST.get('data')
    
    naver_client_id = os.getenv("NAVER_KEY")
    naver_client_secret = os.getenv("NAVER_PWD")
    
    papago_url = "https://openapi.naver.com/v1/papago/n2mt"
    
    headers = {
        "X-Naver-Client-Id": naver_client_id,
        "X-Naver-Client-Secret": naver_client_secret
    }
    data = {
        "source": "ko",
        "target": "en",
        "text": text[4:]
    }
    
    papago_response = requests.post(papago_url, headers=headers, data=data).json()
    print(papago_response)
    reply_text = papago_response["message"]["result"]["translatedText"]
    
    return render(request, 'utilities/translated.html', {'reply_text': reply_text})
