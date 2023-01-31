from django.contrib import admin
from django.urls import path,include
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.index, name='home'),
    path('buku/', include('buku.urls')),
]
