from django.contrib import admin
from django.urls import path,include
from . import views
from .views import speech
from .views import next_page
#from .views import process_input



urlpatterns = [
    path('', views.index),
    path('word/', views.word),
    path('voice/', views.voice),
    #path('', views.login),
    path('register/', views.register),
    path('speech/', speech, name='speech'),  #check result
    #path('voice/', process_input, name='process_input'),
    path('voice/', next_page, name='next_page_url'),
    #path('process_input/', process_input, name='process_input'),

]

