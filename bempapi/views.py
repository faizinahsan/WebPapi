from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from papi.models import ProposalPKM,Anggota,BidangPKM
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from users.models import Fakultas,Jurusan,Dosen,Mahasiswa
User = get_user_model()
# Create your views here.
def akumulasi_pkm(request):
    pkm = ProposalPKM.objects.all()
    pkmNotRevisied = ProposalPKM.objects.filter(idStatus = 1)
    pkmOnProgress = ProposalPKM.objects.filter(idStatus = 2)
    pkmRevisied = ProposalPKM.objects.filter(idStatus = 3)
    fakultas = []
    # Select * From Proposal where idProposal = 1 & Fakultas = Fmipa
    # Select * From Proposal where idStatus = 2
    # Select * From Proposal where idStatus = 3
    fmipa = ProposalPKM.objects.filter(idFakultas=1).count
    dataRevisi = {}
    for fak in Fakultas.objects.all():
        fakultas.append({
            'nama': fak.namaFakultas,
            'notRevisi':ProposalPKM.objects.filter(idFakultas=fak.pk,idStatus=1).count(),
            'onProgress':ProposalPKM.objects.filter(idFakultas=fak.pk,idStatus=2).count(),
            'revisi':ProposalPKM.objects.filter(idFakultas=fak.pk,idStatus=3).count(),
            'total': ProposalPKM.objects.filter(idFakultas=fak.pk).count(),
        })
    #    Mengsortir Fakultas berdasarkan Total
    fakultas = sorted(fakultas, key=(lambda i: i['revisi']),reverse=True)
    context = {
        'pkm':pkm,
        'notrevisied':pkmNotRevisied,
        'onprogress':pkmOnProgress,
        'revisied':pkmRevisied,
        'fakultas':fakultas,
        'fmipa':fmipa,
    }
    return render(request,'bempapi/dashboard_pengurus.html',context)
def timeline_pkm(request):
    return render(request,'bempapi/timeline_pkm.html')
def manage_pkm(request):
    pkm = ProposalPKM.objects.all()
    context = {
        'pkm':pkm,
    }
    return render(request,'bempapi/manage_pkm.html',context)