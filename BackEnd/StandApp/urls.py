from StandApp import views
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'stat-csc/', csrf_exempt(views.StatFile), name='file'),
]
