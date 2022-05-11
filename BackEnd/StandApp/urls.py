from StandApp import viewProfiling
from StandApp import viewsConcoCSC
from StandApp import viewsStatCSC
from StandApp import viewsStatALG
from StandApp import viewsStatTUN
from StandApp import viewsMesureCSC
from StandApp import viewsMesureALG
from StandApp import viewsMesureTUN
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'stat-csc/', csrf_exempt(viewsStatCSC.StatCSC), name='file'),
    url(r'stat-csc-info/', csrf_exempt(viewsStatCSC.StatCSCInfo), name='file'),
    url(r'stat-csc-obj/', csrf_exempt(viewsStatCSC.StatCSCObj), name='file'),
    url(r'stat-csc-plus/', csrf_exempt(viewsStatCSC.StatCSCPLUS), name='file'),

    url(r'stat-alg/', csrf_exempt(viewsStatALG.StatALG), name='file'),
    url(r'stat-alg-info/', csrf_exempt(viewsStatALG.StatALGInfo), name='file'),
    url(r'stat-alg-obj/', csrf_exempt(viewsStatALG.StatALGObj), name='file'),
    url(r'stat-alg-plus/', csrf_exempt(viewsStatALG.StatALGPLUS), name='file'),
    
    url(r'stat-tun/', csrf_exempt(viewsStatTUN.StatTUN), name='file'),
    url(r'stat-tun-info/', csrf_exempt(viewsStatTUN.StatTUNInfo), name='file'),
    url(r'stat-tun-obj/', csrf_exempt(viewsStatTUN.StatTUNObj), name='file'),
    url(r'stat-tun-plus/', csrf_exempt(viewsStatTUN.StatTUNPLUS), name='file'),

    url(r'mesure-csc/', csrf_exempt(viewsMesureCSC.MesureCSC), name='file'),
    url(r'mesure-csc-plus/', csrf_exempt(viewsMesureCSC.MesureCSCPLUS), name='file'),
    url(r'mesure-alg/', csrf_exempt(viewsMesureALG.MesureALG), name='file'),
    url(r'mesure-alg-plus/', csrf_exempt(viewsMesureALG.MesureALGPLUS), name='file'),
    url(r'mesure-tun/', csrf_exempt(viewsMesureTUN.MesureTUN), name='file'),
    url(r'mesure-tun-plus/', csrf_exempt(viewsMesureTUN.MesureTUNPLUS), name='file'),

    url(r'report-csc/', csrf_exempt(viewsMesureCSC.ReportCSC), name='file'),
    url(r'report-alg/', csrf_exempt(viewsMesureALG.ReportALG), name='file'),
    url(r'report-tun/', csrf_exempt(viewsMesureTUN.ReportTUN), name='file'),

    url(r'profiling/', csrf_exempt(viewProfiling.pandasProfiling), name='file'),
    url(r'sweetviz/', csrf_exempt(viewProfiling.sweetviz), name='file'),
    url(r'pandasgui/', csrf_exempt(viewProfiling.pandasgui), name='file'),

    url(r'conco-csc/', csrf_exempt(viewsConcoCSC.ConcoCSC), name='file'),
]
