from django.urls import path
from . import views

app_name='buku'

urlpatterns=[
    path('',views.buku,name='buku'),
]