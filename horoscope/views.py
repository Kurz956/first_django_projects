from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
signs = {
    'aries': ["♈", "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)."],
    'taurus': ["♉", "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)."],
    'gemini': ["♊", "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)."],
    'cancer': ["♋", "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)."],
    'leo': ["♌", "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)."],
    'virgo': ["♍", "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)."],
    'libra': ["♎", "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)."],
    'scorpio': ["♏", "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)."],
    'sagittarius': ["♐", "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)."],
    'capricorn': ["♑", "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января)."],
    'aquarius': ["♒", "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)."],
    'pisces': ["♓", "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."]
}
def index(request):
    zodiacs = list(signs.keys())
    response = '<ol>'
    for sign in zodiacs:
        redirect_path = reverse('horoscope-name', args=(sign,))
        response += f'<li><a href=\'{redirect_path}\'>{sign.title()}</a></li>'
    response += '</ol>'

    print(response)
    return HttpResponse(response)
def get_info_about_sign_zodiac_by_number(request, sign_zodiac:int):
    '''Получение знака зодиака по числу'''
    zodiacs = list(signs.keys())
    if  not 0 < sign_zodiac < len(zodiacs) + 1:
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac, ))
    return redirect(redirect_url)
def get_info_about_sign_zodiac(request, sign_zodiac:str):
    '''Получение знака зодиака по строке'''
    try:
        home_page = reverse('index-name')
        horoscope_home = f'<br><br><b><a href=\'{home_page}\'>На главную</a></b>'
        return HttpResponse(' '.join(signs[sign_zodiac]) + horoscope_home)
    except KeyError:
        return HttpResponseNotFound(f'Неизвестный знак зодиака - {sign_zodiac}')
