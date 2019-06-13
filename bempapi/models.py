from django.db import models
from papi.models import BidangPKM
# Create your models here.


class FormatProposalPKM(models.Model):
    bidangPKM = models.ForeignKey(
        BidangPKM, on_delete=models.CASCADE, null=True)
    documentFormat = models.FileField(
        upload_to='format', default='ProposalDefault.txt')

    def __str__(self):
        return f'{self.bidangPKM}'
