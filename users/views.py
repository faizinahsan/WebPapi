from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, MahasiswaRegisForm, DosenRegisForm
from django.contrib import messages
from .models import Fakultas, Jurusan, Mahasiswa
from papi.models import KategoriPKM
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
# For Student


def register(request):
    fakultas = Fakultas.objects.all()
    jurusan = Jurusan.objects.all()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        m_form = MahasiswaRegisForm(request.POST)
        if form.is_valid() and m_form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            user.refresh_from_db()
            user.email = email
            try:
                user.mahasiswa.npm = m_form.cleaned_data.get('npm')
                user.mahasiswa.fakultas = m_form.cleaned_data.get('fakultas')
                user.mahasiswa.jurusan = m_form.cleaned_data.get('jurusan')
            except Mahasiswa.DoesNotExist:
                messages.success(
                    request, f'You Haven\'t agree with the terms!')
                return redirect('register')
            user.save()

            # form_user = form.save(commit=False)
            # form_user.is_student = True
            # form_user.save()
            # form = self.form_class( request.POST)
            # if form.is_valid():
            # new_formfile = form.save(commit=False)
            # new_formfile.is_activate = true
            # new_formfile.save()
            messages.success(request, f'Account created for {email}!')
            return redirect('index')
        else:
            print("Error di form")
    else:
        form = RegistrationForm()
        m_form = MahasiswaRegisForm()
    context = {
        'form': form,
        'm_form': m_form,
        'jurusan': jurusan,
        'fakultas': fakultas,
    }
    return render(request, 'users/register.html', context)


def register_dosen(request):
    fakultas = Fakultas.objects.all()
    bidang = KategoriPKM.objects.all()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        m_form = DosenRegisForm(request.POST)
        if form.is_valid() and m_form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            user.refresh_from_db()
            user.email = email
            user.dosen.nip = m_form.cleaned_data.get('nip')
            user.dosen.bidang = m_form.cleaned_data.get('bidang')
            user.dosen.fakultas = m_form.cleaned_data.get('fakultas')
            user.save()
            messages.success(request, f'Account created for {email}!')
            return redirect('index')
        else:
            print("Error di form")
    else:
        form = RegistrationForm()
        m_form = DosenRegisForm()
    context = {
        'form': form,
        'm_form': m_form,
        'fakultass': fakultas,
        'bidangs': bidang,
    }
    return render(request, 'users/registerdosen.html', context)


def profie_mahasiswa(request):
    return render(request, 'users/profil.html')
