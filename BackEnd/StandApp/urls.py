from StandApp import views
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'stat-csc/', csrf_exempt(views.StatCSC), name='file'),
    url(r'stat-csc-plus/', csrf_exempt(views.StatCSCPLUS), name='file'),
    url(r'stat-alg/', csrf_exempt(views.StatALG), name='file'),
    url(r'stat-ita-ctn/', csrf_exempt(views.StatITA), name='file'),
    url(r'stat-tun-ctn/', csrf_exempt(views.StatTUNCTN), name='file'),
    url(r'stat-tun-cl/', csrf_exempt(views.StatTUNCL), name='file'),
    
]
