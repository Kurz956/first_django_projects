from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')
register_converter(converters.SplitConvertor, 'split')

urlpatterns = [
    path('', views.index, name='index-name'),

    path('<split>:text', views.split_converters),
    path('<my_date:sign_zodiac>/', views.get_my_date_converters),
    path('<yyyy:sign_zodiac>/', views.get_yyyy_converters),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<my_float:sign_zodiac>/', views.get_my_float_converters),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name'),
    path('<int:month>/<int:day>/', views.get_sign_by_date),
    path('type/<str:element>/', views.types_index, name='type-name'),
    path('type', views.type_of_sign, name='type-index'),


]
