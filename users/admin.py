from django.contrib import admin
from .models import User,Mahasiswa,Dosen
# Register your models here.
admin.site.register(User)
admin.site.register(Mahasiswa)
admin.site.register(Dosen)