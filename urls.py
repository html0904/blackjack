from django.urls import path

from .views import HomePageView

urlpattern = [path('',HomePageView, name='home')