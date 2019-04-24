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
class Dosen(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    nip = models.IntegerField(blank=True, null=True)
    bidang = models.IntegerField(blank=True, null=True)
class Mahasiswa(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    npm = models.IntegerField(blank=True, null=True)
    fakultas =models.IntegerField(blank=True, null=True)
    jurusan = models.IntegerField(blank=True, null=True)