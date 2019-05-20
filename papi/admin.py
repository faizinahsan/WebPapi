from django.contrib import admin
from .models import ProposalPKM,KategoriPKM,BidangPKM,StatusRevisi,Anggota,LogHistoryPKM,CobaMultipleInput,DosenPembimbing
# Register your models here.
admin.site.register(ProposalPKM)
admin.site.register(KategoriPKM)
admin.site.register(BidangPKM)
admin.site.register(StatusRevisi)
admin.site.register(Anggota)
admin.site.register(LogHistoryPKM)
admin.site.register(CobaMultipleInput)
admin.site.register(DosenPembimbing)