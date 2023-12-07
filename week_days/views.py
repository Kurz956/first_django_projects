from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def monday(request):
    return HttpResponse(f'<h1>Понедельник</h1>'
                        f'<li>Пресс качат</li>'
                        f'<li>Анжумания</li>'
                        f'<li>Бегат</li>')
def tuesday(request):
    return HttpResponse(f'<h1>Вторник</h1>'
                        f'<li>Питон учит</li>'
                        f'<li>Джанго читат</li>'
                        f'<li>Анжумания</li>')

def wensday(request):
    return HttpResponse(f'<h1>Среда</h1>'
                        f'пока пусто')
def thursday(request):
    return HttpResponse(f'<h1>Четверг</h1>'
                        f'пока пусто')
def friday(request):
    return HttpResponse(f'<h1>Пятница</h1>'
                        f'пока пусто')
def saturday(request):
    return HttpResponse(f'<h1>Суббота</h1>'
                        f'пока пусто')
def sunday(request):
    return HttpResponse(f'<h1>Воскресенье</h1>'
                        f'пока пусто')