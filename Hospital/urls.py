from django.contrib import admin
from django.urls import path, include
from Hospital import views

urlpatterns =[
    path('', views.homepage, name='homepage'),
    path('login1/', views.login1, name='login1'),
    path('login1/patient/', views.patient, name='patient'),
    path('login1/doctor/', views.doctor, name='doctor'),
    path('login1/lab_tech', views.lab_tech, name='lab_tech'),
    path('login1/administrator/', views.administrator, name='administrator'),
    path('login1/administrator1/', views.administrator1, name='administrator1'),
    path('login1/administrator2/', views.administrator2, name='administrator2'),
    path('login1/administrator3/', views.administrator3, name='administrator3'),
    path('register/', views.register, name='register'),
    path('logreg/', views.logreg, name='logreg'),
    path('homepage/', views.homepage, name='homepage')

]