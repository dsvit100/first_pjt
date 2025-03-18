"""
URL configuration for first_pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first_app import views
# first_app 폴더 내부의 views.py를 가지고 옴

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    # 경로설정하는 함수. '<기능명>' 생성, views의 index를 실행해줘
    path('hello/', views.hello),
    path('lunch/', views.lunch),
    path('lotto/', views.lotto),
    # variable routing
    path('profile/<username>/', views.profile), # <> 이 값에 어떤 것이 들어가든 모두 username으로 대응할게
    path('cube/<int:number>/', views.cube), # 장고식 해결방법 = number에 숫자 들어올 거니깐 int: 로 정수로 바꿔줌
    path('articles/', views.articles),

    # 입력값 받아오는 것
    path('ping/', views.ping),
    path('pong/', views.pong),
]
