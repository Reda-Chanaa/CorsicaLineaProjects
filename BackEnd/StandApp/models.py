from django.db import models

# Create your models here.

class MesureCorse(models.Model):
    Annee_Report = models.CharField(max_length=20)
    Date = models.CharField(max_length=20)
    Jour = models.CharField(max_length=10)
    Mois = models.CharField(max_length=10)
    Annee = models.CharField(max_length=10)
    Jan = models.CharField(max_length=10)
    Fev = models.CharField(max_length=10)
    Mar = models.CharField(max_length=10)
    Apr = models.CharField(max_length=10)
    May = models.CharField(max_length=10)
    Jun = models.CharField(max_length=10)
    Jul = models.CharField(max_length=10)
    Aug = models.CharField(max_length=10)
    Sep = models.CharField(max_length=10)
    Oct = models.CharField(max_length=10)
    Nov = models.CharField(max_length=10)
    Dec = models.CharField(max_length=10)


class MesureAlgerie(models.Model):
    Annee_Report = models.CharField(max_length=20)
    Date = models.CharField(max_length=20)
    Jour = models.CharField(max_length=10)
    Mois = models.CharField(max_length=10)
    Annee = models.CharField(max_length=10)
    Jan = models.CharField(max_length=10)
    Fev = models.CharField(max_length=10)
    Mar = models.CharField(max_length=10)
    Apr = models.CharField(max_length=10)
    May = models.CharField(max_length=10)
    Jun = models.CharField(max_length=10)
    Jul = models.CharField(max_length=10)
    Aug = models.CharField(max_length=10)
    Sep = models.CharField(max_length=10)
    Oct = models.CharField(max_length=10)
    Nov = models.CharField(max_length=10)
    Dec = models.CharField(max_length=10)

class MesureTunisie(models.Model):
    Annee_Report = models.CharField(max_length=20)
    Date = models.CharField(max_length=20)
    Jour = models.CharField(max_length=10)
    Mois = models.CharField(max_length=10)
    Annee = models.CharField(max_length=10)
    Jan = models.CharField(max_length=10)
    Fev = models.CharField(max_length=10)
    Mar = models.CharField(max_length=10)
    Apr = models.CharField(max_length=10)
    May = models.CharField(max_length=10)
    Jun = models.CharField(max_length=10)
    Jul = models.CharField(max_length=10)
    Aug = models.CharField(max_length=10)
    Sep = models.CharField(max_length=10)
    Oct = models.CharField(max_length=10)
    Nov = models.CharField(max_length=10)
    Dec = models.CharField(max_length=10)

class ReportingCorse(models.Model):
    annee = models.CharField(max_length=10)
    mois = models.CharField(max_length=10)
    cible = models.CharField(max_length=10)
    budget = models.CharField(max_length=10)
    objectif = models.CharField(max_length=10)

class ReportingAlgerie(models.Model):
    annee = models.CharField(max_length=10)
    mois = models.CharField(max_length=10)
    cible = models.CharField(max_length=10)
    budget = models.CharField(max_length=10)
    objectif = models.CharField(max_length=10)

class ReportingTunisie(models.Model):
    annee = models.CharField(max_length=10)
    mois = models.CharField(max_length=10)
    cible = models.CharField(max_length=10)
    budget = models.CharField(max_length=10)
    objectif = models.CharField(max_length=10)

