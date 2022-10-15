from django.contrib import admin
from django.urls import path
from beranda.views import indexberanda
from evaluasi.views import indexevaluasi
from materi.views import indexmateri
from profil.views import indexprofil
from rangkuman.views import indexrangkuman
from tujuan.views import indextujuan 
from polabilangan.views import indexpolabilangan
from barisanbilangan.views import indexbarisanbilangan
from deretbilangan.views import indexderetbilangan
from latihan.views import indexlatihan

urlpatterns = [
    path('admin/', admin.site.urls),
    path('beranda/', indexberanda),
    path('evaluasi/', indexevaluasi),
    path('materi/', indexmateri),
    path('profil/', indexprofil),
    path('rangkuman/', indexrangkuman),
    path('tujuan/', indextujuan),
    path('polabilangan/', indexpolabilangan),
    path('barisanbilangan/', indexbarisanbilangan),
    path('deretbilangan/', indexderetbilangan),
    path('latihan/', indexlatihan),
]
