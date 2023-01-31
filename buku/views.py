from django.shortcuts import render
from . import models


def buku(request):
    data_buku = models.buku.objects.all()
    context = {
        'halaman': 'list buku',
        'data': data_buku,
    }
    print(data_buku)
    return render(request, 'buku.html', context)
