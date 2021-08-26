from django.urls import path
from . import views
urlpatterns=[
    path('',views.del_index),
    path('delupdate',views.delupdate),
    path('delsearch',views.delsearch)
]