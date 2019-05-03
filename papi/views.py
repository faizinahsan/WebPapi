from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import UploadPKMForm,AnggotaPKMForm,MultipleInputForm
from .models import ProposalPKM,Anggota,BidangPKM,KategoriPKM
from users.models import Fakultas
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
User = get_user_model()

def index(request):
    return render(request,'papi/index.html')
@login_required
def upload_pkm(request):
    bidang = BidangPKM.objects.all()
    kategori = KategoriPKM.objects.all()
    fakultas = Fakultas.objects.all()
    if request.method == 'POST':
        form = UploadPKMForm(request.POST,request.FILES)
        if form.is_valid():
            u_form = form.save(commit=False)
            u_form.idUsers = request.user
            u_form.save()
            return redirect('proposal-pkm',idPkm=u_form.pk)
    else:
        form = UploadPKMForm()
    context = {
        'u_form':form,
        'bidang':bidang,
        'kategori':kategori,
        'fakultas':fakultas,
    }
    return render(request,'papi/Dashboard_mhs.html',context)
@login_required
def input_anggota(request,idPkm):
    pkm = get_object_or_404(ProposalPKM, pk=idPkm)
    if request.method == 'POST':
        a_form = AnggotaPKMForm(request.POST)
        if a_form.is_valid():
            aform = a_form.save(commit=False)
            aform.idKetua = request.user
            aform.idPkm = pkm
            aform.save()
        return redirect('proposal-pkm',idPkm=pkm.pk)
    else:
        a_form = AnggotaPKMForm()
    return render(request,'papi/input_anggota.html',{'a_form':a_form,'pkm':pkm})
def coba_multiple_input(request):
    listAnggota = []
    for i in range (0,5):
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
    return render(request,'papi/coba_multiple_input.html',{'form':form,'list':listAnggota})
def proposal_pkm_page(request,idPkm):
    pkm = get_object_or_404(ProposalPKM, pk=idPkm)
    anggota = Anggota.objects.filter(idPkm = idPkm)
    total = anggota.count
    return render(request,'papi/proposal_page.html',{'pkm':pkm,'anggota':anggota,'total':total})