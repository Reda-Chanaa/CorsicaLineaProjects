from .settings import *
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
'default': {
# 'ENGINE': 'django.db.backends.sqlite3',
# 'NAME': 'db.sqlite3',
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'yield',
'USER': 'postgres',
'PASSWORD' : '2022',
'HOST': 'localhost',
'PORT': '5432',
}
}
