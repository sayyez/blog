from lib2to3.pgen2 import grammar
from . import views
from django.urls import path




urlpatterns = [
    path('', views.index),
    path('group/<slug:slug>', views.group_posts)
    

]



