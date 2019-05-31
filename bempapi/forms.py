from django import forms
from papi.models import ProposalPKM

class InputDosenReviewer(forms.ModelForm):
    class Meta:
        model = ProposalPKM
        fields = ('idDosenReviewer',)
class TimelineForms(forms.ModelForm):
    date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
