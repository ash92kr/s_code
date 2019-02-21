from django.shortcuts import render
from faker import Faker
import requests
import os
from .models import Job


# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')
    
def pastlife(request):
    name = request.GET.get('name')
    person = Job.objects.filter(name=name).first()
    # name이 db에 있는지 확인하고 1개의 인스턴스만 가져온다
    # person = Job.objects.get(name=name)
    # get은 없으면 error가 나지만, filter는 None을 반환한다

    # 있으면 원래 직업을 가져오고
    if person:
        pastjob = person.pastjob
    # 없으면 faker로 새로운 직업을 넣어 모델에 저장하고 가져온다
    else:
        faker = Faker('ko_kr')
        pastjob = faker.job()
        person = Job(name=name, pastjob=pastjob)  # person에 입력하고 만든 데이터를 넣기
        person.save()
        
    
    GIPHY_KEY = os.getenv("GIPHY_KEY")
    
    url = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_KEY}&q={pastjob}&limit=1&lang=ko'
    data = requests.get(url).json()   # 이거 기억할 것 - 데이터를 json으로 받아오기
    image = data.get('data')[0].get('images').get('original').get('url')   # 키 = .get('키 이름')
    
    return render(request, 'jobs/pastlife.html', {'person': person, 'image': image})
    
    
