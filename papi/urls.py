from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('upload-page/',views.upload_pkm,name='upload-page'),
    path('multiple-input/',views.coba_multiple_input,name='multiple-input'),
    path('input-anggota/<idPkm>/',views.input_anggota,name='input-anggota'),
    path('proposal-pkm/<idPkm>/',views.proposal_pkm_page,name='proposal-pkm'),
]