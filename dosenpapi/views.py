from django.shortcuts import render,redirect,get_object_or_404
from papi.models import ProposalPKM
from .forms import DownloadForm
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
        if d_form.is_valid():
            d_form.save()
            print(status,path,pkm)
            return download_pkm(request,path)
    else:
        d_form = DownloadForm()
    print(pkms)
    context = {
        'pkms':pkms,
        'form':d_form,
        'dosen':dosen,
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
def upload_revisi(request):

    return redirect('list-pkm-dosen',idStatus=1)