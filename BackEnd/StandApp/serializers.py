from rest_framework import serializers
from .models import MesureAlgerie, MesureCorse, MesureTunisie, ReportingAlgerie, ReportingCorse, ReportingTunisie


class MesureCSCSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesureCorse
        fields = ('Annee_Report','Date','Jour','Mois','Annee','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
        
class MesureALGSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesureAlgerie
        fields = ('Annee_Report','Date','Jour','Mois','Annee','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')

class MesureTUNSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesureTunisie
        fields = ('Annee_Report','Date','Jour','Mois','Annee','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')

class ReportingTUNSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportingTunisie
        fields = ('Annee','Mois','Cible','Budget','Objectif')

class ReportingALGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportingAlgerie
        fields = ('Annee','Mois','Cible','Budget','Objectif')

class ReportingCSCSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportingCorse
        fields = ('Annee','Mois','Cible','Budget','Objectif')