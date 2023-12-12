from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from dataclasses import dataclass
from . import signs_descriptions
# Create your views here.


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали число из 4 числе - {sign_zodiac}')
def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали число вещественное число - {sign_zodiac}')
def get_my_date_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали дату - {sign_zodiac}')
def split_converters(reques, text):
    return HttpResponse(f'текст разбит - {text}')

def home_page():
    '''Возврат на список элементов'''
    home_page = reverse('horoscope-index')
    horoscope_home = f'<br><br><b><a href=\'{home_page}\'>На главную</a></b>'
    return horoscope_home
def element_page():
    '''Возврат на список стихий'''
    element_page = reverse('type-index')
    element_home = f'<br><br><b><a href=\'{element_page}\'>К стихиям</a></b>'
    return element_home

def type_of_sign(request):
    '''Стихии'''
    types = sorted({type._type for type in signs_descriptions.zodiac_signs.values()})
    list_element = ''
    for element in types:
        redirect_path = reverse('type-name', args=(element,))
        list_element += f'<li><a href="{redirect_path}">{element.title()}</a></li>'
    response = f'''
                <ul>
                {list_element}
                </ul>
                '''
    return HttpResponse(response + home_page())
def index(request): # после цикла ФОР в шаблоне хтмл
    '''Главная страница со списком всех знаком зодиака'''
    zodiacs = list(signs_descriptions.zodiac_signs.keys())
    # f'<li><a href=\'{redirect_path}\'>{sign.title()}</a></li>'
    context = {
        'zodiacs' : zodiacs,
        'zodiac_signs': signs_descriptions.zodiac_signs
    }
    return render(request, 'horoscope/index.html', context=context)
# def index_old(request): # до цикла ФОР в шаблоне хтмл - оставил для наглядности
#     '''Главная страница со списком всех знаком зодиака'''
#     zodiacs = list(zodiac_signs.keys())
#     response = '<ol>'
#     for sign in zodiacs:
#         redirect_path = reverse('horoscope-name', args=(sign,))
#         response += f'<li><a href=\'{redirect_path}\'>{sign.title()}</a></li>'
#     response += '</ol>'
#     return HttpResponse(response + element_page())
def types_index(request, element):
    '''Переход со стихий на знаки'''
    zodiacs = list(signs_descriptions.zodiac_signs.keys())
    response = '<ol>'
    for sign in zodiacs:
        redirect_path = reverse('horoscope-name', args=(sign, ))
        if signs_descriptions.zodiac_signs[sign]._type == element:
            response += f'<li><a href=\'{redirect_path}\'>{sign.title()}</a></li>'
    response += '</ol>'
    return HttpResponse(response + element_page() + home_page())

def get_info_about_sign_zodiac_by_number(request, sign_zodiac:int): # работает через классы
    '''Получение знака зодиака по числу'''
    if  not 0 < sign_zodiac < len(signs_descriptions.zodiac_signs) + 1: # проверка входимости индекса в данные
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sign_zodiac}')
    for key, index in signs_descriptions.zodiac_signs.items(): # проверка значений, редирект на основную страницу, с нужным индексом
        if index._index == str(sign_zodiac):
            redirect_url = reverse('horoscope-name', args=(key, ))
            return redirect(redirect_url)
def get_info_about_sign_zodiac_by_number_old(request, sign_zodiac:int): # старая версия, оставил для наглядности сравнения
    '''Получение знака зодиака по числу'''
    zodiacs = list(signs_descriptions.signs.keys())
    if  not 0 < sign_zodiac < len(zodiacs) + 1:
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac, ))
    return redirect(redirect_url)
def get_info_about_sign_zodiac(request, sign_zodiac:str):  # работает через классы
    '''Получение знака зодиака по строке'''
    #try:
        #response = render_to_string('horoscope/info_zodiac.html') # статический html шаблон
        #return HttpResponse(response)
        #return HttpResponse(zodiac_signs[sign_zodiac]._description + element_page() + home_page()) # вывод без html шаблона
        #return HttpResponse(' '.join(signs[sign_zodiac]) + horoscope_home) # версия без классов OLD
    # except KeyError:
    #    return HttpResponseNotFound(f'Неизвестный знак зодиака - {sign_zodiac}')
    # except AttributeError:
    #    return HttpResponseNotFound(f'Неизвестный знак зодиака - {sign_zodiac}')
    description = signs_descriptions.zodiac_signs.get(sign_zodiac)
    if description: #Если объекта класса зодиак нет по запрашиваемой переменной, присваивается NONE
        to_html_description_zodiac = description._description if description else None
        to_html_sign = description._name if description else None
    else:
        to_html_description_zodiac = None
        to_html_sign = sign_zodiac
    data = {
        'description_zodiac' : to_html_description_zodiac,
        'sign': to_html_sign,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)

def get_sign_by_date(request, month:int, day:int):
    '''Получение знака зодиака по его дате'''
    year = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if month not in year: # сверяем валидность даты
        return HttpResponseNotFound(f'Неверный месяц - {month}')
    if not 0 < day < year[month] + 1:
        return HttpResponseNotFound(f'Неверный день - {day}, для месяца - {month}')
    else:
        day_to_return = 0 # счётчик на принадлежность дня к знаку
        for key, value in year.items():
            if key == month:
                day_to_return += day # суммируем остаток месяца
                for key, value in signs_descriptions.zodiac_signs.items(): # находим в каком знаке этот день
                    if day_to_return in value._date: # редиректим на нужный знак
                        redirect_url = reverse('horoscope-name', args=(key,))
                        return redirect(f'{redirect_url}')
            day_to_return += value


@dataclass # для примера
class Person:
    name: str
    age: int
    def __str__(self):
        return f'this is {self.name}, he is {self.age} years old'
def help_desk(request): # пример, переменную можно и при построении рута сделать\
    '''Базовые возможности тут, пока не запомнишь'''
    description = signs_descriptions.zodiac_signs.get('aries')
    data = {
        'zodiac_signs': {},
        'sign': 'aries11',
        'description_zodiac' : description._description,
        'my_list': [1,2,3,4],
        'my_tuple': (1, 2, 3, 4, 5, 6),
        'my_dict': {'name': 'Jack', 'age': 40},
        'my_class': Person('Will', 55),
        'my_int': 1111,
        'my_float': 1.5,
        'value': [],
        'value1': 'qwerty',
        'lst_to_join': [1,2,3,4,5],
        'leo': "<b>Лев</b> - пятый <b>знак</b> зодиака, <i>сол</i>нце (с 23 июля по 21 августа).",
    }
    return render(request, 'horoscope/help.html', context=data)

