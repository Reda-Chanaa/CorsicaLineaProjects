from StandApp import views
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'stat-csc/', csrf_exempt(views.StatFile), name='file'),
    url(r'stat-csc-plus/', csrf_exempt(views.StatFilePlus), name='file'),
    url(r'stat-alg/', csrf_exempt(views.StatALG), name='file'),
]
