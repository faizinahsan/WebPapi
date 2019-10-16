from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from users.models import Fakultas,Jurusan,Dosen
from papi.validators import validate_file_extension
User = get_user_model() 
# Mantap jiwa
# Create your models here.
class ProposalPKM(models.Model):
    judul = models.CharField(max_length =50)
    namaKetua = models.CharField(max_length=50)
    deskripsi = models.TextField(default = '')
    createdDate = models.DateTimeField(default=timezone.now)
    document = models.FileField(upload_to='proposal',default = 'ProposalDefault.txt',validators=[validate_file_extension])
    idUsers = models.ForeignKey(User, on_delete=models.CASCADE)
    idDosenReviewer = models.ForeignKey(Dosen,on_delete=models.CASCADE,default=1)
    idKategori = models.ForeignKey('KategoriPKM',on_delete=models.CASCADE,default=1)
    idBidang = models.ForeignKey('BidangPKM',on_delete=models.CASCADE,default=1)
    idStatus = models.ForeignKey('StatusRevisi',on_delete=models.CASCADE,default=1)
    idFakultas = models.ForeignKey(Fakultas,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return f'{self.pk,self.judul}'
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
    idKetua = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return f'{self.namaAnggota}'
class DosenPembimbing(models.Model):
    namaDosen= models.CharField(max_length=20)
    nipDosen = models.CharField(max_length=13,default="")
    emailDosen = models.EmailField(null=True)
    idKetua = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return f'{self.namaDosen}'
class LogHistoryPKM(models.Model):
    tanggal = models.DateTimeField(default=timezone.now)
    documentRevisi = models.FileField(upload_to='revisi',null=True,validators=[validate_file_extension])
    deskripsiLog = models.CharField(max_length=50,default="")
    idProposalPkm = models.ForeignKey('ProposalPKM',on_delete=models.CASCADE,null=True)
    idKetua = models.ForeignKey(User,on_delete=models.CASCADE,null =True)
    idDosenReviewer = models.ForeignKey(Dosen,on_delete=models.CASCADE,null=True)
class CobaMultipleInput(models.Model):
    namaInput = models.CharField(max_length = 20)
    emailInput = models.EmailField(null = True)
    def __str__(self):
        return f'{self.namaInput}'