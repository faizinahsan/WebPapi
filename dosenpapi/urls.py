from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard_dosen,name='dashboard-dosen'),
    path('list-pkm-dosen/<idStatus>/',views.list_pkm_dosen,name='list-pkm-dosen'),
    path('download-pkm/<path>/', views.download_pkm, name='download-pkm'),
]