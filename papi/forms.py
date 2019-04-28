from django import forms
from .models import ProposalPKM,Anggota,CobaMultipleInput
# from .models import Registration
class UploadPKMForm(forms.ModelForm):
    class Meta:
        model = ProposalPKM
        fields = ('judul','namaKetua','document','deskripsi','idKategori','idBidang','idStatus')
class AnggotaPKMForm(forms.ModelForm):
    class Meta:
        model = Anggota
        fields = ('namaAnggota','npmAnggota','emailAnggota')
class MultipleInputForm(forms.ModelForm):
    class Meta:
        model = CobaMultipleInput
        fields = ('namaInput','emailInput')