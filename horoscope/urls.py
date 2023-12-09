from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index-name'),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name'),
    path('type/<str:element>', views.types_index, name='type-name'),
    path('type', views.type_of_sign, name='type-index'),


]
