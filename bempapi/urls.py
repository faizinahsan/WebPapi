from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.akumulasi_pkm,name='akumulasi-pkm'),
    path('timeline_pkm/',views.timeline_pkm,name='timeline-pkm'),
    path('manage_pkm/',views.manage_pkm,name='manage-pkm'),
    path('manage_dosen/<idPkm>/',views.manage_dosen,name='manage-dosen'),
    path('list_pkm/',views.list_pkm,name="list-pkm-pengurus"),
    path('list_pkm/<idStatus>/', views.list_pkm_withId, name="list-pkm-withId"),
    path('upload_format_pkm/', views.upload_format_pkm, name="upload-format-pkm"),
]