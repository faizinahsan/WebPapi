from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('upload-page/', views.upload_pkm, name='upload-page'),
    path('multiple-input/', views.coba_multiple_input, name='multiple-input'),
    path('input-anggota/', views.input_anggota, name='input-anggota'),
    path('proposal-pkm/<idPkm>/', views.proposal_pkm_page, name='proposal-pkm'),
    path('download-format/', views.download_format_pkm, name='format-pkm'),
    path('info-dosen/', views.info_dosen, name='info-dosen'),
    path('log-file/', views.log_file, name='log-file'),
    path('list-format', views.list_format, name='list-format'),
    path('dashboard-mhs', views.dashboard_mhs, name='dashboard-mhs'),
    path('input-dospem', views.input_dospem, name='input-dospem'),
    path('timeline-mahasiswa', views.timeline_mahasiswa, name='timeline-mahasiswa'),
    path('download_revisi/<path>/',
         views.download_revisi, name='download-revisi'),
    path('update/<idUsers>', views.update_pkm, name='update-pkm'),
    path('list_anggota/<idUser>', views.list_anggota, name='list-anggota'),
    path('view_dosbim/<idUser>', views.view_dosbim, name='view-dosbim'),
    path('update_anggota/<idAnggota>/',
         views.update_anggota, name='update-anggota'),
    path('update_dosbim/<idDosbim>/',
         views.update_dosbim, name='update-dosbim'),
]
