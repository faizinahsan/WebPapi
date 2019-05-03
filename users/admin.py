from django.contrib import admin
from .models import User,Mahasiswa,Dosen,Fakultas,Jurusan
# Register your models here.
admin.site.register(User)
admin.site.register(Mahasiswa)
admin.site.register(Dosen)
admin.site.register(Fakultas)
admin.site.register(Jurusan)