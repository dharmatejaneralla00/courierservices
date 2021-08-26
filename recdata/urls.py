from django.urls import path
from . import  views

urlpatterns = [
    path('',views.index),
    path('index',views.index),
    path('addco',views.addco),
    path('search',views.search),
    path('display',views.display),
    path('docudel',views.docudel)
]