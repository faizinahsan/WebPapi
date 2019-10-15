from django import forms
from .models import ProposalPKM, Anggota, CobaMultipleInput, DosenPembimbing, LogHistoryPKM
# from .models import Registration


class UploadPKMForm(forms.ModelForm):
    class Meta:
        model = ProposalPKM
        fields = ('judul', 'namaKetua', 'deskripsi', 'document', 'idFakultas',
                  'idBidang', 'idKategori', 'idStatus', 'idDosenReviewer')


class AnggotaPKMForm(forms.ModelForm):
    class Meta:
        model = Anggota
        fields = ('namaAnggota', 'npmAnggota', 'emailAnggota')


class DosenPembimbingForm(forms.ModelForm):
    class Meta:
        model = DosenPembimbing
        fields = ('namaDosen', 'nipDosen', 'emailDosen')


class MultipleInputForm(forms.ModelForm):
    class Meta:
        model = CobaMultipleInput
        fields = ('namaInput', 'emailInput')


class LogHistoryUploadForm(forms.ModelForm):
    class Meta:
        model = LogHistoryPKM
        fields = ('idProposalPkm', 'idKetua', 'deskripsiLog',)
# class UpdatePKMForm (forms.ModelForm):
#     class Meta:
#         model = Propo
