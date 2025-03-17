import random
from django.shortcuts import render
from faker import Faker

# Create your views here.
def index(request): # request 인자 항상 들어옴
    return render(request, 'index.html') # render = 위에 불러온 함수, html을 랜더링해줌

def hello(request):

    my_name = 'hyojin'
    # 변하는 데이터를 만들 거기 때문에 변수화함
    context = {
        'my_name': my_name,
    }

    return render(request, 'hello.html', context)
    # = return render(request, 'hello.html', {'my_name': 'hyojin'})
    # 지금을 이름만 넣었지만 context가 더 많아지면 코드 치기 힘들기 때문에 쪼개서 작성할 것

def lunch(request):
    menu = ['떡볶이', '김밥', '우동', '샐러드', '파스타', '샤브샤브']
    pick = random.choice(menu)

    context = {
        'pick': pick,
    }
    return render(request, 'lunch.html', context)


def lotto(request):
    my_numbers = random.sample(range(1, 46), 6)
    # lucky_numbers = 'https://dhlottery.co.kr/gameResult.do?method=byWin&wiselog=C_A_1_1'
    
    context = {
        'my_numbers': my_numbers,
    }
    return render(request, 'lotto.html', context)

def profile(request, username): # 받을 인자를 모두 기입
    context = {
        'username': username,
    }
    return render(request, 'profile.html', context)


def cube(request, number):
    result = number ** 3

    context = {
        'number': number,
        'result': result,
    }
    return render(request, 'cube.html', context)

def articles(request): # python faker = 가짜데이터를 생성해주는 라이브러리
    fake = Faker() # 라이브러리 인스턴스화
    fake_articles = [] # 빈 리스트

    for i in range(100):
        fake_articles.append(fake.text())

    context = {
        'fake_articles': fake_articles,
    }

    return render(request, 'articles.html', context)