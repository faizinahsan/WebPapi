from django import forms
# from .models import Registration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Mahasiswa,Dosen

User = get_user_model()
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    is_student = forms.BooleanField(initial = False,required=False)
    is_teacher = forms.BooleanField(initial = False,required=False)
    # npm = forms.IntegerField()
    # fakultas = forms.IntegerField()
    # jurusan = forms.IntegerField()
    class Meta:
       model = User
       fields=('username', 'first_name','last_name','kontak' ,'email','password1','password2','is_student','is_teacher','kontak')
    #    fields=('username','email','password1','password2','is_student','is_teacher','npm','fakultas','jurusan')
    # def save(self,commit = True):
    #     user = super(RegistrationForm,self).save(commit = False)
    #     user.email = self.cleaned_data['email']
    #     user.mahasiswa.npm = self.cleaned_data['npm']
    #     user.mahasiswa.fakultas = self.cleaned_data['npm']
    #     user.mahasiswa.jurusan = self.cleaned_data['npm']

    #     if commit:
    #         user.save() 
class MahasiswaRegisForm(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = ('npm','fakultas','jurusan')
class DosenRegisForm(forms.ModelForm):
    class Meta:
        model = Dosen
        fields=('nip','bidang')