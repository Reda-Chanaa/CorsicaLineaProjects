from django.db import models

# Create your models here.

class MesureCorse(models.Model):
    Annee_Report = models.CharField(max_length=25)
    Date = models.CharField(max_length=25)
    Jour = models.CharField(max_length=10)
    Mois = models.CharField(max_length=10)
    Annee = models.CharField(max_length=10)
    Jan = models.CharField(max_length=10)
    Feb = models.CharField(max_length=10)
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
    Annee_Report = models.CharField(max_length=25)
    Date = models.CharField(max_length=25)
    Jour = models.CharField(max_length=10)
    Mois = models.CharField(max_length=10)
    Annee = models.CharField(max_length=10)
    Jan = models.CharField(max_length=10)
    Feb = models.CharField(max_length=10)
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
    Annee_Report = models.CharField(max_length=25)
    Date = models.CharField(max_length=25)
    Jour = models.CharField(max_length=10)
    Mois = models.CharField(max_length=10)
    Annee = models.CharField(max_length=10)
    Jan = models.CharField(max_length=10)
    Feb = models.CharField(max_length=10)
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
    Annee = models.CharField(max_length=10)
    Mois = models.CharField(max_length=10)
    Cible = models.CharField(max_length=10)
    Budget = models.CharField(max_length=10)
    Objectif = models.CharField(max_length=10)

class ReportingAlgerie(models.Model):
    Annee = models.CharField(max_length=10)
    Mois = models.CharField(max_length=10)
    Cible = models.CharField(max_length=10)
    Budget = models.CharField(max_length=10)
    Objectif = models.CharField(max_length=10)

class ReportingTunisie(models.Model):
    Annee = models.CharField(max_length=10)
    Mois = models.CharField(max_length=10)
    Cible = models.CharField(max_length=10)
    Budget = models.CharField(max_length=10)
    Objectif = models.CharField(max_length=10)

