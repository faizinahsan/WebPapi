from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model() 

# Create your models here.
class ProposalPKM(models.Model):
    judul = models.CharField(max_length =50)
    namaKetua = models.CharField(max_length=50)
    deskripsi = models.TextField(default = '')
    document = models.FileField(upload_to='proposal',default = 'ProposalDefault.txt')
    idUsers = models.ForeignKey(User, on_delete=models.CASCADE)
    idKategori = models.ForeignKey('KategoriPKM',on_delete=models.CASCADE,default=0)
    idBidang = models.ForeignKey('BidangPKM',on_delete=models.CASCADE,default=0)
    idStatus = models.ForeignKey('StatusRevisi',on_delete=models.CASCADE,default=0)
    def __str__(self):
        return f'{self.pk}'
class KategoriPKM(models.Model):
    namaKategori = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.namaKategori}'
class BidangPKM(models.Model):
    namaBidang = models.CharField(max_length=50)
    jumlahAnggota = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return f'{self.namaBidang}'
class StatusRevisi(models.Model):
    namaStatus = models.CharField(max_length = 50)
    def __str__(self):
        return f'{self.namaStatus}'
class Anggota(models.Model):
    namaAnggota= models.CharField(max_length=20)
    npmAnggota = models.CharField(max_length=13,default="")
    emailAnggota = models.EmailField(null=True)
    idKetua = models.ForeignKey(User,on_delete=models.CASCADE,null =True)
    idPkm = models.ForeignKey('ProposalPKM',on_delete=models.CASCADE,null =True)
    def __str__(self):
        return f'{self.namaAnggota}'
class LogHistoryPKM(models.Model):
    tanggal = models.DateTimeField(default=timezone.now)
    linkRevisi = models.CharField(max_length=100)
    idStatus = models.ForeignKey('StatusRevisi',on_delete=models.CASCADE,null =True)
    idKetua = models.ForeignKey(User,on_delete=models.CASCADE,null =True)

class CobaMultipleInput(models.Model):
    namaInput = models.CharField(max_length = 20)
    emailInput = models.EmailField(null = True)
    def __str__(self):
        return f'{self.namaInput}'