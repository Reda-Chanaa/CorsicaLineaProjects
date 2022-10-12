from .settings import *

DEBUG = False

#SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['0.0.0.0', 'localhost','192.168.178.231','P-CLYIELDAPP-A-01.corsicalinea.net']
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
'default': {
# 'ENGINE': 'django.db.backends.sqlite3',
# 'NAME': 'db.sqlite3',
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'YIELD',
'USER': 'YIELD',
'PASSWORD' : '2022',
'HOST': '192.168.172.58',
'PORT': '5432',
}
}
