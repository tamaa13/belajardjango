from django.db import models


class buku(models.Model):
    kode_buku = models.CharField(max_length=100)
    judul_buku = models.CharField(max_length=100)
    penulis = models.CharField(max_length=100)
    penerbit = models.CharField(max_length=100)
    tahun_terbit = models.DateField()
    jumlah_buku = models.IntegerField()

    def __str__(self):
        return self.judul_buku
