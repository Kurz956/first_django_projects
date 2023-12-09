from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
signs = {
    'aries': ['Fire', "♈", '1', "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
              [i for i in range(80,111)]],
    'taurus': ['Earth', "♉", '2', "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
               [i for i in range(111,141)]],
    'gemini': ['Air', "♊", '3', "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
               [i for i in range(141,172)]],
    'cancer': ['Water', "♋", '4', "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
               [i for i in range(172,202)]],
    'leo': ['Fire', "♌", '5', "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
            [i for i in range(202,234)]],
    'virgo': ['Earth', "♍", '6', "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
              [i for i in range(234,267)]],
    'libra': ['Air', "♎", '7', "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
              [i for i in range(267,297)]],
    'scorpio': ['Water', "♏", '8', "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
                [i for i in range(297,324)]],
    'sagittarius': ['Fire', "♐", '9', "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
                    [i for i in range(324, 357)]],
    'capricorn': ['Earth', "♑", '10', "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
                  [i for i in range(357,366)] + [i for i in range(1,21)]],
    'aquarius': ['Air', "♒", '11', "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
                 [i for i in range(21,51)]],
    'pisces': ['Water', "♓", '12', "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).",
               [i for i in range(51,80)]],
}

class Sign:
    def __init__(self, name:str, type:str, picture:str, description:str, index:str, date:list):
        self._name = name
        self._type = type
        self._picture = picture
        self._description = description
        self._index = index
        self._date = date
    def __repr__(self):
        return str(self._name)
    def get_sign(self):
        return self.__dict__


zodiac_signs = {}
for sign, desc in signs.items():
    zodiac_signs[sign] = Sign(name=sign, type=desc[0], picture=desc[1], index=desc[2], description=desc[3], date=desc[4])
def home_page():
    '''Возврат на список элементов'''
    home_page = reverse('index-name')
    horoscope_home = f'<br><br><b><a href=\'{home_page}\'>На главную</a></b>'
    return horoscope_home
def element_page():
    '''Возврат на список стихий'''
    element_page = reverse('type-index')
    element_home = f'<br><br><b><a href=\'{element_page}\'>К стихиям</a></b>'
    return element_home

def type_of_sign(request):
    '''Стихии'''
    types = sorted({type._type for type in zodiac_signs.values()})
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
def index(request):
    '''Главная страница со списком всех знаком зодиака'''
    zodiacs = list(zodiac_signs.keys())
    response = '<ol>'
    for sign in zodiacs:
        redirect_path = reverse('horoscope-name', args=(sign,))
        response += f'<li><a href=\'{redirect_path}\'>{sign.title()}</a></li>'
    response += '</ol>'
    return HttpResponse(response + element_page())
def types_index(request, element):
    '''Переход со стихий на знаки'''
    zodiacs = list(zodiac_signs.keys())
    response = '<ol>'
    for sign in zodiacs:
        redirect_path = reverse('horoscope-name', args=(sign, ))
        if zodiac_signs[sign]._type == element:
            response += f'<li><a href=\'{redirect_path}\'>{sign.title()}</a></li>'
    response += '</ol>'
    return HttpResponse(response + element_page() + home_page())

def get_info_about_sign_zodiac_by_number(request, sign_zodiac:int): # работает через классы
    '''Получение знака зодиака по числу'''
    if  not 0 < sign_zodiac < len(zodiac_signs) + 1: # проверка входимости индекса в данные
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sign_zodiac}')
    for key, index in zodiac_signs.items(): # проверка значений, редирект на основную страницу, с нужным индексом
        if index._index == str(sign_zodiac):
            redirect_url = reverse('horoscope-name', args=(key, ))
            return redirect(redirect_url)
def get_info_about_sign_zodiac_by_number_old(request, sign_zodiac:int): # старая версия, оставил для наглядности сравнения
    '''Получение знака зодиака по числу'''
    zodiacs = list(signs.keys())
    if  not 0 < sign_zodiac < len(zodiacs) + 1:
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac, ))
    return redirect(redirect_url)
def get_info_about_sign_zodiac(request, sign_zodiac:str):  # работает через классы
    '''Получение знака зодиака по строке'''
    try:
        return HttpResponse(zodiac_signs[sign_zodiac]._description + element_page() + home_page())
        #return HttpResponse(' '.join(signs[sign_zodiac]) + horoscope_home) # версия без классов OLD
    except KeyError:
        return HttpResponseNotFound(f'Неизвестный знак зодиака - {sign_zodiac}')

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
                for key, value in zodiac_signs.items(): # находим в каком знаке этот день
                    if day_to_return in value._date: # редиректим на нужный знак
                        redirect_url = reverse('horoscope-name', args=(key,))
                        return redirect(f'{redirect_url}')
            day_to_return += value
