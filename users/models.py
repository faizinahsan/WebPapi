from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    kontak = models.CharField(max_length=13)
    email = models.EmailField(unique= True, null=True)
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return f'{self.pk, self.email}'
class Dosen(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    nip = models.IntegerField(blank=True, null=True)
    bidang = models.ForeignKey('papi.KategoriPKM',on_delete=models.CASCADE,default=1)
    fakultas = models.ForeignKey('Fakultas',on_delete=models.CASCADE,default=1)
    def __str__(self):
        return f'{self.user}'
class Mahasiswa(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    npm = models.IntegerField(blank=True, null=True)
    fakultas = models.ForeignKey('Fakultas',on_delete=models.CASCADE,default=1)
    jurusan = models.ForeignKey('Jurusan',on_delete=models.CASCADE,default=1)
    # fakultas =models.IntegerField(blank=True, null=True)
    # jurusan = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return f'{self.user}'
class Fakultas(models.Model):
    namaFakultas = models.CharField(max_length=10,default="")
    def __str__(self):
        return f'{self.namaFakultas}'
class Jurusan(models.Model):
    namaJurusan = models.CharField(max_length=100,default="")
    idFakultas= models.ForeignKey("Fakultas",on_delete=models.CASCADE,default=0)
    def __str__(self):
        return f'{self.namaJurusan}'