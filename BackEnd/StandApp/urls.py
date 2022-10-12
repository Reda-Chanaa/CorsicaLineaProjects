from StandApp import viewProfiling
from StandApp import viewsConcoCSC
from StandApp import viewsConcoALG
from StandApp import viewsConcoTUN
from StandApp import viewsStatCSC
from StandApp import viewsStatALG
from StandApp import viewsStatTUN
from StandApp import viewsMesureCSC
from StandApp import viewsMesureALG
from StandApp import viewsMesureTUN
from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(r'stat-csc/', csrf_exempt(viewsStatCSC.StatCSC), name='file'),
    re_path(r'stat-csc-info/', csrf_exempt(viewsStatCSC.StatCSCInfo), name='file'),
    re_path(r'stat-csc-obj/', csrf_exempt(viewsStatCSC.StatCSCObj), name='file'),
    re_path(r'stat-csc-plus/', csrf_exempt(viewsStatCSC.StatCSCPLUS), name='file'),

    re_path(r'stat-alg/', csrf_exempt(viewsStatALG.StatALG), name='file'),
    re_path(r'stat-alg-info/', csrf_exempt(viewsStatALG.StatALGInfo), name='file'),
    re_path(r'stat-alg-obj/', csrf_exempt(viewsStatALG.StatALGObj), name='file'),
    re_path(r'stat-alg-plus/', csrf_exempt(viewsStatALG.StatALGPLUS), name='file'),
    
    re_path(r'stat-tun/', csrf_exempt(viewsStatTUN.StatTUN), name='file'),
    re_path(r'stat-tun-info/', csrf_exempt(viewsStatTUN.StatTUNInfo), name='file'),
    re_path(r'stat-tun-obj/', csrf_exempt(viewsStatTUN.StatTUNObj), name='file'),
    re_path(r'stat-tun-plus/', csrf_exempt(viewsStatTUN.StatTUNPLUS), name='file'),

    re_path(r'mesure-csc/', csrf_exempt(viewsMesureCSC.MesureCSC), name='file'),
    re_path(r'mesure-csc-plus/', csrf_exempt(viewsMesureCSC.MesureCSCPLUS), name='file'),
    re_path(r'mesure-alg/', csrf_exempt(viewsMesureALG.MesureALG), name='file'),
    re_path(r'mesure-alg-plus/', csrf_exempt(viewsMesureALG.MesureALGPLUS), name='file'),
    re_path(r'mesure-tun/', csrf_exempt(viewsMesureTUN.MesureTUN), name='file'),
    re_path(r'mesure-tun-plus/', csrf_exempt(viewsMesureTUN.MesureTUNPLUS), name='file'),

    re_path(r'report-csc/', csrf_exempt(viewsMesureCSC.ReportCSC), name='file'),
    re_path(r'report-alg/', csrf_exempt(viewsMesureALG.ReportALG), name='file'),
    re_path(r'report-tun/', csrf_exempt(viewsMesureTUN.ReportTUN), name='file'),

    #re_path(r'profiling/', csrf_exempt(viewProfiling.pandasProfiling), name='file'),
    re_path(r'sweetviz/', csrf_exempt(viewProfiling.sweetviz), name='file'),
    #re_path(r'pandasgui/', csrf_exempt(viewProfiling.pandasgui), name='file'),
    re_path(r'getcolumn/', csrf_exempt(viewProfiling.getcolumn), name='file'),

    re_path(r'conco-csc/', csrf_exempt(viewsConcoCSC.ConcoCSC), name='file'),
    re_path(r'conco-tun/', csrf_exempt(viewsConcoTUN.ConcoTUN), name='file'),
    re_path(r'conco-alg/', csrf_exempt(viewsConcoALG.ConcoALG), name='file'),
]
