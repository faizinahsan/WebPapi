from django import forms
from papi.models import ProposalPKM,Anggota,CobaMultipleInput,LogHistoryPKM

class DownloadForm(forms.ModelForm):
    class Meta:
        model = ProposalPKM
        fields = ('idStatus',)
class UploadRevisiForm(forms.ModelForm):
    class Meta:
        model = LogHistoryPKM
        fields = ('document','idStatus','idKetua','idDosenReviewer',)
