from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from papi.models import ProposalPKM, Anggota, BidangPKM
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from users.models import Fakultas, Jurusan, Dosen, Mahasiswa
from bempapi.forms import InputDosenReviewer, FormatProposalPKMForm
from .models import FormatProposalPKM
User = get_user_model()
# Create your views here.


def akumulasi_pkm(request):
    pkm = ProposalPKM.objects.all()
    pkmNotRevisied = ProposalPKM.objects.filter(idStatus=1)
    pkmOnProgress = ProposalPKM.objects.filter(idStatus=2)
    pkmRevisied = ProposalPKM.objects.filter(idStatus=3)
    fakultas = []
    # Select * From Proposal where idProposal = 1 & Fakultas = Fmipa
    # Select * From Proposal where idStatus = 2
    # Select * From Proposal where idStatus = 3
    fmipa = ProposalPKM.objects.filter(idFakultas=1).count
    dataRevisi = {}
    for fak in Fakultas.objects.all():
        fakultas.append({
            'nama': fak.namaFakultas,
            'notRevisi': ProposalPKM.objects.filter(idFakultas=fak.pk, idStatus=1).count(),
            'onProgress': ProposalPKM.objects.filter(idFakultas=fak.pk, idStatus=2).count(),
            'revisi': ProposalPKM.objects.filter(idFakultas=fak.pk, idStatus=3).count(),
            'total': ProposalPKM.objects.filter(idFakultas=fak.pk).count(),
        })
    #    Mengsortir Fakultas berdasarkan Total
    fakultas = sorted(fakultas, key=(lambda i: i['revisi']), reverse=True)
    context = {
        'pkm': pkm,
        'notrevisied': pkmNotRevisied,
        'onprogress': pkmOnProgress,
        'revisied': pkmRevisied,
        'fakultas': fakultas,
        'fmipa': fmipa,
    }
    return render(request, 'bempapi/dashboard_pengurus.html', context)


def timeline_pkm(request):
    return render(request, 'bempapi/timeline_pkm.html')


def list_pkm(request):
    pkm = ProposalPKM.objects.all()
    context = {
        'pkm': pkm,
    }
    return render(request, 'bempapi/list_pkm_pengurus.html', context)


def list_pkm_withId(request, idStatus):
    pkm = ProposalPKM.objects.filter(idStatus=idStatus)
    context = {
        'pkm': pkm,
    }
    return render(request, 'bempapi/list_pkm_pengurus.html', context)


def manage_pkm(request):
    pkm = ProposalPKM.objects.filter(idDosenReviewer=2)
    context = {
        'pkms': pkm,
    }
    return render(request, 'bempapi/manage_dosen.html', context)


def manage_dosen(request, idPkm):
    pkm = get_object_or_404(ProposalPKM, pk=idPkm)
    dosens = Dosen.objects.filter(bidang=pkm.idKategori.pk)
    if request.method == 'POST':
        d_form = InputDosenReviewer(request.POST, instance=pkm)
        if d_form.is_valid():
            d_form.save()
            return redirect('list-pkm-pengurus')
    else:
        d_form = InputDosenReviewer()
    context = {
        'pkm': pkm,
        'form': d_form,
        'dosens': dosens,
    }
    return render(request, 'bempapi/manage_dosen_next.html', context)


def upload_format_pkm(request):
    formatProposal = FormatProposalPKM.objects.all()
    status = request.POST.get('status')
    path = request.POST.get('path')
    if status == 'download':
        return download(request, path)
    context = {
        'formatProposal': formatProposal
    }
    return render(request, 'bempapi/list_format_pengurus.html', context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + \
                os.path.basename(file_path)
            return response
    raise Http404


def upload_format_form(request):
    if request.method == 'POST':
        f_form = FormatProposalPKMForm(request.POST, request.FILES)
        if f_form.is_valid():
            f_form.save()
            return redirect('upload-format-pkm')
    else:
        f_form = FormatProposalPKMForm()
    context = {
        'f_form': f_form,
    }
    return render(request, 'bempapi/upload_format_form.html', context)
