from rest_framework import serializers
from .models import MesureAlgerie, MesureCorse, MesureTunisie, ReportingAlgerie, ReportingCorse, ReportingTunisie


class MesureCSCSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesureCorse
        fields = ('anneeReport','date','jour','mois','annee','jan','fev','mar','apr','may','jun','jul','aug','sep','oct','nov','dec')
        
class MesureALGSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesureAlgerie
        fields = ('anneeReport','date','jour','mois','annee','jan','fev','mar','apr','may','jun','jul','aug','sep','oct','nov','dec')

class MesureTUNSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesureTunisie
        fields = ('anneeReport','date','jour','mois','annee','jan','fev','mar','apr','may','jun','jul','aug','sep','oct','nov','dec')

class ReportingTUNSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportingTunisie
        fields = ('annee','mois','cible','budget','objectif')

class ReportingALGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportingAlgerie
        fields = ('annee','mois','cible','budget','objectif')

class ReportingCSCSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportingCorse
        fields = ('annee','mois','cible','budget','objectif')