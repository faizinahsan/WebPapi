from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.akumulasi_pkm,name='akumulasi-pkm'),
    path('timeline_pkm/',views.timeline_pkm,name='timeline-pkm'),
    path('manage_pkm/',views.manage_pkm,name='manage-pkm'),
]