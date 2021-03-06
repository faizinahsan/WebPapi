from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import UploadPKMForm, AnggotaPKMForm, MultipleInputForm, DosenPembimbingForm, LogHistoryUploadForm
from .models import ProposalPKM, Anggota, BidangPKM, KategoriPKM, DosenPembimbing, LogHistoryPKM
from users.models import Fakultas, Dosen
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from django.http import HttpResponse, Http404

from django.conf import settings  # correct way
base_dir = settings.MEDIA_ROOT

User = get_user_model()


def index(request):
    return render(request, 'papi/index.html')


@login_required
def upload_pkm(request):
    bidang = BidangPKM.objects.all()
    kategori = KategoriPKM.objects.all()
    fakultas = Fakultas.objects.all()
    if request.method == 'POST':
        form = UploadPKMForm(request.POST, request.FILES)
        l_form = LogHistoryUploadForm(request.POST)
        if form.is_valid():
            u_form = form.save(commit=False)
            u_form.idUsers = request.user
            u_form.save()
            return redirect('dashboard-mhs')
    else:
        form = UploadPKMForm()
    context = {
        'u_form': form,
        'bidang': bidang,
        'kategori': kategori,
        'fakultas': fakultas,
    }
    return render(request, 'papi/uploadDashboard_mhs.html', context)


def update_pkm(request, idUsers):
    # proposal = ProposalPKM.objects.filter(idUsers=idUsers).first
    proposal = get_object_or_404(ProposalPKM, idUsers=idUsers)
    bidang = BidangPKM.objects.all()
    kategori = KategoriPKM.objects.all()
    fakultas = Fakultas.objects.all()
    if request.method == 'POST':
        form = UploadPKMForm(request.POST, request.FILES, instance=proposal)
        # l_form = LogHistoryUploadForm(request.POST)
        if form.is_valid():
            u_form = form.save(commit=False)
            u_form.idUsers = request.user
            u_form.save()
            return redirect('dashboard-mhs')
    else:
        form = UploadPKMForm()
    context = {
        'u_form': form,
        'pkms': proposal,
        'idUsers': idUsers,
        'bidang': bidang,
        'kategori': kategori,
        'fakultas': fakultas,
    }
    return render(request, 'papi/updateDashboard_mhs.html', context)


@login_required
def input_anggota(request):
    if request.method == 'POST':
        a_form = AnggotaPKMForm(request.POST)
        if a_form.is_valid():
            aform = a_form.save(commit=False)
            aform.idKetua = request.user
            aform.save()
        return redirect('dashboard-mhs')
    else:
        a_form = AnggotaPKMForm()
    return render(request, 'papi/input_anggota.html', {'a_form': a_form})


@login_required
def list_anggota(request, idUser):
    anggotas = Anggota.objects.filter(idKetua=idUser)
    context = {
        'anggotas': anggotas
    }
    return render(request, 'papi/list_anggota.html', context)


@login_required
def update_anggota(request, idAnggota):
    anggota = get_object_or_404(Anggota, pk=idAnggota)
    if request.method == 'POST':
        a_form = AnggotaPKMForm(request.POST, instance=anggota)
        if a_form.is_valid():
            aform = a_form.save(commit=False)
            aform.idKetua = request.user
            aform.save()
        return redirect('dashboard-mhs')
    else:
        a_form = AnggotaPKMForm()
    return render(request, 'papi/update_anggota.html', {'a_form': a_form, 'anggota': anggota})

    pass


@login_required
def update_dosbim(request, idDosbim):
    dosbim = get_object_or_404(DosenPembimbing, pk=idDosbim)
    if request.method == 'POST':
        a_form = DosenPembimbingForm(request.POST, instance=dosbim)
        if a_form.is_valid():
            aform = a_form.save(commit=False)
            aform.idKetua = request.user
            aform.save()
        return redirect('dashboard-mhs')
    else:
        a_form = DosenPembimbingForm()
    return render(request, 'papi/update_dosbim.html', {'a_form': a_form, 'dosbim': dosbim})


@login_required
def view_dosbim(request, idUser):
    dosbims = DosenPembimbing.objects.filter(idKetua=idUser)
    context = {
        'dosbims': dosbims
    }
    return render(request, 'papi/view_dosbim.html', context)


def coba_multiple_input(request):
    listAnggota = []
    for i in range(0, 5):
        listAnggota.append(i)
    if request.method == 'POST':
        form = MultipleInputForm(request.POST)
        get_data = request.POST
        if form.is_valid():
            for i in get_data:
                form.save()
            # form.save()
        return redirect('index')
    else:
        form = MultipleInputForm()
    return render(request, 'papi/coba_multiple_input.html', {'form': form, 'list': listAnggota})


def proposal_pkm_page(request, idPkm):
    pkm = get_object_or_404(ProposalPKM, pk=idPkm)
    anggota = Anggota.objects.filter(idPkm=idPkm)
    total = anggota.count
    return render(request, 'papi/proposal_page.html', {'pkm': pkm, 'anggota': anggota, 'total': total})


def download_format_pkm(request):
    return render(request, 'papi/download_format.html')


def info_dosen(request):
    dosen = Dosen.objects.all()
    context = {
        'dosen': dosen,
    }
    return render(request, 'papi/info_dosen.html', context)


def log_file(request):
    p_user = request.user
    logHistory = LogHistoryPKM.objects.filter(idKetua=request.user)
    fileRevisi = LogHistoryPKM.objects.filter(
        idKetua=request.user).order_by('-tanggal').first()
    filePath = request.POST.get('filePath')
    print(fileRevisi)
    print("base dir:"+base_dir)
    if fileRevisi is None:
        pass
    else:
        print("WOW ADA")
        if fileRevisi.documentRevisi.name != "DefaultFile.docx":
            if filePath == fileRevisi.documentRevisi.path:
                path = fileRevisi.documentRevisi.path
                return download_revisi(request, path)
        else:
            pass
    proposal = ProposalPKM.objects.filter(idUsers=p_user).first()
    context = {
        'logHistory': logHistory,
        'proposal': proposal,
        'fileRevisi': fileRevisi,
    }
    return render(request, 'papi/file_log.html', context)


def download_revisi(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + \
                os.path.basename(file_path)
            return response
    raise Http404


def list_format(request):

    return render(request, 'papi/list_format.html')


def dashboard_mhs(request):
    pkms = ProposalPKM.objects.filter(
        idUsers=request.user).order_by('-createdDate').first()
    anggota = Anggota.objects.filter(idKetua=request.user)
    dospem = DosenPembimbing.objects.filter(idKetua=request.user).first()
    print(dospem)
    # print("Id:",pkms.pk,"Judul:",pkms.judul,"Jumlah Anggota:",anggota.count())
    context = {
        'pkms': pkms,
        'anggota': anggota,
        'dospem': dospem,
    }
    return render(request, 'papi/Dashboard_mhs.html', context)


def input_dospem(request):
    if request.method == 'POST':
        a_form = DosenPembimbingForm(request.POST)
        if a_form.is_valid():
            aform = a_form.save(commit=False)
            aform.idKetua = request.user
            aform.save()
        return redirect('dashboard-mhs')
    else:
        a_form = DosenPembimbingForm()
    return render(request, 'papi/input_dospem.html', {'aform:': a_form})


def timeline_mahasiswa(request):
    return render(request, 'papi/timeline.html')
