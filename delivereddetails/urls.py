from django.urls import path
from . import  views
urlpatterns = [
    path('',views.deldetails_index),
    path('updatedeldetails',views.updatedeldetails),
    path('viewdeldetails',views.viewdeldetails)
]