from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
# Create your views here.
days = {
    'monday':[f'<h1>Понедельник</h1>'
              f'<li>Пресс качат</li>'
              f'<li>Анжумания</li>'
              f'<li>Бегит</li>'],

    'tuesday':[f'<h1>Вторник</h1>'
               f'<li>Питон учит</li>'
               f'<li>Джанго читат</li>'
               f'<li>Анжумания</li>'],

    'wednesday':[f'<h1>Среда</h1>'
                 f'пока пусто'],

    'thursday':[f'<h1>Четверг</h1>'
                f'пока пусто'],

    'friday':[f'<h1>Пятница</h1>'
              f'пока пусто'],

    'saturday':[f'<h1>Суббота</h1>'
                f'пока пусто'],

    'sunday':[f'<h1>Воскресенье</h1>'
              f'пока пусто']
}

def get_day_by_number(request, day:int):
    '''Получение конкретного дня'''
    if 0 < day < 8:
        day_to_response = list(days.keys())[day - 1]
        redirect_url = reverse('day-name', args=(day_to_response,))
        return redirect(redirect_url)
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {day}')

def get_day(request, day:str):
    '''Получение конкретного дня'''
    try:
        return HttpResponse(' '.join(days[day]))
    except KeyError:
        return HttpResponseNotFound(f'Не знаю такой день - {day}')
