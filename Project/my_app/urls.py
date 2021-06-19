from django.contrib import admin
from django.urls import path
from my_app import views
urlpatterns = [
    path('',views.index,name='index'),
    path('ABOUT US',views.ABOUT,name='ABOUT'),
    path('CONTACT',views.CONTACT,name='CONTACT'),
    path('WASTAGES',views.WASTAGES,name='WASTAGES')
]
