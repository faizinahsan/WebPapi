from django.shortcuts import render,redirect,get_object_or_404
from papi.models import ProposalPKM
from .forms import DownloadForm,UploadRevisiForm,LogDownloadForm
from users.models import Dosen
import os
from django.conf import settings
from django.http import HttpResponse, Http404
# Create your views here.
def dashboard_dosen(request):
    dosen = Dosen.objects.get(user=request.user)
    pkms = ProposalPKM.objects.filter(idDosenReviewer=dosen)
    notrevisied= ProposalPKM.objects.filter(idStatus=1,idDosenReviewer=dosen)
    revisied = ProposalPKM.objects.filter(idStatus=3,idDosenReviewer=dosen)
    context = {
        'pkms':pkms,
        'notrevisied':notrevisied,
        'revisied':revisied,
    }
    return render(request,'dosenpapi/dashboard_dosen.html',context)
def list_pkm_dosen(request,idStatus):
    dosen = Dosen.objects.get(user=request.user)
    pkms = ProposalPKM.objects.filter(idStatus=idStatus,idDosenReviewer=dosen) | ProposalPKM.objects.filter(idStatus=2,idDosenReviewer=dosen)
    if request.method == 'POST':
        status = request.POST.get('idStatus')
        path = request.POST.get('path')
        idPkm = request.POST.get('idPkm')
        pkm = get_object_or_404(ProposalPKM, pk=idPkm)
        d_form = DownloadForm(request.POST,instance=pkm)
        l_form = LogDownloadForm(request.POST)
        if d_form.is_valid():
            d_form.save()
            l_form.save()
            print(status,path,pkm)
            return download_pkm(request,path)
    else:
        d_form = DownloadForm()
    print(pkms)
    context = {
        'pkms':pkms,
        'form':d_form,
        'dosen':dosen,
        'idStatus':idStatus,
    }
    return render(request,'dosenpapi/list_pkm_dosen.html',context)
def download_pkm(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
def upload_revisi(request,idProposal):
    pkm = get_object_or_404(ProposalPKM, pk=idProposal)
    print(pkm)
    if request.method == 'POST':
        d_form = UploadRevisiForm(request.POST,request.FILES)
        # To Update idStatus Change
        p_form = DownloadForm(request.POST,instance=pkm)
        status = request.POST.get('idStatus')
        idKetua = request.POST.get('idKetua')
        print(request.user.dosen)
        if d_form.is_valid():
            dform = d_form.save(commit=False)
            dform.idDosenReviewer = request.user.dosen
            dform.save()
            p_form.save()
            return redirect('list-pkm-dosen',idStatus=3)
    else:
        d_form = UploadRevisiForm()
    context = {
        'pkm':pkm,
        'd_form':d_form
    }
    return render(request,'dosenpapi/upload_revisi.html',context)