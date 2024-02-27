from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
author = {"Имя": "Евгений",
    "Отчество": "Владимирович",
    "Фамилия": "Кислов",
    "телефон": "8-925-676-35-41",
    "email": "e.kislow32@yandex.ru"
}
def home(request):
    text = '''<h1>Изучаем django</h1>
        <strong>Автор</strong>: <i>Кислов Е.В.</i>
        '''
    return HttpResponse(text)

def about(request):
    text = f'''
    Имя: <b>{author['Имя']}</b><br>
    Отчество: <b>{author['Отчество']}</b><br>
    Фамилия: <b>{author['Фамилия']}</b><br>
    Телефон: <b>{author['телефон']}</b><br>
    email: <b>{author['email']}</b>
    '''


    return HttpResponse(text)

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

def item(request):
   id = f'''



   '''


    

    return HttpResponseRedirect(reverse(new_id, args=id,))