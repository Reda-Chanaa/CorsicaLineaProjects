import os
import time
import json
import pandas as pd
import webbrowser
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
import numpy as np
import sweetviz as sv

# Statistiques avec pandas profiling
'''
def pandasProfiling(request):
    start_time = time.time()
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        #File = JSONParser().parse(request)
        df1 = pd.read_csv(File1, encoding="utf8", sep=';', index_col=False)
        
        print(df1)
        # get html profile (minimal= True) pour ne pas avoir bcp d'informations sur le profiling (une optimisation d'information)
        # profile = ProfileReport(newdf1, title="Pandas Profiling Report", minimal=True)
        profile = ProfileReport(df1, title="Profilage des données", explorative=True)
        #profile = ProfileReport(newdf1, title="Data Profiling")
        # profile
        profile.to_file(output_file="./templates/profiling.html")
        html = open('./templates/profiling.html', 'r')
        mystr = html.read()
    total = time.time() - start_time
    print(total)
    # pour choisir d'ouvrir le profiling dans le navigateur
    webbrowser.get().open("file://" +
                          os.path.realpath("./templates/profiling.html"),
                          new=0,
                          autoraise=True)
    # pour retourner en response le résultat text de la page html du profiling
    return HttpResponse(json.dumps(mystr), content_type='text/plain')
'''
# Statistiques avec sweet Viz
def sweetviz(request):
    start_time = time.time()
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        #File = JSONParser().parse(request)
        df1 = pd.read_csv(File1, encoding="utf-8", sep=';', index_col=False)
        
        df1.drop(columns={"COM", "SAIL_ID","DATE_DEPART","GI","STATUS","DSP","PAIEMENT"}, axis=1,inplace=True)
        my_report = sv.analyze(df1,target_feat='PAX')
        my_report.show_html()
        
    total = time.time() - start_time
    print(total)
    # pour retourner en response le résultat text de la page html du profiling
    return HttpResponse(total, content_type='text/plain')

# Statistiques avec pandas GUI
'''
def pandasgui(request):
    start_time = time.time()
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        #File = JSONParser().parse(request)
        df1 = pd.read_csv(File1, encoding="utf8" ,sep=';', index_col=False)
        
        #Deploy the GUI of the mpg dataset
        show(df1,)
    total = time.time() - start_time
    print(total)
    # pour retourner en response le résultat text de la page html du profiling
    return HttpResponse(total, content_type='text/plain')
'''
# get column
def getcolumn(request):
    start_time = time.time()
    if request.method == 'POST':
        File1 = request.FILES["file1"]
        #File = JSONParser().parse(request)
        df1 = pd.read_csv(File1, encoding="utf8" ,sep=';', index_col=False)
        
        #Deploy the GUI of the mpg dataset
        table=[]
        i=0
        for col in df1.columns:
            table.append({ 'id': i, 'name': col })
            i=i+1

    total = time.time() - start_time
    print(total)
    # pour retourner en response le résultat text de la page html du profiling
    return HttpResponse(json.dumps(table))