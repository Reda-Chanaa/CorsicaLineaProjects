from StandApp import views
from StandApp import viewsALG
from StandApp import viewsTUN
from StandApp import viewsMesure
from StandApp import viewsMesureALG
from StandApp import viewsMesureTUN
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'stat-csc/', csrf_exempt(views.StatCSC), name='file'),
    url(r'stat-csc-info/', csrf_exempt(views.StatCSCInfo), name='file'),
    url(r'stat-csc-obj/', csrf_exempt(views.StatCSCObj), name='file'),
    url(r'stat-csc-plus/', csrf_exempt(views.StatCSCPLUS), name='file'),

    url(r'stat-alg/', csrf_exempt(viewsALG.StatALG), name='file'),
    url(r'stat-alg-info/', csrf_exempt(viewsALG.StatALGInfo), name='file'),
    url(r'stat-alg-obj/', csrf_exempt(viewsALG.StatALGObj), name='file'),
    url(r'stat-alg-plus/', csrf_exempt(viewsALG.StatALGPLUS), name='file'),
    
    url(r'stat-tun/', csrf_exempt(viewsTUN.StatTUN), name='file'),
    url(r'stat-tun-info/', csrf_exempt(viewsTUN.StatTUNInfo), name='file'),
    url(r'stat-tun-obj/', csrf_exempt(viewsTUN.StatTUNObj), name='file'),
    url(r'stat-tun-plus/', csrf_exempt(viewsTUN.StatTUNPLUS), name='file'),

    url(r'mesure-csc/', csrf_exempt(viewsMesure.MesureCSC), name='file'),
    url(r'mesure-alg/', csrf_exempt(viewsMesureALG.MesureALG), name='file'),
    url(r'mesure-tun/', csrf_exempt(viewsMesureTUN.MesureTUN), name='file'),

    url(r'report-csc/', csrf_exempt(viewsMesure.ReportCSC), name='file'),
    url(r'report-alg/', csrf_exempt(viewsMesureALG.ReportALG), name='file'),
    url(r'report-tun/', csrf_exempt(viewsMesureTUN.ReportTUN), name='file'),
]
