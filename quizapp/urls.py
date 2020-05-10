from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show/', views.show, name='show'),
    path('create/', views.create, name='create'),
    path('quiz/', views.quiz, name='quiz'),
    path('result/', views.result, name='result'),


]